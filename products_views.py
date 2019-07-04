from werkzeug.exceptions import NotFound
from flask import Blueprint, render_template

from likedatabase import dogs_feed, cats_feed, hamsters_feed, category

product_app = Blueprint('product_app', __name__)


@product_app.route('/<int:prod_id>/')
def product_show(prod_id):
    response = 'Извините, данный товар не найден'
    # Поиск во всех продуктах по id
    products_list = (dogs_feed, cats_feed, hamsters_feed)
    for products in products_list:
        for item in products:
            if item[3] == prod_id:
                response = render_template('product.html', prod=item, category=category)
    return response
