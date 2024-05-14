class User:
    def __init__(self, user_id, name, access_level='user'):
        # Инициализация объекта User
        # user_id: уникальный идентификатор пользователя
        # name: имя пользователя
        # access_level: уровень доступа пользователя, по умолчанию 'user'
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        # Возвращает уникальный идентификатор пользователя
        return self.__user_id

    def get_name(self):
        # Возвращает имя пользователя
        return self.__name

    def get_access_level(self):
        # Возвращает уровень доступа пользователя
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        # Инициализация объекта Admin, унаследованного от User
        # admin имеет уровень доступа 'admin' и список пользователей
        super().__init__(user_id, name, access_level='admin')
        self.__users = []

    def add_user(self, user_name):
        # Добавляет пользователя в список пользователей
        self.__users.append(user_name)

    def remove_user(self, user_name):
        # Удаляет пользователя из списка пользователей
        self.__users.remove(user_name)

    def get_users(self):
        # Возвращает список пользователей, добавленных администратором
        return self.__users


# Создание пользователей
user1 = User(1, "Ольга")  # Создание пользователя с ID 1 и именем Ольга
user2 = User(2, "Владимир")    # Создание пользователя с ID 2 и именем Владимир
admin = Admin(3, "Николай")  # Создание администратора с ID 3 и именем Николай


# Добавление пользователей администратором
admin.add_user(user1)     # Администратор добавляет пользователя Ольга
admin.add_user(user2)     # Администратор добавляет пользователя Владимир

# Вывод пользователей
print("Список пользователей, добавленных администратором:")
for user in admin.get_users():
    # Вывод информации о пользователях, добавленных администратором
    print("ID:", user.get_user_id(), "Имя:", user.get_name(), "Уровень доступа:", user.get_access_level())

# Удаление пользователя администратором
admin.remove_user(user1)  # Администратор удаляет пользователя Ольга

# Вывод пользователей после удаления
print("\nСписок пользователей, после удаления:")
for user in admin.get_users():
    # Вывод информации о пользователях после удаления одного из них
    print("ID:", user.get_user_id(), "Имя:", user.get_name(), "Уровень доступа:", user.get_access_level())
