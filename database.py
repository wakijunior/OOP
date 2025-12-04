import psycopg2

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
    




