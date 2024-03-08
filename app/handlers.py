from email import message
from os import name
from aiogram import F, Router

from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram.types.input_file import FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

class Reg(StatesGroup):
    name = State()
    number = State()
    adress = State()
    articul = State()


#CONSTANS:
name = ''
adress = ''
articul = ''


'''
idias:
    очистка корзины
'''

class Articules:
    articules_dict_name = {
        '563564645645': 'shoes 1',
        '5646764746746': 'shoes 2',
        '564465556666': 'shoes 3',
        '564465559999': 'shoes 4'
        }


    articules_dict_prize = {
        'shoes 1': '77$',
        'shoes 2': '86$',
        'shoes 3': '76$',
        'shoes 4': '97$'
    }



class Buttons: 
    menu_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Корзина 🛒')],
                                        [KeyboardButton(text='Информация о нас 📃✏️'), KeyboardButton(text='Контакт 📰')]],
            resize_keyboard=True,
            input_field_placeholder='Выберите пунт меню.')


    busket_button = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='В меню')],
        [KeyboardButton(text='Добавить товар'), KeyboardButton(text='Перейти к оплате')]],
        resize_keyboard=True)


    add_item_button = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Добавить еще товар'), KeyboardButton(text='Перейти к оплате')]], 
        resize_keyboard=True,
        input_field_placeholder='Введите артикуль')


    verifcation = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Да, это мои данные'), KeyboardButton(text='Нет, я хочу переписать их')]],
        resize_keyboard=True,
        input_field_placeholder='Выбирите ваш вариант'
    )

    go_to_pay_button = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='/reg'), KeyboardButton(text='В меню')]],
        resize_keyboard=True
    )

    about_us = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='В меню')]],
        resize_keyboard=True
    )



router = Router()
catalog_photo = FSInputFile('demo.jpg')


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello! Я бот длля продажи предметов в локальном магазине \n что бы перейти к выполнению заказа напиши 'Корзина 🛒'", 
                         reply_markup=Buttons.menu_button)


@router.message(F.text == 'Информация о нас 📃✏️')
async def getcatalog(message: Message):
    await message.answer('''  - Donda Clothing
        • С текущего момента все ваши посылки будут сохранять герметичность до момента передачи вам. Вы полностью сами вскроете посылку
        • Площадка 95 - это аналог всеми известной русской площадки 📱, только в Китае. Огромное количество позиций начиная с носков Nike заканчивая Nike AJ1 Dior. Все вещи проходят обязательный Legit Check, этим занимается Poizon 🛒
        • Площадка Taobao, о ней слова излишни. Там вы сможете найти абсолютно все необходимое. 
        • Доставка по России и внутри Владимира. Мы предлагаем отправку ваших посылок транспортной компанией СДЭК, Почта России, Boxberry📦
        • Курьер привезет вашу посылку в целостности и сохранности. Стоимости данных услуг уточняются индивидуально🤍

        • Новая удобная группа с отзывами для наших новых клиентов ''', reply_markup=Buttons.about_us)


@router.message(F.text == 'Корзина 🛒')
async def get_busket(message: Message):
    await message.answer('Выбирите действия из доступных, для поиска товаров, их описания и артиклей переходите в нашу группу https://vk.******',reply_markup=Buttons.busket_button)


#    await message.answer(f'Ваш товар {Articules.articules_dict_name[str(articul)]} по стоимости - {Articules.articules_dict_prize[str(Articules.articules_dict_name[str(articul)])]}')


@router.message(F.text == 'Добавить товар')
async def func_add_item(message: Message):
    await message.answer('add item')


@router.message(F.text == 'Перейти к оплате')
async def go_to_pay(message: Message):
    await message.answer('Ссылка на страцницу с оплатой')
    await message.answer('Для ввода данных напишите "/reg"', reply_markup=Buttons.go_to_pay_button)


@router.message(F.text == 'Контакт 📰')
async def get_contact(message: Message):
    await message.answer('Функция контакты')


@router.message(F.text == 'В меню')
async def get_menu(message: Message):
    await message.answer('you in menu', reply_markup=Buttons.menu_button)

@router.message(F.text == 'Да, это мои данные')
async def verification_true(message: Message):
    await message.answer('Ваши данные собираются...')
    await message.answer(f'Имя: {name} \nАдрес: {adress} \nОформил заказ на товар с артикулем "артикуль" "нейм товара" по стоимости "стоимость товара" \nЧек приложен:')
    await message.answer('Для отправки заказа перешлите данное собщение с чеком оплаты в личные сообщения пользователю @bot_shop_example')


@router.message(F.text == 'Нет, я хочу переписать их')
async def not_true_verification(message: Message):
    await message.answer('Введите "/reg", чтобы перезаписать ваши данные')


'''
docstring
Функци я которая принимает значение '/reg' и принимает паеременные adress, name и записывает их в переменные
'''
@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите ваше имя')


@router.message(Reg.name)
async def reg_second(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите адрес')


@router.message(Reg.number)
async def second_three(message: Message, state: FSMContext):
    
    global name
    global adress
    
    await state.update_data(number=message.text)
    await message.answer('Регистрация прошла успешно')
    data = await state.get_data() #{'name': 'your name', 'number': 'number'}
    name = data['name']
    adress = data['number']
    
    await message.answer(f'Подтвердите ваши данные: \n Ваше имя: {name}, ваш адресс: {adress}', reply_markup=Buttons.verifcation)