function UserProfile({ user }) {
	const renderUserActions = () => {
		if (user.role === 'admin') {
			return (
				<div className='admin-panel'>
					<button>Управление пользователями</button>
					<button>Системные настройки</button>
					<button>Просмотр логов</button>
				</div>
			)
		}

		if (user.role === 'moderator') {
			return (
				<div className='moderator-panel'>
					<button>Модерация контента</button>
					<button>Управление комментариями</button>
				</div>
			)
		}

		return (
			<div className='user-panel'>
				<button>Редактировать профиль</button>
				<button>Настройки уведомлений</button>
			</div>
		)
	}

	return (
		<div className='profile'>
			<h2>{user.name}</h2>
			<p>Роль: {user.role}</p>
			{renderUserActions()}
		</div>
	)
}
