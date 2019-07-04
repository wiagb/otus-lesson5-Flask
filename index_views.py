from flask import Flask, request, render_template
from werkzeug.exceptions import NotFound
from products_views import product_app
from likedatabase import dogs_feed, cats_feed, hamsters_feed, category

app = Flask(__name__)
app.register_blueprint(product_app, url_prefix='/products/')


@app.route('/')
def index_page():
    if request.method == 'GET':
        products_list = (dogs_feed, cats_feed, hamsters_feed)
        response = render_template('index.html', category=category, products_list=products_list)
        return response


@app.route('/<string:subcat>/')
def category_page(subcat=None):
    if request.method == 'GET':
        if subcat == 'Корма для собак':
            products_list = (dogs_feed, ([]))
        elif subcat == 'Корма для кошек':
            products_list = (cats_feed, ([]))
        elif subcat == 'Корма для хомячков':
            products_list = (hamsters_feed, ([]))
        elif subcat == 'Все':
            products_list = (dogs_feed, cats_feed, hamsters_feed)
        else:
            raise NotFound

        response = render_template('index.html', category=category, products_list=products_list)
        return response


app.run('localhost', 8080, debug=True)
