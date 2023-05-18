import DB
from CREATEBOT import *
from aiogram import executor
from States import *
from Board import *
from DB import *
from aiogram import types
# import re
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
# from geopy import Nominatim

#Обработка команды /start
@dp.message_handler(commands=['start'], state='*')
async def start_cmd(message):
    start_lable=f'{message.from_user.first_name}🫲🤖🫱\n'
    user_id=message.from_user.id
    black = get_black_list(user_id)
    admins = get_admins_id(user_id)
    users = get_users_id(user_id)

    await bot.delete_message(message.from_user.id, message_id=message.message_id)
    if black:
        await bot.send_message(message.from_user.id, 'Вы в черном списке')
        connection.close()
    elif admins:
        admin_info = get_admin_info(user_id)
        await message.answer(f'{admin_info[0][1]}\nГлавное меню', reply_markup = administration())
        await Admin.change_task.set()
    elif users:
        user_info = get_users_info(user_id)
        await message.answer(f'{(user_info[0][1])}\nГлавное меню', reply_markup = client())
        await User.change_task.set()
    else:
        await message.answer(f'{start_lable}\nГлавное меню', reply_markup = newclient())
        await New_user.change_task.set()

@dp.message_handler(state=New_user.change_task)
async def get_name(message, state=New_user.change_task):
    if message.text == 'Зарегистрироваться':
        reg_lable = f'Представтесь!\nВведите Ваше имя или выберите поделиться👇:'
        await bot.delete_message(message.from_user.id, message_id=message.message_id -1)
        await bot.delete_message(message.from_user.id, message_id=message.message_id)
        await message.answer(reg_lable, reply_markup=get_name_kb())
        await Registration.get_name.set()
    elif message.text == 'ОФЕРТА':
        oferta = 'Тут пропечатаны все ваши условия/акции/обязанности'
        await bot.delete_message(message.from_user.id, message_id=message.message_id - 1)
        await bot.delete_message(message.from_user.id, message_id=message.message_id)
        await message.answer(oferta, reply_markup=newclient())
        await New_user.change_task.set()
    elif message.text == 'Наши контакты':

        aboutUs = 'Офис: (хх)ххх-хх-хх\nCall-Center: (xx)xxx-xx-xx\nTG-GROUP: xxxxxxx@tg'
        await bot.delete_message(message.from_user.id, message_id=message.message_id - 1)
        await bot.delete_message(message.from_user.id, message_id=message.message_id)
        await message.answer(aboutUs, reply_markup=newclient())
        await New_user.change_task.set()
    else:
        await bot.delete_message(message.from_user.id, message_id=message.message_id - 1)
        await bot.delete_message(message.from_user.id, message_id=message.message_id)
        await message.answer('Ой, что-то пошло не так, повторите команду!', reply_markup=newclient())
        await New_user.change_task.set()

@dp.message_handler(state=Admin.change_task)
async def get_name(message, state=Admin.change_task):
    if message.text == 'Редактировать товары':
        await bot.delete_message(message.from_user.id, message_id=message.message_id -1)
        await bot.delete_message(message.from_user.id, message_id=message.message_id)
        await message.answer('Выберите нужную операцию:', reply_markup=admin_edit_products())
        await state.finish()
        await Admin_edit_change.change_task.set()
    elif message.text == 'Просмотреть заказы':
        await bot.delete_message(message.from_user.id, message_id=message.message_id - 1)
        await bot.delete_message(message.from_user.id, message_id=message.message_id)
        await message.answer('Выберите нужную операцию:', reply_markup=admin_orders_view())
        await state.finish()
        await Admin_edit_change.change_task.set()
    elif message.text == 'Права администратора':
        await bot.delete_message(message.from_user.id, message_id=message.message_id - 1)
        await bot.delete_message(message.from_user.id, message_id=message.message_id)
        await message.answer('Выберите нужную операцию:', reply_markup=admin_list())
        await state.finish()
        await Admin_edit_change.change_task.set()
    elif message.text == 'Черный список':
        await bot.delete_message(message.from_user.id, message_id=message.message_id - 1)
        await bot.delete_message(message.from_user.id, message_id=message.message_id)
        info_black_list = info_allblack_list()
        print(info_black_list)
        result = 'Черный список:\n'
        for i in info_black_list:
            result += f'ID = {i[0]}\n'
        await bot.send_message(message.from_user.id, text=result)
        await message.answer('Выберите команду:', reply_markup=black_list_command())
        await state.finish()
        await Admin_edit_change.change_task.set()
    else:
        await bot.delete_message(message.from_user.id, message_id=message.message_id - 1)
        await bot.delete_message(message.from_user.id, message_id=message.message_id)
        await message.answer('Ой, что-то пошло не так, повторите команду!', reply_markup=administration())
        await Admin.change_task.set()

@dp.message_handler(state=Admin_edit_change.change_task)
async def get_name(message, state=Admin_edit_change.change_task):
    if message.text == 'Добавить товар':
        await message.answer('Введите наименование товара', reply_markup=ReplyKeyboardRemove())
        await Add_product.name_new_product.set()
    elif message.text == 'Редактировать товар':
        pass
    elif message.text == 'Удалить товар':
        await message.answer ('Выберите товар для удаления:', reply_markup = products_board_for_del())
        await delete_product_state.status_delete.set()
    elif message.text == 'Все заказы по очереди📋':
        pass
    elif message.text == 'Все заказы клиента по ID':
        pass
    elif message.text == 'Удалить заказ клиента по ID':

        pass
    elif message.text == 'Вернуться в главное меню🔙':
        await state.finish()
        await start_cmd(message)
    elif message.text == 'Добавить администратора':
        await message.answer('Введите имя новго администратора:', reply_markup=ReplyKeyboardRemove())
        await state.finish()
        await RegistrationAdmins.get_name_admins.set()
    elif message.text == 'Удалить администратора':
        info_admins = get_info_admins()
        print(info_admins)
        admins_list = 'Список администраторов:\n'
        for i in info_admins:
            admins_list += f'ID = {i[0]}\n   Имя: {i[1]}\n   Должность {i[4]}\n'
        await bot.send_message(message.from_user.id, text=admins_list)
        await message.answer('Введите ID администратора, которого хотите удалить:', reply_markup=ReplyKeyboardRemove())
        await Admin_delete_admin.del_admin.set()
    elif message.text == 'Добавить в ч/с':
        await message.answer('Введите ID:', reply_markup=ReplyKeyboardRemove())
        await state.finish()
        await black.add_id.set()
    elif message.text == 'Удалить с ч/с':
        await message.answer('Введите ID:', reply_markup=ReplyKeyboardRemove())
        await black.del_id.set()
    else:
        await bot.delete_message(message.from_user.id, message_id=message.message_id - 1)
        await bot.delete_message(message.from_user.id, message_id=message.message_id)
        await message.answer('Ой, что-то пошло не так, повторите команду!', reply_markup=administration())
        await Admin.change_task.set()

@dp.message_handler(state=delete_product_state.status_delete)
async def status_delete(message, state=delete_product_state.status_delete):

    for id in message.text.split('-'):
        if id.isdigit():
            await state.update_data(id_prod_del=int(id))
    s = await state.get_data()
    id_prod_delete = s.get('id_prod_del')
    print(id_prod_delete)
    info_product_delete = [i for i in get_info_product(id_prod_delete)]
    print(info_product_delete)
    await bot.send_photo(message.from_user.id, photo=info_product_delete[0][4])
    await message.answer (f'Название продукта: {info_product_delete[0][1]}\nЦена:{info_product_delete[0][2]}\nОписание: {info_product_delete[0][3]}', reply_markup=del_product_kb())


@dp.message_handler(state=Add_product.name_new_product)
async def name_new_product(message, state=Add_product.name_new_product):
    await state.update_data(new_prod_name=message.text)
    await message.answer(f'Теперь введите стоимость {message.text}:>>')
    await Add_product.price_new_product.set()

@dp.message_handler(state=Add_product.price_new_product)
async def name_new_product(message, state=Add_product.price_new_product):
    try:
        print(float(message.text))
        await state.update_data(new_prod_price=float(message.text))
        await message.answer(f'Теперь введите описание товара:>>')
        await Add_product.info_new_product.set()
    except:
        await message.answer(f'Вы ввели неверный формат - {message.text}\nПовторите ввод:>>')
        await Add_product.price_new_product.set()


@dp.callback_query_handler(text = 'delete', state='*' )
async def delete_product_handler (callback:CallbackQuery):
    user_data = await dp.current_state(user=callback.message.chat.id).get_data()
    prod_id=user_data.get('id_prod_del')
    del_product(prod_id)
    await callback.answer(f'Удалено!', show_alert=True)
    await callback.message.answer('Выберите следующий продукт', reply_markup=products_board_for_del())
    await callback.message.edit_reply_markup(reply_markup=None)
    await delete_product_state.status_delete.set()


@dp.message_handler(state=Add_product.info_new_product)
async def name_new_product(message, state=Add_product.info_new_product):
    await state.update_data(new_prod_info=message.text)
    await message.answer(f'Теперь загрузите фотографию используя📎:>>')
    await Add_product.photo_new_product.set()

@dp.message_handler(content_types=['photo'], state=Add_product.photo_new_product)
async def prod_photo(message, state=Add_product.photo_new_product):
    photo_id=message.photo[-1].file_id
    print(photo_id)
    await state.update_data(new_prod_photo=photo_id)
    await message.answer('Изображение успешно добавлено, введите кол-во:')
    await Add_product.count_new_product.set()


@dp.message_handler(state=Add_product.count_new_product)
async def prod_photo(message, state=Add_product.count_new_product):
    if message.text.isdigit():
        await state.update_data(new_prod_count=int(message.text))
        all_info_new_product = await state.get_data()
        id_prod = len(get_products_ids()) + 1
        print(id_prod)
        print(all_info_new_product)
        name_prod = all_info_new_product.get('new_prod_name')
        price_prod = all_info_new_product.get('new_prod_price')
        info_prod = all_info_new_product.get('new_prod_info')
        photo_id_prod = all_info_new_product.get('new_prod_photo')
        count_prod = all_info_new_product.get('new_prod_count')
        add_new_product(id_prod, name_prod, price_prod, info_prod, photo_id_prod, count_prod)
        await bot.send_photo(message.from_user.id, photo=photo_id_prod,
                             caption=f'Название продукта: {name_prod}\nЦена:{price_prod}\nКол-во на складе: {count_prod}')
        await message.answer(f'Успешно добавлен {name_prod}')
        await state.finish()
        await start_cmd(message)
    else:
        await message.answer('Неверный формат! Введите снова:')
        await Add_product.count_new_product.set()

@dp.message_handler(state=black.add_id)
async def del_admin(message, state=black.add_id):
    check_users = get_allinfo_users()
    id_check_users = [i[0] for i in check_users]
    print(check_users)
    if message.text.isdigit() and len(message.text)>5 and len(message.text)<=10:
        if int(message.text) in id_check_users:
            delete_user(int(message.text))
        await message.answer('Успешное добавлен!', reply_markup=black_list_command())
        add_black_list(int(message.text))
        await state.finish()
        await Admin_edit_change.change_task.set()
    else:
        await message.answer('Вы ввели неверный ID, повторите ввод:')
        await state.finish()
        await black.add_id.set()

@dp.message_handler(state=black.del_id)
async def del_admin(message, state=black.del_id):
    info_black_list = info_allblack_list()
    id_del_black = [i[0] for i in info_black_list]
    if message.text.isdigit() and int(message.text) in id_del_black:
        await message.answer('Успешное удаление!', reply_markup=black_list_command())
        del_id_fromblack(int(message.text))
        await state.finish()
        await Admin_edit_change.change_task.set()
    else:
        await message.answer('Вы ввели неверный ID, повторите ввод:')
        await state.finish()
        await black.del_id.set()

@dp.message_handler(state=Admin_delete_admin.del_admin)
async def del_admin(message, state=Admin_delete_admin.del_admin):
    info_admins = DB.get_info_admins()
    id_del_admin = [i[0] for i in info_admins]
    print(id_del_admin)
    if int(message.text) in id_del_admin:
        await message.answer('Успешное удаление!', reply_markup=admin_list())
        delete_admin(int(message.text))
        await state.finish()
        await Admin_edit_change.change_task.set()
    else:
        await message.answer('Вы ввели неверный ID, повторите ввод:')
        await state.finish()
        await Admin_delete_admin.del_admin.set()

@dp.message_handler(state=Registration.get_name)
async def get_name(message, state=Registration.get_name):

    if message.text=='Взять из аккаунта':
        name=message.from_user.first_name
        await state.update_data(user_name=name)
        await message.answer(f'Отлично! {name}👍\nTеперь нам нужно знать Ваш телефон, нажмите поделиться👇:', reply_markup=phone_number_kb())
        await Registration.get_contact.set()
    elif message.text.isalpha():
        name=message.text
        await state.update_data(user_name=name)
        await message.answer(f'Отлично! {name}👍\nTеперь нам нужно знать Ваш телефон, нажмите поделиться👇:', reply_markup=phone_number_kb())
        await Registration.get_contact.set()
    else:
        await message.answer('Ой, что-то пошло не так, попробуйте снова!', reply_markup=get_name_kb())
        await Registration.get_name.set()


@dp.message_handler(state=Registration.get_contact, content_types=['contact'])
async def get_contact(message, state=Registration.get_contact):
        phone_number = message.contact.phone_number
        name=await state.get_data()
        await state.update_data(user_contact=phone_number)
        await message.answer(f'Отлично! {name["user_name"]}👍\nTеперь нам нужно знать Вашу локацию👇:', reply_markup=location_kb())
        await Registration.get_location.set()


@dp.message_handler(state=Registration.get_location, content_types=['location'])
async def get_location(message, state=Registration.get_location):
        location = (message.location.longitude, message.location.latitude)
        name = await state.get_data()
        await state.update_data(user_location=location)
        await message.answer(f'Отлично! {name["user_name"]}👍\nTеперь нам нужно знать Ваш пол👇:', reply_markup = gender_kb())
        await Registration.get_gender.set()
#
@dp.message_handler(state=Registration.get_gender, content_types=['text'])
async def get_gender(message, state=Registration.get_gender):

    name = await state.get_data()
    if message.text=='Мужской' or message.text=='Женский':
        gender=message.text
        await state.update_data(user_gender=gender)
        await message.answer(f'Отлично! {name["user_name"]}👍\nВы прошли регистрацию, поздравляем🎉🎉🎉')
    else:
        await message.answer(f'Ой! {name["user_name"]}\nВы допустили ошибку при выборе пола, воспользуйтесь кнопкой выбора!', reply_markup=gender_kb())
        await Registration.get_gender.set()
    all_info = await state.get_data()
    name = all_info.get('user_name')
    ph_num = all_info.get('user_contact')
    locat = all_info.get('user_location')
    gender = all_info.get('user_gender')
    id = message.from_user.id
    add_users(id,name,ph_num,locat[0],locat[1],gender)
    await state.finish()
    await start_cmd(message)

#__________________________________________________________________________________________________#

@dp.message_handler(state=RegistrationAdmins.get_name_admins)
async def get_name(message, state=RegistrationAdmins.get_name_admins):
    name=message.text
    if name.isalpha():
        await state.update_data(admin_name=name)
        await message.answer(f'Отлично! Укажите ID:')
        await RegistrationAdmins.get_id_admins.set()
    else:
        await message.answer('Ой, что-то пошло не так, попробуйте снова!')
        await RegistrationAdmins.get_name_admins.set()

@dp.message_handler(state=RegistrationAdmins.get_id_admins)
async def get_name(message, state=RegistrationAdmins.get_id_admins):
    if message.text.isdigit():
        await state.update_data(admin_id=message.text)
        await message.answer(f'Отлично! Укажите номер телефона (9 цифр):')
        await RegistrationAdmins.get_contact_admins.set()
    else:
        await message.answer('Ой, что-то пошло не так, попробуйте снова!')
        await RegistrationAdmins.get_id_admins.set()

@dp.message_handler(state=RegistrationAdmins.get_contact_admins)
async def get_contact(message, state=RegistrationAdmins.get_contact_admins):
        if message.text.isdigit() and len(message.text)==9:
            await state.update_data(admin_contact=message.text)
            await message.answer(f'Отлично! Укажите пол:')
            await RegistrationAdmins.get_gender_admins.set()
        else:
            await message.answer('Ой, что-то пошло не так, попробуйте снова!')
            await RegistrationAdmins.get_contact_admins.set()

@dp.message_handler(state=RegistrationAdmins.get_gender_admins)
async def get_contact(message, state=RegistrationAdmins.get_gender_admins):
        if message.text=='Мужской' or message.text=='Женский':
            await state.update_data(admin_gender=message.text)
            await message.answer(f'Отлично! Укажите должность:')
            await RegistrationAdmins.get_post_admins.set()
        else:
            await message.answer('Ой, что-то пошло не так, попробуйте снова! Введите "Мужской"/"Женский"')
            await RegistrationAdmins.get_gender_admins.set()

@dp.message_handler(state=RegistrationAdmins.get_post_admins)
async def get_location(message, state=RegistrationAdmins.get_post_admins):
    if message.text.isalpha():
        await state.update_data(admin_post=message.text)
        all_info = await state.get_data()
        add_admins(all_info['admin_id'], all_info['admin_name'], all_info['admin_contact'], all_info['admin_gender'], all_info['admin_post'])
        await message.answer(f'Отлично!👍\nВы создали нового администратора {all_info["admin_name"]}🎉🎉🎉')
        await state.finish()
        await start_cmd(message)
    else:
        await message.answer('Ой, что-то пошло не так, попробуйте снова!')
        await RegistrationAdmins.get_post_admins.set()

@dp.message_handler(commands=['menu'], state='*')
async def get_location(message: types.Message):

        await message.answer('Сайт', reply_markup=open_site_kb())




executor.start_polling(dp)
