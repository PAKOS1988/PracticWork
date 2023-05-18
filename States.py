from aiogram.dispatcher.filters.state import State,StatesGroup



class Admin(StatesGroup):
    change_task=State()

class black(StatesGroup):
    add_id=State()
    del_id=State()

class User(StatesGroup):
    change_task=State() #Получаем этап выбора с первой панели клиента
class New_user(StatesGroup):
    change_task=State() #Получаем этап выбора с первой панели проходимца:)

class Registration(StatesGroup):
    get_name=State()
    get_contact=State()
    get_location=State()
    get_gender=State()

class Admin_edit_change(StatesGroup):
    change_task=State()

class Admin_delete_admin(StatesGroup):
    del_admin=State()

class RegistrationAdmins(StatesGroup):
    get_id_admins=State()
    get_name_admins=State()
    get_contact_admins=State()
    get_gender_admins=State()
    get_post_admins=State()

class Add_product(StatesGroup):
    name_new_product=State()
    price_new_product=State()
    info_new_product=State()
    photo_new_product=State()
    count_new_product=State()
    all_info_new_product=State()

class delete_product_state(StatesGroup):
    status_delete = State()