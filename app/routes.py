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

@app.route('/products')
def products():
    user = {'username': 'Guest'}
    # Придуманные данные: продукт, цена, наличие
    products = [
        {'product': 'Laptop', 'price': 1200, 'in_stock': True},
        {'product': 'Smartphone', 'price': 800, 'in_stock': True},
        {'product': 'Headphones', 'price': 150, 'in_stock': False},
        {'product': 'Keyboard', 'price': 90, 'in_stock': True},
        {'product': 'Mouse', 'price': 45, 'in_stock': True},
        {'product': 'Monitor', 'price': 450, 'in_stock': False}
    ]
    price_threshold = 500  # пороговая цена
    return render_template('products.html',
                           title='Products',
                           site_name='My Site',
                           year=2026,
                           user=user,
                           products=products,
                           price_threshold=price_threshold)
