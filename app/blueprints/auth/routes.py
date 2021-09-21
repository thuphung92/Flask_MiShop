from flask import render_template, request, redirect, url_for,flash
from .forms import RegisterForm, LoginForm
from.models import User
from flask_login import login_user, logout_user, current_user, login_required
from . import bp as auth

@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            new_user_data={
                "first_name": form.first_name.data.title(),
                "last_name": form.last_name.data.title(),
                "email": form.email.data.lower(),
                "password": form.password.data
            }
            new_user_object = User()
            new_user_object.from_dict(new_user_data)
        except:
            flash('There was an unexpected error', 'danger')
            return render_template('auth/register.html.j2',form=form)
        # Give the user some feedback that says registered successfully 
        flash('Registered Successfully','success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html.j2',form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email=form.email.data.lower()
        password=form.password.data
        user = User.query.filter_by(email=email).first()
        if user is not None and user.check_hashed_password(password):
            login_user(user)
            flash('Logged in Successfully', 'success')
            return redirect(url_for('shop.index'))
        else:
            flash('Invalid Email/Password', 'danger')
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html.j2', form=form)


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    if current_user is not None:
        logout_user()
        flash("You've been logged out",'warning')
        return redirect(url_for('shop.index')) # redirect to home page
