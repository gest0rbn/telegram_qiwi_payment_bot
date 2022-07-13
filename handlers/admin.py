from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from bot_create import bot
from config import admin_id
from inline_button import inl_admin
from base_data.data_base import sql_get_wallets


# панель администратора
async def start_admin(message: types.Message):
    if message.from_user.id == admin_id:
        await bot.send_message(message.from_user.id, 'Добрый день, уважаемый администратор', reply_markup=inl_admin)
    else:
        await bot.send_message(message.from_user.id, 'Вы не администратор!')


# спарсить кошельки из бд
async def check_wallets(callback: types.CallbackQuery):
    if callback.from_user.id == admin_id:
        await sql_get_wallets(callback)
        await callback.answer()


# регистрация хэндлеров для админа
def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(start_admin, commands='admin')
    dp.register_callback_query_handler(check_wallets, text='wallet_list')
