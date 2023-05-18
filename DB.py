import sqlite3

#Создать/подключиться к базе данных
connection = sqlite3.connect('SPRINGWATER.db')

#Создаем переводчик, который будет транслировать запросы БД через пайтон
sql = connection.cursor()

#Запрос создания таблицы ADMINS
# sql.execute('CREATE TABLE admin (id INTEGER, name TEXT, phone_number TEXT, gender TEXT, post TEXT);')

#Запрос создания таблицы black
# sql.execute('CREATE TABLE black (id INTEGER);')

#Запрос создания таблицы USERS
# sql.execute('CREATE TABLE users (id INTEGER, name TEXT, phone_number TEXT, loc_lat REAL, loc_long REAL, gender TEXT);')

#Запрос создания таблицы PRODUCTS
# sql.execute('CREATE TABLE products (id INTEGER, name TEXT, price REAL, info TEXT, photo TEXT, count INTEGER);')

#Запрос создания таблицы CARTS
# sql.execute('CREATE TABLE carts (user_id INTEGER, user_name TEXT, prod_id INTEGER, prod_name TEXT, count INTEGER, price REAL, total REAL);')

#Запрос создания таблицы ORDERS
# sql.execute('CREATE TABLE orders (user_id INTEGER, user_name TEXT, user_phone TEXT, user_loclat REAL, user_loclag REAL, prod_id INTEGER, prod_name TEXT, count INTEGER, price REAL, total REAL);')


def get_admins_id(user_id):#Проверяем наличие ID
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    cheker = sql.execute('SELECT id FROM admin WHERE id=?;', (user_id, ))
    if cheker.fetchone(): #Проверяем на наличие совпадений
        return True
    else:
        return False

def get_black_list(user_id):#Проверяем наличие ID
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    cheker = sql.execute('SELECT id FROM black WHERE id=?;', (user_id, ))
    if cheker.fetchone(): #Проверяем на наличие совпадений
        return True
    else:
        return False

def get_users_id(user_id):#Проверяем наличие ID
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    cheker = sql.execute('SELECT id FROM users WHERE id=?;', (user_id, ))
    if cheker.fetchone(): #Проверяем на наличие совпадений
        return True
    else:
        return False

def get_admin_info(user_id):#Проверяем наличие ID
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    cheker = sql.execute('SELECT * FROM admin WHERE id=?;', (user_id, ))
    return cheker.fetchall()

def get_info_admins():#Проверяем наличие ID
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    cheker = sql.execute('SELECT * FROM admin;')
    return cheker.fetchall()

def get_users_info(user_id):#Проверяем наличие ID
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    cheker = sql.execute('SELECT * FROM users WHERE id=?;', (user_id, ))
    return cheker.fetchall()

def get_allinfo_users():#Проверяем наличие ID
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    cheker = sql.execute('SELECT * FROM users;')
    return cheker.fetchall()

def add_black_list(id):
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Добавляем пользователя
    sql.execute('INSERT INTO black VALUES (?);', (id,))

    #Фиксируем любые изменения
    connection.commit()

def add_new_product(id, name, price, info, photo, count):
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Добавляем пользователя
    sql.execute('INSERT INTO products VALUES (?,?,?,?,?,?);', (id,name, price, info, photo, count))

    #Фиксируем любые изменения
    connection.commit()

def del_product(id):
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Добавляем пользователя
    sql.execute('DELETE FROM products WHERE id=?;', (id, ))

    #Фиксируем любые изменения
    connection.commit()

def del_id_fromblack(id):
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Добавляем пользователя
    sql.execute('DELETE FROM black WHERE id=?;', (id, ))

    #Фиксируем любые изменения
    connection.commit()

def info_allblack_list():#Проверяем наличие ID
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    cheker = sql.execute('SELECT id FROM black;')
    return cheker.fetchall()

#Добавляем администратора
def add_admins(admin_id, admin_name, phone_number, gender, post):
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Добавляем пользователя
    sql.execute('INSERT INTO admin VALUES (?,?,?,?,?);', (admin_id, admin_name, phone_number, gender, post))

    #Фиксируем любые изменения
    connection.commit()

#Добавляем пользователя
def add_users(user_id, user_name, phone_number, lati, longi, gender):
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Добавляем пользователя
    sql.execute('INSERT INTO users VALUES (?,?,?,?,?,?);', (user_id, user_name, phone_number, lati, longi, gender))

    #Фиксируем любые изменения
    connection.commit()

def delete_admin(admin_id):
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    sql.execute('DELETE FROM admin WHERE Id=?;', (admin_id,))
    connection.commit()

def delete_user(user_id):
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    sql.execute('DELETE FROM users WHERE Id=?;', (user_id,))
    connection.commit()


def get_products_ids():
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    products_ids = sql.execute('SELECT id FROM products;')
    return products_ids.fetchall()

def get_info_product(id):
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    product_info = sql.execute('SELECT * FROM products WHERE id=?;',(id, ))
    return product_info.fetchall()

def get_products_names():
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    products_ids = sql.execute('SELECT name FROM products;')
    return products_ids.fetchall()

def get_products_names_ids():
    connection = sqlite3.connect('SPRINGWATER.db')
    sql = connection.cursor()

    #Запрос для получения данных из базы данных
    products_ids = sql.execute('SELECT id, name FROM products;')
    return products_ids.fetchall()