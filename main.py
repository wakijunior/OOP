from flask import Flask, render_template, request, redirect, url_for
from database import get_products, get_sales, insert_products

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/products')
def fetch_products():
    products = get_products()
    return render_template("products.html", products = products)



@app.route('/addproducts', methods=['GET','POST'])
def add_products():
    product_name = request.form["product_name"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]
    new_product = (product_name,buying_price,selling_price)
    insert_products(new_product)
    return redirect(url_for('fetch_products'))
   
    

@app.route('/sales')
def make_sale():
    pid = request.form["pid"]
    quantity = request.form["quantity"]
    created_at = request.form["created_at"]
    new_sale = (pid, quantity, created_at)
    make_sale(new_sale)
    return redirect(url_for('/sales'))

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


   

app.run(debug=True)

