from aiogram import F, Router
from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.input_file import FSInputFile


menu_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Информация о нас'), KeyboardButton(text='Контакт')]],
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
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}! Я бот длля продажи предметов в локальном магазине \n что бы перейти к выполнению заказа напиши 'В меню'", 
                         reply_markup=menu_button)


@router.message(F.text == 'Информация о нас')
async def getcatalog(message: Message):
    await message.answer('info about us')


@router.message(F.text == 'Корзина')
async def get_busket(message: Message):
    await message.answer('функционал корзины',reply_markup=busket_button)


@router.message(F.text == 'Добавить товар')
async def add_item(message: Message):
    await message.answer('Принимается некое число, артикуль', reply_markup=add_item_button)


@router.message(F.text == 'Перейти к оплате')
async def go_to_pay(message: Message):
    await message.answer('Ссылка на страцницу с оплатой')

#!идея: функция отправки чека им артикула администратору для отправки input: name, adress, check_photo

@router.message(F.text == 'Контакт')
async def get_contact(message: Message):
    await message.answer('Функция контакты')


@router.message(F.text == 'В меню')
async def get_menu(message: Message):
    await message.answer('you in menu', reply_markup=menu_button)