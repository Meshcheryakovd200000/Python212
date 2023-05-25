from flask import Flask, render_template, url_for, request, flash, session, redirect, g
import os
import sqlite3

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = '7f3268221fd5e708a6c28bd1f81bff721cf53c3b'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fgdf4654fgdfgdfg789798hnjmghmh464dfg'
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))  # app.root_path - доступ к


# корневой папке p43python_flask

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()  # сохраняем все данные во внутри БД
    db.close()  # закрываем!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Обратная связь", "url": "contact"},
    {"name": "Серверы HP ML350P", "url": "hp"},
    {"name": "IBM", "url": "ibm"},
]


def get_db():
    if not hasattr(g, 'link_db'):  # hasattr -проверка наличия атрибута "g" в глобальных настройках - "global"
        g.link_db = connect_db()
    return g.link_db  # если нет соединения то создаем соединение


@app.route("/index")  # decorator
@app.route("/")  # decorator, над функцией index()
def index():
    db = get_db()
    # dbase = FDataBase(db)
    # print(url_for('index'))
    return render_template('index.html', title="Главная", menu=menu)


@app.route("/about")  # decorator, route -это маршруты по которым сможем переходить
def about():
    print(url_for('about'))  # показывает путь срабатывания функции about()
    return render_template('about.html', title="О нас", menu=menu)


@app.route("/profile/<username>")  # decorator
def profile(username):
    return f"Пользователь: {username}"


@app.route("/contact", methods=["POST", "GET"])  # метод GET отрабатывает когда мы зашли на саму страницу
# а метод POST отрабатывает когда мы нажали на кнопку отправить
def contact():
    if request.method == "POST":  # метод отправки данных
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено успешно', category='success')  # если длина в имени пользователя больше 2
        else:
            flash('Ошибка отправки', category='error')
        # print(request.form)
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message']
        # }
        # return render_template('contact.html', title="Обратная связь", menu=menu, **context)
    return render_template('contact.html', title="Обратная связь", menu=menu)


@app.errorhandler(404)  # если страница не существует
def page_not_found(error):
    # db = get_db()
    # dbase = FDataBase(db)
    return render_template('page404.html', title="Страница не найдена", menu=menu)  # , 404


@app.route('/login', methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))  # пользователь залогинен и
        # перенаправляем его на страницу profile
    elif request.method == 'POST' and request.form['username'] == 'dima' and request.form['psw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title="Авторизация", menu=menu)


@app.teardown_appcontext  # закрытие БД
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/hp")  # decorator, route -это маршруты по которым сможем переходить
def hp():
    print(url_for('hp'))  # показывает путь срабатывания функции hp()
    return render_template('hp.html', title="HP PROLIANT ML350P", menu=menu)


@app.route("/ibm")  # decorator, route -это маршруты по которым сможем переходить
def ibm():
    print(url_for('ibm'))
    return render_template('ibm.html', title="IBM servers", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)  # включили режим отладки
