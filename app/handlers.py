from ipaddress import AddressValueError
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


menu_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Корзина 🛒')],
                                     [KeyboardButton(text='Информация о нас 📃✏️'), KeyboardButton(text='Контакт 📰')]],
        resize_keyboard=True,
        input_field_placeholder='Выберите пунт меню.')


busket_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Добавить товар'), KeyboardButton(text='Перейти к оплате')]],
    resize_keyboard=True)


add_item_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Добавить еще товар'), KeyboardButton(text='Перейти к оплате')]], 
    resize_keyboard=True,
    input_field_placeholder='Введите артикуль')


router = Router()
catalog_photo = FSInputFile('demo.jpg')


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello! Я бот длля продажи предметов в локальном магазине \n что бы перейти к выполнению заказа напиши 'В меню'", 
                         reply_markup=menu_button)


@router.message(F.text == 'Информация о нас 📃✏️')
async def getcatalog(message: Message):
    await message.answer('info about us')


@router.message(F.text == 'Корзина 🛒')
async def get_busket(message: Message):
    await message.answer('функционал корзины',reply_markup=busket_button)


@router.message(F.text == 'Добавить товар')
async def add_item(message: Message, state: FSMContext):
    await state.set_state(Reg.articul)
    await message.answer('Принимается некое число, артикуль', reply_markup=add_item_button)


@router.message(F.text == 'Перейти к оплате')
async def go_to_pay(message: Message):
    await message.answer('Ссылка на страцницу с оплатой')

#!идея: функция отправки чека им артикула администратору для отправки input: name, adress, check_photo

@router.message(F.text == 'Контакт 📰')
async def get_contact(message: Message):
    await message.answer('Функция контакты')


@router.message(F.text == 'В меню')
async def get_menu(message: Message):
    await message.answer('you in menu', reply_markup=menu_button)

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
    await message.answer('Введите номер телефона')


@router.message(Reg.number)
async def second_three(message: Message, state: FSMContext):
    
    global name
    global adress
    
    await state.update_data(number=message.text)
    await message.answer('Регистрация прошла успешно')
    data = await state.get_data() #{'name': 'your name', 'number': 'number'}
    name = data['name']
    adress = data['number']