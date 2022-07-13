from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# инлайн клавиатура (пополнить, баланс)
inl_markup_balance = InlineKeyboardMarkup()
pay = InlineKeyboardButton(text='Пополнить баланс', callback_data='pay_data')
balance = InlineKeyboardButton(text='Мой баланс', callback_data='balance_data')
inl_markup_balance.row(pay, balance)
