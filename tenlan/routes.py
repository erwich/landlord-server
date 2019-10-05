from flask import render_template, url_for, flash, redirect
from site_prelim import app
from site_prelim.forms import register, login
from site_prelim.models import user, post
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
def home():
    return render_template('home.html', title='jhome')

@app.route("/")
def about():
    return render_template('landlords.html', title='landlords')
    
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = user(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('account created, login', 'success')
        return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home))
    form = LoginForm()
    if form.validate_on_submit():
        user = user.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('unsuccessful', 'danger')
    return render_template('login.html', title='login', form=form)
    

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
	return render_template('account.html', title='account')
