from flask import Flask, render_template, request, redirect, url_for
from database import get_products, get_sales, insert_products, insert_sales, available_stock, insert_stocks, get_stocks, get_users, insert_users

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
def fetch_sales():
    sales = get_sales()
    products = get_products()
    return render_template("sales.html",sales=sales, products=products)


@app.route('/make_sales', methods=['GET','POST'])
def make_sale():
    pid = request.form["pid"]
    quantity = request.form["quantity"]
    new_sale = (pid, quantity)
    check_stock = available_stock(pid)
    if check_stock < float(quantity):
        print(f"insufficient stock")
        return redirect(url_for('fetch_sales'))
    insert_sales(new_sale)
    return redirect(url_for('fetch_sales'))

@app.route('/stock')
def fetch_stocks():
    stock = get_stocks()
    products = get_products()
    return render_template("stock.html",stock=stock, products=products)

@app.route('/insert_stock', methods=['GET','POST'])
def insert_stocks():
    pid = request.form["pid"]
    quantity = request.form["quantity"]
    new_stock = (pid, quantity)
    insert_stocks(new_stock)
    return redirect(url_for("fetch_stocks"))

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/users')
def get_users():
    users = get_users()
    return render_template('users.html')

# @app.route('/insert_users')
# def insert_user(values):





   

app.run(debug=True)

