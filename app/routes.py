'''from app import app

@app.route('/')
@app.route('/page')
def index ():
    return "You are so cool"'''

'''Klass work 10-03-26'''
from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ksu'}
    posts = [
        {
            'author': {'username': 'Alice'},
            'body': 'Hello!'
        },
        {
            'author': {'username': 'Mike'},
            'body': 'Hi, number 2!'
        }
    ]
    students = [
        {"name":"Vasya", "age":20, "grade":4},
        {"name":"Ivan", "age":19, "grade":5},
        {"name":"Dima", "age":19, "grade":3}
    ]
    return render_template('index.html', title='Home. Практика по фласк', user=user, students = students)
