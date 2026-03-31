import requests
import sqlite3
from bs4 import BeautifulSoup
from typing import List, Dict, Any


class BlogArticle:
    """Класс для представления статьи блога"""
    def __init__(self, title: str, text: str):
        self.title = title.strip()
        self.text = text.strip()

    def to_dict(self) -> Dict[str, str]:
        return {'title': self.title, 'text': self.text}

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> 'BlogArticle':
        return cls(title=data['title'], text=data['text'])


class BlogParser:
    """Парсер для сбора статей с блога Top Academy"""
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/120.0.0.0 Safari/537.36'
        })

    def fetch_html(self, url: str) -> str:
        """Загружает HTML-код страницы"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Ошибка при загрузке {url}: {e}")
            return ""

    def parse_articles(self, html: str) -> List[BlogArticle]:
        """Извлекает статьи из HTML-кода с правильными селекторами"""
        if not html:
            return []

        soup = BeautifulSoup(html, 'html.parser')
        articles = []

        article_cards = soup.find_all('article') or soup.find_all(
            'div', class_=lambda x: x and (
                'card' in x.lower() or
                'article' in x.lower() or
                'post' in x.lower()
            )
        )

        if not article_cards:
            all_divs = soup.find_all('div', class_=True)
            article_cards = [
                div for div in all_divs if any(
                    word in div.get('class', [''])[0].lower()
                    for word in ['card', 'article', 'post', 'blog', 'item']
                )
            ]

        print(f"Найдено потенциальных карточек статей: {len(article_cards)}")

        for i, card in enumerate(article_cards, 1):
            try:
                title = ""
                for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    title_tag = card.find(
                        tag,
                        class_=lambda x: x and any(
                            word in x.lower()
                            for word in ['title', 'header', 'name', 'heading']
                        )
                    )
                    if title_tag:
                        title = title_tag.get_text(strip=True)
                        break

                if not title:
                    header = card.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                    if header:
                        title = header.get_text(strip=True)

                if not title:
                    title_link = card.find('a', title=True)
                    if title_link and title_link.get('title'):
                        title = title_link['title']

                if not title:
                    for tag in ['span', 'div', 'p']:
                        title_elem = card.find(
                            tag,
                            class_=lambda x: x and 'title' in x.lower()
                        )
                        if title_elem:
                            title = title_elem.get_text(strip=True)
                            break

                if not title or len(title) < 5:
                    print(f"  Карточка {i}: заголовок не найден")
                    continue

                text_parts = []
                paragraphs = card.find_all('p')
                for p in paragraphs:
                    p_text = p.get_text(strip=True)
                    if p_text and len(p_text) > 10:
                        text_parts.append(p_text)

                if not text_parts:
                    text_divs = card.find_all(
                        'div',
                        class_=lambda x: x and any(
                            word in x.lower()
                            for word in ['content', 'text', 'body',
                                         'description', 'excerpt']
                        )
                    )
                    for div in text_divs:
                        div_text = div.get_text(strip=True)
                        if div_text and len(div_text) > 10:
                            text_parts.append(div_text)

                if not text_parts:
                    all_text = card.get_text(strip=True)
                    if title in all_text:
                        all_text = all_text.replace(title, '').strip()
                    if len(all_text) > 20:
                        text_parts.append(all_text[:500])

                if text_parts:
                    full_text = ' '.join(text_parts)
                    if len(full_text) > 1000:
                        full_text = full_text[:1000] + "..."

                    article = BlogArticle(title=title, text=full_text)
                    articles.append(article)
                    print(f"  Статья {len(articles)}: '{title[:50]}...'")

            except Exception as e:
                print(f"  Ошибка при обработке карточки {i}: {e}")
                continue

        return articles


class BlogDatabase:
    """Класс для работы с базой данных SQLite"""
    def __init__(self, db_name: str = 'top_academy_blog.db'):
        self.db_name = db_name
        self.connection = None
        self.init_database()

    def init_database(self):
        """Инициализирует базу данных"""
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT UNIQUE NOT NULL,
                    text TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при создании БД: {e}")

    def save_articles(self, articles: List[BlogArticle]) -> int:
        """Сохраняет статьи в БД"""
        if not articles:
            return 0

        saved_count = 0
        try:
            cursor = self.connection.cursor()
            for article in articles:
                try:
                    cursor.execute(
                        'INSERT OR IGNORE INTO articles (title, text) '
                        'VALUES (?, ?)',
                        (article.title, article.text)
                    )
                    if cursor.rowcount > 0:
                        saved_count += 1
                except sqlite3.IntegrityError:
                    continue
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при сохранении: {e}")

        return saved_count

    def get_recent_articles(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Получает последние статьи"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                'SELECT id, title, text FROM articles '
                'ORDER BY id DESC LIMIT ?',
                (limit,)
            )
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Ошибка при получении статей: {e}")
            return []

    def close(self):
        """Закрывает соединение"""
        if self.connection:
            self.connection.close()


def main():
    """Основная функция"""
    BASE_URL = "https://msk.top-academy.ru/blog"

    print(f"Парсинг страницы {BASE_URL}...")

    parser = BlogParser(BASE_URL)

    html = parser.fetch_html(BASE_URL)
    if not html:
        print("Не удалось загрузить страницу.")
        return

    print("Извлечение статей...")
    articles = parser.parse_articles(html)
    print(f"\nНайдено {len(articles)} статей.")

    if articles:
        print("\nСохранение данных в базу данных...")
        db = BlogDatabase()
        saved_count = db.save_articles(articles)
        print(f"Успешно сохранено {saved_count} статей в {db.db_name}.")

        print("\nПоследние 5 добавленных статей:")
        print("-" * 60)
        recent_articles = db.get_recent_articles(5)

        for i, article in enumerate(recent_articles, 1):
            print(f"{i}. Заголовок: {article['title']}")
            preview = article['text'][:150] + "..." \
                if len(article['text']) > 150 else article['text']
            print(f"   Текст: {preview}\n")

        db.close()
    else:
        print("Статьи не найдены. Проверьте CSS-селекторы.")

    print("-" * 60)
    print("Парсинг завершен.")


if __name__ == "__main__":
    main()
