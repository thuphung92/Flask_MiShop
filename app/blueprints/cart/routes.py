from flask import render_template, redirect, request, session, flash, url_for
from flask_login import login_required
from .import bp as cart
from app.blueprints.shop.models import Product

def merge_dict(dic1, dic2):
    if isinstance(dic1, list) and isinstance(dic2, list):
        return dic1 + dic2
    elif isinstance(dic1, dict) and isinstance(dic2, dict):
        return dict(list(dic1.items()) + list(dic2.items()))
    return False

@cart.post('/add_product')
@login_required
def add_product():
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        product = Product.query.filter_by(id=product_id).first()     
        if product_id and quantity and request.method == 'POST':
            product_dict = {
                product_id: {'name': product.name,
                            'price': product.price,
                            'quantity': quantity,
                            'img': product.img}
            }
            if 'cart' in session:
                print(session['cart'])
                if product_id in session['cart']:
                    print('This product is already in your cart')
                else:
                    session['cart'] = merge_dict(session['cart'], product_dict)
                    return redirect(request.referrer)
            else:
                session['cart'] = product_dict
                return redirect(request.referrer)
        flash("There was an error while adding the product to your cart. Please try again!")
        return redirect(request.referrer)            

@cart.get('/view_cart')
@login_required
def view_cart():
    if 'cart' in session:
        grand_total = 0
        total_quantity = 0
        for key, product in session['cart'].items():
            grand_total += (product['price'] * int(product['quantity']))
            total_quantity += int(product['quantity'])
        return render_template('cart.html.j2', total_quantity=total_quantity, grand_total=grand_total/100)
    return render_template('cart.html.j2')

@cart.post('/update_cart/<int:key>')
@login_required
def update_cart(key):
    if 'cart' not in session and len(session['cart']) <= 0:
        return redirect(url_for('shop.index'))
    if request.method == 'POST':
        quantity = request.form.get('quantity')
        try:
            session.modified = True
            for k, product in session['cart'].items():
                if int(k) == key:
                    product['quantity'] = quantity
                    flash ('Your cart has been updated')
                    redirect(url_for('cart.view_cart'))
        except Exception as e:
            print(e)
            return redirect(url_for('cart.view_cart'))
    return render_template('cart.html.j2')

@cart.get('/remove_product/<int:id>')
def remove_product(id):
    if 'cart' not in session and len(session['cart']) <=0:
        return redirect(url_for('shop.index'))
    session.modified = True
    for k, product in session['cart'].items():
        if int(k) == id:
            session['cart'].pop(k, None)
            return redirect(url_for('cart.view_cart'))
    return

@cart.get('/clear_cart')
@login_required
def clear_cart():
    if 'cart' in session:
        session.pop('cart', None)
    return redirect(url_for('shop.index'))