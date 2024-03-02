from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакт')]],
        resize_keyboard=True,
        input_field_placeholder='Выберите пунт меню.')


router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}! Я бот длля продажи предметов в локальном магазине. \n что бы перейти к выполнению заказа напиши 'В меню'", reply_markup=main)


@router.message(F.text == 'Каталог')
async def get_catalog(message: Message):
    await message.answer('Функция каталога')

@router.message(F.text == 'Корзина')
async def get_busket(message: Message):
    await message.answer('Функция Корзины')

@router.message(F.text == 'Контакт')
async def get_contact(message: Message):
    await message.answer('Функция контакты')

@router.message(F.text == 'В меню')
async def get_menu(message: Message):
    await message.answer('you in menu')