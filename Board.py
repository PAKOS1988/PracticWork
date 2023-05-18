from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from DB import *
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types.web_app_data import WebAppData


# Панель администратора
def administration():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    btn_task_editproducts = KeyboardButton('Редактировать товары')
    btn_task_editadmins = KeyboardButton('Права администратора')
    btn_task_orders = KeyboardButton('Просмотреть заказы')
    btn_black = KeyboardButton('Черный список')

    kb.add(btn_task_editproducts, btn_task_orders, btn_black, btn_task_editadmins)
    return kb

def admin_edit_products():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    btn_add_product = KeyboardButton('Добавить товар')
    # btn_edit_product = KeyboardButton('Редактировать товар')
    btn_delete_product = KeyboardButton('Удалить товар')
    btn_back = KeyboardButton("Вернуться в главное меню🔙")
    kb.add(btn_add_product, btn_back, btn_delete_product)
    return kb

def admin_orders_view():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
    btn_all_orders_view = KeyboardButton('Все заказы по очереди📋')
    btn_clientId_orders_view = KeyboardButton('Все заказы клиента по ID')
    btn_delId_orders_order = KeyboardButton('Удалить заказ клиента по ID')
    btn_back = KeyboardButton("Вернуться в главное меню🔙")
    kb.add(btn_all_orders_view, btn_clientId_orders_view, btn_delId_orders_order, btn_back)
    return kb

def admin_list():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
    btn_add_admin = KeyboardButton('Добавить администратора')
    btn_del_admin = KeyboardButton('Удалить администратора')

    btn_back = KeyboardButton("Вернуться в главное меню🔙")
    kb.add(btn_add_admin, btn_del_admin , btn_back)
    return kb

def black_list_command():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
    btn_add_black = KeyboardButton('Добавить в ч/с')
    btn_del_black = KeyboardButton('Удалить с ч/с')
    btn_back = KeyboardButton("Вернуться в главное меню🔙")
    kb.add(btn_add_black, btn_del_black, btn_back)
    return kb

# Панель клиента
def client():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    btn_task_products = KeyboardButton('Приступить к заказу')
    btn_task_carts = KeyboardButton('Корзина')
    btn_task_editregistration = KeyboardButton('Настройки данных')
    btn_task_contactsus = KeyboardButton('Наши контакты')

    kb.add(btn_task_products, btn_task_carts, btn_task_editregistration, btn_task_contactsus)
    return kb

#панель регистрации
def newclient():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    btn_task_contactsus = KeyboardButton('Наши контакты')
    btn_task_registration = KeyboardButton('Зарегистрироваться')
    btn_task_oferta = KeyboardButton('ОФЕРТА')
    kb.add(btn_task_registration, btn_task_oferta, btn_task_contactsus)
    return kb

def newclient2():
    kbi = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton('Оферта', callback_data='oferta')
    btn2 = InlineKeyboardButton('Наши контакты', callback_data='aboutUs')
    kbi.add(btn1, btn2)


    return kbi

#Кнопка выбора имени
def get_name_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton('Взять из аккаунта')
    kb.add(btn)
    return kb

# Кнопка для отправки номера
def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton('Поделиться контактом', request_contact=True)
    kb.add(btn)
    return kb

# Кнопка для отправки локации
def location_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton('Поделиться локацией', request_location=True)
    kb.add(btn)
    return kb
# Кнопка для отправки пола
def gender_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton('Мужской')
    btn2 = KeyboardButton('Женский')
    kb.add(btn1,btn2)
    return kb

def del_product_kb():
    kb=InlineKeyboardMarkup(row_width=2)
    btn1=InlineKeyboardButton('Удалить', callback_data='delete')

    kb.add(btn1)
    return kb


def add_product_to_cart():
    kb = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton('+', callback_data='increase')
    btn2 = InlineKeyboardButton('-', callback_data='decrease')
    btn3 = InlineKeyboardButton('Добавить в корзину', callback_data='add_to_cart')
    kb.add(btn1, btn2, btn3)
    return kb

def products_board_for_del():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    back = KeyboardButton('Вернуться в главное меню🔙')
    all_products = get_products_names_ids()
    #Генерируем список кнопок с названиями
    for i in all_products:
        btn = str(i[0])+'-'+i[1]
        kb.insert(btn)
    # btns = [KeyboardButton(i[0:2]) for i in all_products]
    # print(btns)
    # kb.add(*btns)
    kb.insert(back)
    return kb


def open_site_kb():
    kbi = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Open site', web_app=WebAppInfo(url='https://pakos1988.github.io/PracticWork/'))
    kbi.add(btn1)

    return kbi
