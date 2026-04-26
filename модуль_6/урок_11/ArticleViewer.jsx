import { useState, useEffect } from 'react'

function ArticleViewer({ articleId }) {
	const [article, setArticle] = useState(null)
	const [loading, setLoading] = useState(true)
	const [error, setError] = useState(null)

	useEffect(() => {
		const fetchArticle = async () => {
			try {
				setLoading(true)
				setError(null)
				const response = await fetch(`/api/articles/${articleId}`)

				if (!response.ok) {
					throw new Error('Не удалось загрузить статью')
				}

				const data = await response.json()
				setArticle(data)
			} catch (err) {
				setError(err.message)
			} finally {
				setLoading(false)
			}
		}

		fetchArticle()
	}, [articleId])

	if (loading) {
		return (
			<div className='loading-container'>
				<div className='spinner'></div>
				<p>Загружаем статью...</p>
			</div>
		)
	}

	if (error) {
		return (
			<div className='error-container'>
				<h3>Ошибка загрузки</h3>
				<p>{error}</p>
				<button onClick={() => window.location.reload()}>
					Попробовать снова
				</button>
			</div>
		)
	}

	if (!article) {
		return (
			<div className='empty-state'>
				<p>Статья не найдена</p>
			</div>
		)
	}

	return (
		<article className='article-content'>
			<h1>{article.title}</h1>
			<div className='article-meta'>
				<span>Автор: {article.author}</span>
				<span>Дата: {new Date(article.createdAt).toLocaleDateString()}</span>
			</div>
			<div className='article-body'>{article.content}</div>
		</article>
	)
}
