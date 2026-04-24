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

# ========== ЗАДАНИЕ 3: НОВОСТНОЙ САЙТ ==========
@app.route('/news')
def news_home():
    """Главная страница новостного раздела"""
    user = {'username': 'Ksu'}
    return render_template('news/index.html',
                           title='Новости',
                           site_name='Мой сайт',
                           year=2026,
                           user=user)

@app.route('/news/list')
def news_list():
    """Список новостей"""
    user = {'username': 'Ksu'}
    # Данные: заголовок, просмотры
    news_items = [
        {'title': 'Запущен новый спутник', 'views': 1500},
        {'title': 'Открытие кафе в центре', 'views': 870},
        {'title': 'Выставка современного искусства', 'views': 2300},
        {'title': 'Рекордный урожай яблок', 'views': 420},
        {'title': 'Фестиваль уличной еды', 'views': 1200},
    ]
    return render_template('news/news.html',
                           title='Список новостей',
                           site_name='Мой сайт',
                           year=2026,
                           user=user,
                           news=news_items)

# ========== ЗАДАНИЕ 4: МИНИ-БЛОГ ==========
# Данные статей (обычно хранятся в БД, но для примера – в коде)
articles = {
    1: {'title': 'Первый пост', 'content': 'Это текст первого поста. Привет, мир!'},
    2: {'title': 'Flask – это просто', 'content': 'Flask позволяет быстро создавать веб-приложения на Python.'},
    3: {'title': 'Шаблоны Jinja2', 'content': 'Jinja2 – мощный шаблонизатор с поддержкой условий и циклов.'},
    4: {'title': 'Маршрутизация', 'content': 'С помощью декоратора @app.route можно связывать URL с функциями.'},
}

@app.route('/posts')
def posts_list():
    """Список всех статей"""
    user = {'username': 'Ksu'}
    # Преобразуем словарь в список для удобства в шаблоне
    posts = [{'id': id, 'title': data['title']} for id, data in articles.items()]
    return render_template('posts.html',
                           title='Блог',
                           site_name='Мой сайт',
                           year=2026,
                           user=user,
                           posts=posts)

@app.route('/posts/<int:id>')
def post_detail(id):
    """Страница отдельной статьи"""
    user = {'username': 'Ksu'}
    post = articles.get(id)
    if not post:
        return "Статья не найдена", 404
    return render_template('post_detail.html',
                           title=post['title'],
                           site_name='Мой сайт',
                           year=2026,
                           user=user,
                           post=post,
                           post_id=id)

# ========== ЗАДАНИЕ 5: СПИСОК РЕПОЗИТОРИЕВ ==========
@app.route('/repos')
def repos_list():
    user = {'username': 'Ksu'}
    repos = [
        {'name': 'flask', 'language': 'Python', 'stars': 65000},
        {'name': 'react', 'language': 'JavaScript', 'stars': 210000},
        {'name': 'tensorflow', 'language': 'Python', 'stars': 180000},
        {'name': 'bootstrap', 'language': 'CSS', 'stars': 164000},
        {'name': 'my_small_lib', 'language': 'Python', 'stars': 45},
        {'name': 'awesome_project', 'language': 'Go', 'stars': 320}
    ]
    stars_threshold = 100  # порог популярности
    total_repos = len(repos)
    return render_template('repos.html',
                           title='Репозитории',
                           site_name='Мой сайт',
                           year=2026,
                           user=user,
                           repos=repos,
                           stars_threshold=stars_threshold,
                           total_repos=total_repos)
