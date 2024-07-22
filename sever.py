from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shop')
def shop():
    products = [
        {'id': 1, 'title': 'First Product', 'img': 'static/img/product/product-1.jpg'},
        {'id': 2, 'title': 'Second Product', 'img': 'static/img/product/product-2.jpg'},
        {'id': 3, 'title': 'Third Product', 'img': 'static/img/product/product-3.jpg'},
        {'id': 4, 'title': 'Fourth Product', 'img': 'static/img/product/product-4.jpg'},
        {'id': 5, 'title': 'Fifth Product', 'img': 'static/img/product/product-3.jpg'},
        {'id': 6, 'title': 'Sixth Product', 'img': 'static/img/product/product-5.jpg'},
        {'id': 8, 'title': 'Eight Product', 'img': 'static/img/product/product-6.jpg'},
        {'id': 9, 'title': 'Eight Product', 'img': 'static/img/product/product-7.jpg'},
        {'id': 10, 'title': 'Eight Product', 'img': 'static/img/product/product-8.jpg'},
        {'id': 11, 'title': 'Eight Product', 'img': 'static/img/product/product-9.jpg'},
        {'id': 12, 'title': 'Eight Product', 'img': 'static/img/product/product-10.jpg'},
        {'id': 13, 'title': 'Eight Product', 'img': 'static/img/product/product-11.jpg'},
        {'id': 14, 'title': 'Eight Product', 'img': 'static/img/product/product-12.jpg'},
    ]
    return render_template('shop.html', products=products)


@app.route('/shop-pro')
def shop_product():
    return render_template('shop-details.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


if __name__ == '__main__':
    app.run(debug=True)
