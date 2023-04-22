def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title('Ввод пользовательских данных')
    def wait_user_answer(self):
        # print(" Редактирование данных каталога фильмов ".center(50, "="))
        print("Действия с фильмами:")
        print("1 - добавление фильма\n"
              "2 - каталог фильмов\n"
              "3 - просмотр определенного фильма\n"
              "4 - удаление фильма\n"
              "q - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title('добавление фильма')
    def add_user_article(self):
        dict_article = {
            'название': None,
            'жанр': None,
            'режиссер': None,
            'год выпуска': None,
            'длительность': None,
            'студия': None,
            'актеры': None
        }
        # print("добавление фильма".center(50, "="))
        for key in dict_article:
            dict_article[key] = input(f'Введите {key} фильма: ')
        # print("=" * 50)
        return dict_article

    @add_title('Список фильмов')
    def show_all_articles(self, articles):
        # print(" Список фильмов ".center(50, "="))
        for ind, article in enumerate(articles, start=1):
            print(f"{ind}. {article}")  # ind - номер элемента
        # print("=" * 50)

    @add_title('Ввод названия фильма')
    def get_user_article(self):
        user_article = input("Введите название фильма: ")
        return user_article

    @add_title('Просмотр фильма')
    def show_single_article(self, article):
        for key in article:
            print(f"{key} фильма - {article[key]}")

    @add_title('Сообщение об ошибке')
    def show_incorrect_title_error(self, user_title):
        print(f"Фильм с названием {user_title} не существует")

    @add_title('Удаление фильма')
    def remove_single_article(self, article):
        print(f"Фильм {article} - был удален")

    @add_title('Сообщение об ошибке')
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")
