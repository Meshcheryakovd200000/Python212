import pickle
import os.path


class Article:
    def __init__(self, title, genre, director, year_of_issue, duration, studio, actors):
        self.title = title  # название
        self.genre = genre  # жанр
        self.director = director  # режиссер
        self.year_of_issue = year_of_issue  # год выпуска
        self.duration = duration  # длительность
        self.studio = studio  # студия
        self.actors = actors  # актеры

    def __str__(self):
        return f"Название фильма: {self.title} (Жанр: {self.genre}) (Год выпуска: {self.year_of_issue})"


class ArticleModel:
    def __init__(self):
        self.db_name = "db.txt"
        # self.articles = {}  # {} переменная в которой будут храниться данные
        self.articles = self.load_data()  # {} переменная в которой будут храниться данные

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            'название': article.title,
            'жанр': article.genre,
            'режиссер': article.director,
            'год выпуска': article.year_of_issue,
            'длительность': article.duration,
            'студия': article.studio,
            'актера': article.actors
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.articles, f)
