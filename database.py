import psycopg2 
from datetime import datetime, date, timezone

conn = psycopg2.connect(host='localhost',port='5432', user='postgres', password='0911', dbname='myduka')

cur = conn.cursor()

def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products
products = get_products()
print(products)

def insert_products(values):
    cur.execute(f"insert into products(name, buying_price, selling_price) values{values}")
    conn.commit()
values = ('thermal_printer', 5500, 8000)
product1 = insert_products(values)

print(products)

def insert_sales(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s,%s)",values)
    conn.commit()
prod = (1, 2)
sale = insert_sales(values)
print(sale)

    




