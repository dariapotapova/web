from flask import Flask, url_for, render_template, redirect
from data.db_session import global_init, create_session
from data.users import User
from data.news import News

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init("db/blogs.db")
    user = User()
    user.name = "Пользователь 1"
    user.about = "биография пользователя 1"
    user.email = "email1@email.ru"
    db_sess = create_session()
    db_sess.add(user)
    db_sess.commit()
    user = db_sess.query(User).filter(User.id == 1).first()
    news = News(title="Личная запись", content="Эта запись личная",
                is_private=True)
    user.news.append(news)
    db_sess.commit()
    app.run()


@app.route("/")
def index():
    db_sess = create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


if __name__ == '__main__':
    main()