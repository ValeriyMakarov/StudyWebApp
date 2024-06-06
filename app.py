from flask import Flask, render_template, request, url_for, redirect
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
    user1 = User(username='admin', email='user1@example.com',
                 password_hash='admin', is_admin=True)
    db.session.add(user1)
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
    return '<h1>fdsfs</h1>'


@app.route('/authorization', methods=['GET', 'POST'])
def authorization():
    if request.method == 'GET':
        return render_template(
            'authorization.html', title='Авторизация', css_file='styles.css'
        )
    elif request.method == 'POST':
        username = request.form.get('login')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password_hash=password).first()
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
