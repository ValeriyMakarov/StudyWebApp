from flask import Flask, render_template
from flask_login import login_user
from flask_sqlalchemy import SQLAlchemy

from models import Subject, Article, Exercise, User
from __init__ import create_app, db

app = create_app()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/library')
def library():

    # Создаем объекты моделей данных
    subject1 = Subject(name='Subject 1')
    article1 = Article(name='Article 1', subject=subject1)
    exercise1 = Exercise(article=article1, text='Exercise 1')
    user1 = User(username='user1', email='user1@example.com',
                 password_hash='hashed_password', is_admin=True)

    # Добавляем объекты в сессию
    db.session.add(subject1)
    db.session.add(article1)
    db.session.add(exercise1)
    db.session.add(user1)

    # Зафиксируем изменения
    db.session.commit()
    return 'good'


@app.route('/library/<subject>')
def library_subject(subject: str):
    return


@app.route('/library/<subject>/<int:subject_id>')
def library_item(subject: str, subject_id: int):
    return


@app.route('/calculators')
def calculators():
    return


@app.route('/calculators/<int:calc_id>')
def calculator_item(calc_id: int):
    return


@app.route('/authorization')
def authorization():
    d = {'a':'as', 'b':'asd', 'f':'sdf'}
    return render_template('test.html', title = 'adsd', list = d)


if __name__ == '__main__':
    app.run(debug=True)
