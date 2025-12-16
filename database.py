import psycopg2
from datetime import datetime

conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='0911',dbname='myduka')

cur = conn.cursor()


def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

products = get_products()
print(products)


def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()

   
# product1 = ('iphone',100000,120000)
# product2 = ('hp',50000,60000)
# insert_products(product1)
# insert_products(product2)


def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales


#method 1 - f-string
def insert_sales(values):
    cur.execute(f"insert into sales(pid,quantity)values{values}")
    conn.commit()


#method 2 - using placeholders
def insert_sales_2(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",values)
    conn.commit()

def available_stock(pid):
    cur.execute(f"select sum(stock_quantity)from stock where pid = {pid}")
    total_stock = cur.fetchone()[0] or 0

    cur.execute(f"select sum(quantity)from sales where pid = {pid}")
    total_sales = cur.fetchone()[0] or 0

    return total_stock - total_sales

def get_stocks():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock

def insert_stocks(values):
    cur.execute(f"insert into stock(pid,stock_quantity)values{values}")
    conn.commit()

#fetching users
def get_users():
    cur.execute("select * from users")
    users = cur.fetchall()
    return users

#adding users
def insert_users(values):
    cur.execute("insert into users(full_name, email, phone_number,password) values(%s,%s,%s,%s)",values)
    conn.commit()


#getting sales per product
def get_sales_per_product():
    cur.execute("select pid,sum(quantity) as products_sold FROM sales group by pid")
    sales_per_product =cur.fetchall()
    return sales_per_product

#getting number of sales per day
def get_daily_sales():
    cur.execute("select pid, sum(quantity) as sales_made from sales group by pid")
    sale = cur.fetchall()
    return sale

