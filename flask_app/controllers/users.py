from flask_app import app
from flask import render_template,redirect,request,flash, session
from flask_app.models.user import User
from flask_app.models.product import Product
from flask_app.models.reserve import Reserve
from flask_app.models.review import Review
from flask_app.static import *

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reserve")
def reserve():
    return render_template("book.html", product_list = Product.get_all_products())

@app.route("/reservenow", methods=["POST"])
def newreserve():
    Reserve.new_reserve(request.form)
    return redirect("/reserve")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/dashboard")
def home_page():
    if "user_id" not in session:
        return redirect("/")
    return render_template("dashboard.html", all_apps = Reserve.all_reserves())

@app.route('/loggedin', methods=["POST"])
def login():
    if User.validate_login(request.form):
        data = {
            "email": request.form['email'],
            "password": request.form['password']
        }
        user = User.user_email(data)
        session['user_id'] = user.id
        return redirect('/dashboard')
    else:
        return redirect('/login')

@app.route('/newproduct')
def new_product():
    if "user_id" not in session:
        return redirect("/")
    return render_template('/products.html', products_list=Product.get_all_products())

@app.route('/addproduct', methods=["POST"])
def product():
    if "user_id" not in session:
        return redirect("/")
    Product.create_product(request.form)
    return redirect('/dashboard')

@app.route('/logout') 
def index_two():
    session.clear()
    return redirect('/')


@app.route('/reviews')
def load_reviews():
    return render_template('review.html',all_revs = Review.all_reviews())

@app.route('/newreview')
def new_review():
    return render_template('newreview.html')

@app.route('/createreview', methods=["POST"])
def review_new():
    Review.create_review(request.form)
    return redirect('/reviews')


@app.route('/deleteres/<int:res_id>')
def res_deleted(res_id):
    if "user_id" not in session:
        return render_template("index.html")
    data = {"appoitment_id" : res_id} 
    Reserve.delete_reserve(data)   
    return redirect('/dashboard')


@app.route('/deleteprod/<int:prod_id>')
def prod_deleted(prod_id):
    if "user_id" not in session:
        return render_template("index.html")
    data = {"product_id" : prod_id} 
    Product.delete_product(data)   
    return redirect('/dashboard')