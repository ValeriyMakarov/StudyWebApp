from flask import Flask, render_template
from flask_login import login_user

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/library')
def library():
    return


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
