class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._level = 'user'  # Уровень доступа для обычных сотрудников

    # Геттеры для получения значений атрибутов
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = 'admin'  # Уровень доступа для администраторов
        self._user_list = []  # Список пользователей

    def add_user(self, user):
        if isinstance(user, User):
            self._user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: добавляемый объект не является пользователем.")

    def remove_user(self, user_id):
        for user in self._user_list:
            if user.get_user_id() == user_id:
                self._user_list.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Ошибка: пользователь не найден.")

    def list_users(self):
        if self._user_list:
            print("Список пользователей:")
            for user in self._user_list:
                print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_level()}")
        else:
            print("Список пользователей пуст.")


# Пример использования классов
if __name__ == "__main__":
    admin = Admin(1, "Андрей")

    # Создание пяти пользователей
    user1 = User(2, "Ольга")
    user2 = User(3, "Михаил")
    user3 = User(4, "Олег")
    user4 = User(5, "Юля")
    user5 = User(6, "Виктор")

    # Добавление пользователей администратором
    admin.add_user(user1)
    admin.add_user(user2)
    admin.add_user(user3)
    admin.add_user(user4)
    admin.add_user(user5)

    # Вывод списка пользователей
    admin.list_users()

    # Удаление одного пользователя
    admin.remove_user(3)

    # Вывод обновленного списка пользователей
    admin.list_users()
