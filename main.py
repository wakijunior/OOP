from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import get_products, get_sales, insert_products, insert_sales, available_stock, insert_stocks, get_stocks, get_users, insert_user, check_user_exists, insert_user, profit_per_day, profit_per_product, sales_per_day, sales_per_product  
from flask_bcrypt import Bcrypt
from functools import wraps

# creating a app object / instance
app = Flask(__name__)

# creating a brypt object / instance
bcrypt = Bcrypt(app)

#secret key - signs session data
app.secret_key ='mgknkognjghjkkjri4683749'

@app.route("/")
def home():
    return render_template("index.html")

def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected

@app.route('/products')
@login_required
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
    flash("product added succesfully", 'success')
    return redirect(url_for('fetch_products'))
   
    

@app.route('/sales')
@login_required
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
        flash("insufficient stock", 'danger')
        return redirect(url_for('fetch_sales'))
    insert_sales(new_sale)
    flash("sale completed successfully",'success')
    return redirect(url_for('fetch_sales'))

@app.route('/stock')
@login_required
def fetch_stocks():
    stock = get_stocks()
    products = get_products()
    return render_template("stock.html",stock=stock, products=products)

@app.route('/insert_stock', methods=['GET','POST'])
def add_stock():
    pid = request.form["pid"]
    quantity = request.form["quantity"]
    new_stock = (pid, quantity)
    insert_stocks(new_stock)
    return redirect(url_for("fetch_stocks"))

@app.route('/dashboard')
@login_required
def dashboard():
    product_sales = sales_per_product()
    daily_sales = sales_per_day()
    product_profit = profit_per_product()
    daily_profit = profit_per_day()

    product_names = [i[0] for i in product_sales]
    sales_per_p = [float(i[1]) for i in product_sales]
    profit_per_p = [float(i[1]) for i in product_profit]

    date = [str(i[0]) for i in daily_profit]
    sales_per_d = [float(i[0]) for i in daily_sales]
    profit_per_d = [float(i[1]) for i in daily_profit]

    return render_template("dashboard.html", product_names=product_names, 
                           sales_per_p=sales_per_p,profit_per_p=profit_per_p,date=date,
                           sales_per_d=sales_per_d,profit_per_d=profit_per_d)


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['name']

        registered_user = check_user_exists(email)
        if not registered_user:
            flash("User with this email doesnt exist, register",'danger')
        else:
            if bcrypt.check_password_hash(registered_user[-1],password):
                flash("Login successful", 'success')
                session['email'] = email
                return redirect(url_for('dashboard'))
            else:
                flash("Password incorrect",'danger')
    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone']
        password = request.form['password']
        existing_user = check_user_exists(email)
        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = (full_name, email, phone_number, hashed_password)
            insert_user(new_user)
            flash('user registered successifully')
            return redirect(url_for('login'))
        else:
            flash("user with this email already exists, login instead", 'danger')
    return render_template("register.html")
    
@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))




    





   

app.run(debug=True)

