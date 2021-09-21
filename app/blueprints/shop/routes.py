from flask import render_template, redirect, request, session
from flask_login import login_required
from .import bp as shop
from .models import Product, Category

@shop.get('/')
def index():
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('index.html.j2', products=products, categories=categories)

@shop.get('/category/<int:id>')
def get_product_by_category(id):
    categories = Category.query.all()
    products_by_category = Product.query.filter_by(category_id=id).all()
    return render_template('index.html.j2',categories=categories, products_by_category=products_by_category)

@shop.get("/product/<int:id>")
def get_product(id):
    product = Product.query.get(id)
    return render_template('details.html.j2', product=product)

@shop.post('/add_product')
@login_required
def add_product():
    try:
        product_id = int(request.form.get('product_id'))
        quantity = request.form['quantity']
        product = Product.query.filter_by(id=product_id).first()
        if product_id and quantity and request.method == 'POST':
            product_dict = {
                product_id: {'name': product.name, 'price': product.price, 'quantity': product.quantity}
            }
            if 'cart' in session:
                print(session['cart'])
            else:
                session['cart'] = product_dict
                return redirect(request.referrer)

    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)