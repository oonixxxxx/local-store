from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class Buttons: 
    menu_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Корзина 🛒')],
                                        [KeyboardButton(text='Информация о нас 📃✏️'), KeyboardButton(text='Контакт 📰')]],
            resize_keyboard=True,
            input_field_placeholder='Выберите пунт меню.')


    busket_button = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='В меню🧑🏿‍💻🗂')],
        [KeyboardButton(text='Добавить товар🛍'), KeyboardButton(text='Перейти к оплате💰💳')]],
        resize_keyboard=True)


    add_item_button = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Добавить еще товар🛍'), KeyboardButton(text='Перейти к оплате💰💳')]], 
        resize_keyboard=True,
        input_field_placeholder='Введите артикуль')


    verifcation = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Да, это мои данные✅'), KeyboardButton(text='Нет, я хочу переписать их❌')]],
        resize_keyboard=True,
        input_field_placeholder='Выбирите ваш вариант'
    )

    go_to_pay_button = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='/reg'), KeyboardButton(text='В меню🧑🏿‍💻🗂')]],
        resize_keyboard=True
    )

    about_us = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='В меню🧑🏿‍💻🗂')]],
        resize_keyboard=True
    )

    bool_button = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='В меню🧑🏿‍💻🗂')]],
        resize_keyboard=True
    )