from aiogram import F, Router

from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from basic_text import main_page_text, contact_text
from app.other.buttons import Buttons
from app.other.functions import return_anketa

class Reg(StatesGroup):
    name = State()
    number = State()
    adress = State()
    articul = State()

#CONSTANS:
name = ''
adress = ''
articul = ''

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello! Я бот длля продажи предметов в локальном магазине \n что бы перейти к выполнению заказа напиши 'Корзина 🛒'", 
                         reply_markup=Buttons.menu_button)

@router.message(F.text == 'В меню🧑🏿‍💻🗂')
async def get_menu(message: Message):
    await message.answer(str(main_page_text), reply_markup=Buttons.menu_button)

@router.message(F.text == 'Информация о нас 📃✏️')
async def getcatalog(message: Message):
    await message.answer(str(main_page_text), reply_markup=Buttons.about_us, one_time_keyboard=True)

@router.message(F.text == 'Корзина 🛒')
async def get_busket(message: Message):
    await message.answer('Выбирите действия из доступных, для поиска товаров, их описания и артиклей переходите в нашу группу https://vk.******',reply_markup=Buttons.busket_button)

@router.message(F.text == 'Контакт 📰')
async def get_contact(message: Message):
    await message.answer(str(contact_text), reply_markup=Buttons.bool_button)

@router.message(F.text == 'Перейти к оплате💰💳')
async def go_to_pay(message: Message):
    await message.answer(f'Корзина:')
    await message.answer('Общаю сумма: "finaly_prize"')
    await message.answer('Ссылка на страцницу с оплатой')
    await message.answer('Для ввода данных напишите "/reg"', reply_markup=Buttons.go_to_pay_button)

@router.message(F.text == 'Да, это мои данные✅')
async def verification_true(message: Message):
    await message.answer(str(return_anketa(name, adress)))
    await message.answer('Для отправки заказа перешлите данное собщение с чеком оплаты в личные сообщения пользователю @bot_shop_example', reply_markup=Buttons.bool_button)

@router.message(F.text == 'Нет, я хочу переписать их❌')
async def not_true_verification(message: Message):
    await message.answer('Введите "/reg", чтобы перезаписать ваши данные', reply_markup=Buttons.bool_button)


'''
docstring
Функци я которая принимает значение '/reg' и принимает паеременные adress, name и записывает их в переменные
'''
@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите артикул выбранного товара: ', reply_markup=Buttons.bool_button)

@router.message(Reg.name)
async def reg_second(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите ваш номер для связи:')

@router.message(Reg.number)
async def second_three(message: Message, state: FSMContext):
    
    global name
    global adress
    
    await state.update_data(number=message.text)
    await message.answer('Регистрация прошла успешно')
    data = await state.get_data() #{'name': 'tag', 'number': 'comment'}
    name = data['name']
    adress = data['number']
    await message.answer(f'Подтвердите ваши данные: \nАртикул товара,которого вы хотите заказать: {name}, ваш номер для обратной связи: {adress}', reply_markup=Buttons.verifcation)