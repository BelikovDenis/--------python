function TaskList({ tasks }) {
  return (
    <div className='task-container'>
      <h2>Список задач</h2>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>
            <span className='task-title'>{task.title}</span>
            <span className='task-status'>{task.completed ? '✓' : '○'}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}






function ContactList({ contacts }) {
  return (
    <div className='contacts-wrapper'>
      <h3>Список контактов</h3>
      {contacts.map(contact => (
        <div key={contact.id} className='contact-card'>
          <img src={contact.avatar} alt={`${contact.name} avatar`} />
          <div className='contact-info'>
            <h4>{contact.name}</h4>
            <p>{contact.email}</p>
            <p>{contact.phone}</p>
          </div>
          <div className='contact-actions'>
            <button>Редактировать</button>
            <button>Удалить</button>
          </div>
        </div>
      ))}
    </div>
  )
}






// Корректный подход
function ProductList({ products }) {
  return (
    <div>
      {products.map(product => (
        <div key={product.sku} className='product-item'>
          <h3>{product.name}</h3>
          <p>{product.price}</p>
          <input type='number' placeholder='Количество' />
        </div>
      ))}
    </div>
  )
}








function ProjectDashboard({ projects }) {
  return (
    <div className='dashboard'>
      <h1>Панель управления проектами</h1>
      {projects.map(project => (
        <div key={project.id} className='project-section'>
          <div className='project-header'>
            <h2>{project.name}</h2>
            <span className='project-status'>{project.status}</span>
            <p className='project-description'>{project.description}</p>
          </div>

          <div className='tasks-section'>
            <h3>Задачи ({project.tasks.length})</h3>
            {project.tasks.length > 0 ? (
              <div className='tasks-grid'>
                {project.tasks.map(task => (
                  <div key={task.id} className='task-card'>
                    <h4>{task.title}</h4>
                    <p>{task.description}</p>
                    <div className='task-meta'>
                      <span>Приоритет: {task.priority}</span>
                      <span>
                        Срок: {new Date(task.dueDate).toLocaleDateString()}
                      </span>
                    </div>

                    {task.comments && task.comments.length > 0 && (
                      <div className='comments-section'>
                        <h5>Комментарии:</h5>
                        {task.comments.map(comment => (
                          <div key={comment.id} className='comment'>
                            <strong>{comment.author}:</strong>
                            <span>{comment.text}</span>
                            <small>
                              {new Date(comment.createdAt).toLocaleString()}
                            </small>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            ) : (
              <p className='empty-state'>В проекте пока нет задач</p>
            )}
          </div>
        </div>
      ))}
    </div>
  )
}








import { useState, useMemo } from 'react'

function EmployeeDirectory({ employees }) {
  const [searchTerm, setSearchTerm] = useState('')
  const [departmentFilter, setDepartmentFilter] = useState('all')
  const [sortBy, setSortBy] = useState('name')
  const [sortOrder, setSortOrder] = useState('asc')

  const filteredAndSortedEmployees = useMemo(() => {
    let result = employees

    // Фильтрация по поисковому запросу
    if (searchTerm) {
      result = result.filter(
        employee =>
          employee.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
          employee.email.toLowerCase().includes(searchTerm.toLowerCase())
      )
    }

    // Фильтрация по отделу
    if (departmentFilter !== 'all') {
      result = result.filter(
        employee => employee.department === departmentFilter
      )
    }

    // Сортировка
    result = [...result].sort((a, b) => {
      let aValue = a[sortBy]
      let bValue = b[sortBy]

      if (typeof aValue === 'string') {
        aValue = aValue.toLowerCase()
        bValue = bValue.toLowerCase()
      }

      if (aValue < bValue) {
        return sortOrder === 'asc' ? -1 : 1
      }
      if (aValue > bValue) {
        return sortOrder === 'asc' ? 1 : -1
      }
      return 0
    })

    return result
  }, [employees, searchTerm, departmentFilter, sortBy, sortOrder])

  const uniqueDepartments = useMemo(() => {
    return [...new Set(employees.map(emp => emp.department))]
  }, [employees])

  return (
    <div className='employee-directory'>
      <div className='controls'>
        <input
          type='text'
          placeholder='Поиск сотрудников...'
          value={searchTerm}
          onChange={e => setSearchTerm(e.target.value)}
          className='search-input'
        />

        <select
          value={departmentFilter}
          onChange={e => setDepartmentFilter(e.target.value)}
          className='department-filter'
        >
          <option value='all'>Все отделы</option>
          {uniqueDepartments.map(dept => (
            <option key={dept} value={dept}>
              {dept}
            </option>
          ))}
        </select>

        <select
          value={sortBy}
          onChange={e => setSortBy(e.target.value)}
          className='sort-select'
        >
          <option value='name'>По имени</option>
          <option value='department'>По отделу</option>
          <option value='salary'>По зарплате</option>
          <option value='hireDate'>По дате найма</option>
        </select>

        <button
          onClick={() => setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc')}
          className='sort-order-btn'
        >
          {sortOrder === 'asc' ? '↑' : '↓'}
        </button>
      </div>

      <div className='results-info'>
        Найдено сотрудников: {filteredAndSortedEmployees.length} из{' '}
        {employees.length}
      </div>

      <div className='employees-grid'>
        {filteredAndSortedEmployees.map(employee => (
          <div key={employee.id} className='employee-card'>
            <img src={employee.photo} alt={`${employee.name} photo`} />
            <div className='employee-details'>
              <h3>{employee.name}</h3>
              <p className='position'>{employee.position}</p>
              <p className='department'>{employee.department}</p>
              <p className='email'>{employee.email}</p>
              <p className='hire-date'>
                Дата найма: {new Date(employee.hireDate).toLocaleDateString()}
              </p>
            </div>
          </div>
        ))}
      </div>

      {filteredAndSortedEmployees.length === 0 && (
        <div className='no-results'>
          <p>По вашему запросу ничего не найдено</p>
          <button
            onClick={() => {
              setSearchTerm('')
              setDepartmentFilter('all')
            }}
          >
            Сбросить фильтры
          </button>
        </div>
      )}
    </div>
  )
}







import { useState, useEffect, useRef } from 'react'

function VirtualizedList({ items, itemHeight = 50, containerHeight = 400 }) {
  const [scrollTop, setScrollTop] = useState(0)
  const containerRef = useRef(null)

  const visibleCount = Math.ceil(containerHeight / itemHeight)
  const totalHeight = items.length * itemHeight
  const startIndex = Math.floor(scrollTop / itemHeight)
  const endIndex = Math.min(startIndex + visibleCount + 1, items.length)
  const offsetY = startIndex * itemHeight

  const visibleItems = items.slice(startIndex, endIndex)

  const handleScroll = e => {
    setScrollTop(e.target.scrollTop)
  }

  return (
    <div
      ref={containerRef}
      className='virtualized-container'
      style={{
        height: containerHeight,
        overflow: 'auto',
        position: 'relative',
      }}
      onScroll={handleScroll}
    >
      <div style={{ height: totalHeight, position: 'relative' }}>
        <div
          style={{
            transform: `translateY(${offsetY}px)`,
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
          }}
        >
          {visibleItems.map((item, index) => (
            <div
              key={items[startIndex + index].id}
              style={{
                height: itemHeight,
                display: 'flex',
                alignItems: 'center',
                padding: '0 16px',
                borderBottom: '1px solid #eee',
              }}
            >
              <span>{item.name}</span>
              <span style={{ marginLeft: 'auto' }}>{item.value}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

// Пример использования
function BigDataExample() {
  const generateLargeDataset = () => {
    return Array.from({ length: 10000 }, (_, index) => ({
      id: index,
      name: `Элемент ${index + 1}`,
      value: Math.floor(Math.random() * 1000),
    }))
  }

  const [data] = useState(generateLargeDataset)

  return (
    <div>
      <h2>Виртуализированный список (10,000 элементов)</h2>
      <VirtualizedList items={data} itemHeight={60} containerHeight={500} />
    </div>
  )
}












import { useState } from 'react'

function InteractiveTaskManager() {
  const [tasks, setTasks] = useState([
    {
      id: 1,
      title: 'Изучить React',
      completed: false,
      priority: 'high',
      editing: false,
    },
    {
      id: 2,
      title: 'Написать документацию',
      completed: true,
      priority: 'medium',
      editing: false,
    },
    {
      id: 3,
      title: 'Провести код-ревью',
      completed: false,
      priority: 'low',
      editing: false,
    },
  ])
  const [newTaskTitle, setNewTaskTitle] = useState('')
  const [selectedTasks, setSelectedTasks] = useState(new Set())

  const addTask = () => {
    if (newTaskTitle.trim()) {
      const newTask = {
        id: Date.now(),
        title: newTaskTitle.trim(),
        completed: false,
        priority: 'medium',
        editing: false,
      }
      setTasks(prev => [...prev, newTask])
      setNewTaskTitle('')
    }
  }

  const deleteTask = taskId => {
    setTasks(prev => prev.filter(task => task.id !== taskId))
    setSelectedTasks(prev => {
      const newSet = new Set(prev)
      newSet.delete(taskId)
      return newSet
    })
  }

  const toggleTaskComplete = taskId => {
    setTasks(prev =>
      prev.map(task =>
        task.id === taskId ? { ...task, completed: !task.completed } : task
      )
    )
  }

  const startEditing = taskId => {
    setTasks(prev =>
      prev.map(task =>
        task.id === taskId
          ? { ...task, editing: true }
          : { ...task, editing: false }
      )
    )
  }

  const saveEdit = (taskId, newTitle) => {
    if (newTitle.trim()) {
      setTasks(prev =>
        prev.map(task =>
          task.id === taskId
            ? { ...task, title: newTitle.trim(), editing: false }
            : task
        )
      )
    } else {
      cancelEdit(taskId)
    }
  }

  const cancelEdit = taskId => {
    setTasks(prev =>
      prev.map(task =>
        task.id === taskId ? { ...task, editing: false } : task
      )
    )
  }

  const toggleTaskSelection = taskId => {
    setSelectedTasks(prev => {
      const newSet = new Set(prev)
      if (newSet.has(taskId)) {
        newSet.delete(taskId)
      } else {
        newSet.add(taskId)
      }
      return newSet
    })
  }

  const deleteSelectedTasks = () => {
    setTasks(prev => prev.filter(task => !selectedTasks.has(task.id)))
    setSelectedTasks(new Set())
  }

  const changePriority = (taskId, newPriority) => {
    setTasks(prev =>
      prev.map(task =>
        task.id === taskId ? { ...task, priority: newPriority } : task
      )
    )
  }

  const priorityColors = {
    high: '#ff6b6b',
    medium: '#ffd93d',
    low: '#6bcf7f',
  }

  return (
    <div className='task-manager'>
      <div className='task-input-section'>
        <h2>Менеджер задач</h2>
        <div className='add-task-form'>
          <input
            type='text'
            value={newTaskTitle}
            onChange={e => setNewTaskTitle(e.target.value)}
            placeholder='Введите новую задачу...'
            onKeyPress={e => e.key === 'Enter' && addTask()}
          />
          <button onClick={addTask}>Добавить</button>
        </div>
      </div>

      {selectedTasks.size > 0 && (
        <div className='bulk-actions'>
          <span>Выбрано задач: {selectedTasks.size}</span>
          <button onClick={deleteSelectedTasks} className='delete-btn'>
            Удалить выбранные
          </button>
          <button onClick={() => setSelectedTasks(new Set())}>
            Снять выделение
          </button>
        </div>
      )}

      <div className='tasks-list'>
        {tasks.length === 0 ? (
          <div className='empty-state'>
            <p>Список задач пуст</p>
            <p>Добавьте первую задачу, чтобы начать работу</p>
          </div>
        ) : (
          tasks.map(task => (
            <TaskItem
              key={task.id}
              task={task}
              isSelected={selectedTasks.has(task.id)}
              onToggleComplete={() => toggleTaskComplete(task.id)}
              onDelete={() => deleteTask(task.id)}
              onStartEdit={() => startEditing(task.id)}
              onSaveEdit={newTitle => saveEdit(task.id, newTitle)}
              onCancelEdit={() => cancelEdit(task.id)}
              onToggleSelection={() => toggleTaskSelection(task.id)}
              onChangePriority={newPriority =>
                changePriority(task.id, newPriority)
              }
              priorityColor={priorityColors[task.priority]}
            />
          ))
        )}
      </div>

      <div className='task-stats'>
        <p>Всего задач: {tasks.length}</p>
        <p>Выполнено: {tasks.filter(t => t.completed).length}</p>
        <p>Осталось: {tasks.filter(t => !t.completed).length}</p>
      </div>
    </div>
  )
}

function TaskItem({
  task,
  isSelected,
  onToggleComplete,
  onDelete,
  onStartEdit,
  onSaveEdit,
  onCancelEdit,
  onToggleSelection,
  onChangePriority,
  priorityColor,
}) {
  const [editTitle, setEditTitle] = useState(task.title)

  const handleSave = () => {
    onSaveEdit(editTitle)
  }

  const handleCancel = () => {
    setEditTitle(task.title)
    onCancelEdit()
  }

  return (
    <div
      className={`task-item ${isSelected ? 'selected' : ''} ${
        task.completed ? 'completed' : ''
      }`}
    >
      <input
        type='checkbox'
        checked={isSelected}
        onChange={onToggleSelection}
        className='task-selector'
      />

      <div
        className='priority-indicator'
        style={{ backgroundColor: priorityColor }}
      />

      <input
        type='checkbox'
        checked={task.completed}
        onChange={onToggleComplete}
        className='task-checkbox'
      />

      <div className='task-content'>
        {task.editing ? (
          <div className='edit-form'>
            <input
              type='text'
              value={editTitle}
              onChange={e => setEditTitle(e.target.value)}
              onKeyPress={e => {
                if (e.key === 'Enter') handleSave()
                if (e.key === 'Escape') handleCancel()
              }}
              autoFocus
            />
            <button onClick={handleSave}>Сохранить</button>
            <button onClick={handleCancel}>Отмена</button>
          </div>
        ) : (
          <span className='task-title' onDoubleClick={onStartEdit}>
            {task.title}
          </span>
        )}
      </div>

      <div className='task-actions'>
        <select
          value={task.priority}
          onChange={e => onChangePriority(e.target.value)}
          className='priority-select'
        >
          <option value='low'>Низкий</option>
          <option value='medium'>Средний</option>
          <option value='high'>Высокий</option>
        </select>

        <button onClick={onStartEdit} className='edit-btn'>
          Изменить
        </button>

        <button onClick={onDelete} className='delete-btn'>
          Удалить
        </button>
      </div>
    </div>
  )
}











import { useState, useEffect } from 'react'

function RobustDataList({ apiEndpoint }) {
  const [data, setData] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [retryCount, setRetryCount] = useState(0)

  const fetchData = async () => {
    try {
      setLoading(true)
      setError(null)

      const response = await fetch(apiEndpoint)

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const result = await response.json()

      // Проверяем, что данные имеют ожидаемый формат
      if (!Array.isArray(result)) {
        throw new Error('Полученные данные не являются массивом')
      }

      // Фильтруем и валидируем элементы
      const validData = result.filter(item => {
        return item && typeof item === 'object' && item.id && item.name
      })

      setData(validData)
      setRetryCount(0)
    } catch (err) {
      console.error('Ошибка загрузки данных:', err)
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchData()
  }, [apiEndpoint])

  const handleRetry = () => {
    if (retryCount < 3) {
      setRetryCount(prev => prev + 1)
      fetchData()
    }
  }

  // Компонент для отображения состояния загрузки
  if (loading) {
    return (
      <div className='loading-container'>
        <div className='spinner' />
        <p>Загрузка данных...</p>
        {retryCount > 0 && <small>Попытка {retryCount + 1}</small>}
      </div>
    )
  }

  // Компонент для отображения ошибки
  if (error) {
    return (
      <div className='error-container'>
        <h3>Произошла ошибка</h3>
        <p>{error}</p>
        <div className='error-actions'>
          {retryCount < 3 ? (
            <button onClick={handleRetry}>
              Попробовать снова ({3 - retryCount} попыток осталось)
            </button>
          ) : (
            <p>Превышено максимальное количество попыток</p>
          )}
          <button onClick={() => window.location.reload()}>
            Перезагрузить страницу
          </button>
        </div>
      </div>
    )
  }

  // Компонент для пустого состояния
  if (data.length === 0) {
    return (
      <div className='empty-state'>
        <h3>Данные отсутствуют</h3>
        <p>По вашему запросу ничего не найдено</p>
        <button onClick={fetchData}>Обновить</button>
      </div>
    )
  }

  // Основной рендеринг списка с дополнительными проверками
  return (
    <div className='data-list'>
      <div className='list-header'>
        <h2>Список данных ({data.length})</h2>
        <button onClick={fetchData} className='refresh-btn'>
          Обновить
        </button>
      </div>

      <div className='list-items'>
        {data.map(item => {
          // Дополнительная проверка на уровне элемента
          if (!item || !item.id) {
            console.warn('Пропускаем некорректный элемент:', item)
            return null
          }

          return (
            <div key={item.id} className='list-item'>
              <h4>{item.name || 'Без названия'}</h4>
              <p>{item.description || 'Описание отсутствует'}</p>
              {item.image && (
                <img
                  src={item.image}
                  alt={item.name}
                  onError={e => {
                    e.target.style.display = 'none'
                  }}
                />
              )}
              <div className='item-meta'>
                <span>ID: {item.id}</span>
                {item.createdAt && (
                  <span>
                    Создано: {new Date(item.createdAt).toLocaleDateString()}
                  </span>
                )}
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}














import { useState, useMemo, useCallback, memo } from 'react'

// Мемоизированный компонент элемента списка
const ListItem = memo(({ item, onUpdate, onDelete }) => {
  console.log(`Рендеринг элемента ${item.id}`) // Для отладки

  return (
    <div className='optimized-item'>
      <h3>{item.title}</h3>
      <p>{item.description}</p>
      <div className='item-actions'>
        <button onClick={() => onUpdate(item.id, { ...item, viewed: true })}>
          Отметить как просмотренное
        </button>
        <button onClick={() => onDelete(item.id)}>Удалить</button>
      </div>
    </div>
  )
})

function OptimizedListExample({ initialData }) {
  const [items, setItems] = useState(initialData)
  const [filter, setFilter] = useState('')
  const [sortOrder, setSortOrder] = useState('asc')

  // Мемоизация отфильтрованных и отсортированных данных
  const processedItems = useMemo(() => {
    console.log('Пересчет обработанных элементов') // Для отладки

    let result = items

    if (filter) {
      result = result.filter(item =>
        item.title.toLowerCase().includes(filter.toLowerCase())
      )
    }

    result = result.sort((a, b) => {
      const comparison = a.title.localeCompare(b.title)
      return sortOrder === 'asc' ? comparison : -comparison
    })

    return result
  }, [items, filter, sortOrder])

  // Мемоизация callback-функций
  const handleItemUpdate = useCallback((itemId, updates) => {
    setItems(prevItems =>
      prevItems.map(item =>
        item.id === itemId ? { ...item, ...updates } : item
      )
    )
  }, [])

  const handleItemDelete = useCallback(itemId => {
    setItems(prevItems => prevItems.filter(item => item.id !== itemId))
  }, [])

  const handleFilterChange = useCallback(newFilter => {
    setFilter(newFilter)
  }, [])

  return (
    <div className='optimized-list-container'>
      <div className='list-controls'>
        <input
          type='text'
          placeholder='Фильтр по заголовку...'
          value={filter}
          onChange={e => handleFilterChange(e.target.value)}
        />
        <button
          onClick={() =>
            setSortOrder(prev => (prev === 'asc' ? 'desc' : 'asc'))
          }
        >
          Сортировка: {sortOrder === 'asc' ? '↑' : '↓'}
        </button>
      </div>

      <div className='items-stats'>
        Показано: {processedItems.length} из {items.length}
      </div>

      <div className='optimized-list'>
        {processedItems.map(item => (
          <ListItem
            key={item.id}
            item={item}
            onUpdate={handleItemUpdate}
            onDelete={handleItemDelete}
          />
        ))}
      </div>
    </div>
  )
}









import { useState, useEffect, useCallback, useRef } from 'react'

function PaginatedList({ apiEndpoint, pageSize = 20 }) {
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(false)
  const [hasMore, setHasMore] = useState(true)
  const [page, setPage] = useState(1)
  const [error, setError] = useState(null)
  const observerRef = useRef()

  const loadPage = useCallback(
    async (pageNumber, append = false) => {
      if (loading) return

      try {
        setLoading(true)
        setError(null)

        const response = await fetch(
          `${apiEndpoint}?page=${pageNumber}&limit=${pageSize}`
        )

        if (!response.ok) {
          throw new Error('Ошибка загрузки данных')
        }

        const data = await response.json()

        setItems(prevItems =>
          append ? [...prevItems, ...data.items] : data.items
        )

        setHasMore(data.hasMore)
        setPage(pageNumber)
      } catch (err) {
        setError(err.message)
      } finally {
        setLoading(false)
      }
    },
    [apiEndpoint, pageSize, loading]
  )

  // Загрузка первой страницы
  useEffect(() => {
    loadPage(1)
  }, [loadPage])

  // Функция для загрузки следующей страницы
  const loadMore = useCallback(() => {
    if (hasMore && !loading) {
      loadPage(page + 1, true)
    }
  }, [hasMore, loading, page, loadPage])

  // Intersection Observer для автоматической загрузки при скролле
  const lastItemRef = useCallback(
    node => {
      if (loading) return

      if (observerRef.current) {
        observerRef.current.disconnect()
      }

      observerRef.current = new IntersectionObserver(entries => {
        if (entries[0].isIntersecting && hasMore) {
          loadMore()
        }
      })

      if (node) {
        observerRef.current.observe(node)
      }
    },
    [loading, hasMore, loadMore]
  )

  return (
    <div className='paginated-list'>
      <div className='list-header'>
        <h2>Пагинированный список</h2>
        <div className='list-stats'>
          Загружено элементов: {items.length}
          {loading && <span className='loading-indicator'>⟳</span>}
        </div>
      </div>

      {error && (
        <div className='error-message'>
          <p>Ошибка: {error}</p>
          <button onClick={() => loadPage(page)}>Попробовать снова</button>
        </div>
      )}

      <div className='items-container'>
        {items.map((item, index) => {
          const isLast = index === items.length - 1

          return (
            <div
              key={item.id}
              ref={isLast ? lastItemRef : null}
              className='paginated-item'
            >
              <h3>{item.title}</h3>
              <p>{item.description}</p>
              <div className='item-metadata'>
                <span>#{item.id}</span>
                <span>{item.category}</span>
                {item.createdAt && (
                  <span>{new Date(item.createdAt).toLocaleDateString()}</span>
                )}
              </div>
            </div>
          )
        })}
      </div>

      {loading && (
        <div className='loading-more'>
          <div className='spinner' />
          <p>Загружаем еще...</p>
        </div>
      )}

      {!hasMore && items.length > 0 && (
        <div className='end-message'>
          <p>Все элементы загружены</p>
        </div>
      )}

      {!loading && !hasMore && items.length === 0 && (
        <div className='empty-state'>
          <p>Список пуст</p>
        </div>
      )}

      <div className='manual-controls'>
        <button
          onClick={loadMore}
          disabled={!hasMore || loading}
          className='load-more-btn'
        >
          {loading ? 'Загрузка...' : 'Загрузить еще'}
        </button>

        <button
          onClick={() => {
            setItems([])
            setPage(1)
            setHasMore(true)
            loadPage(1)
          }}
          className='refresh-btn'
        >
          Обновить список
        </button>
      </div>
    </div>
  )
}