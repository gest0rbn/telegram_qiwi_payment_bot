from aiogram import types
from aiogram.types import InlineKeyboardButton
from aiogram.dispatcher import Dispatcher
from time import sleep
from inline_button import inl_markup_balance, inl_markup_pay
from keyboard import keyb
from api_qiwi import p2p
from base_data.data_base import sql_new_insert, sql_read, sql_get_user, sql_update_money


# приветствие
async def start(message: types.Message):
    await message.answer(f'Привет, @{message.from_user.username}', reply_markup=keyb)
    await message.delete()
    sleep(0.5)
    await message.answer('Я - бот для пополнения баланса.\nНажмите на кнопку, чтобы пополнить баланс\n'
                         'Снизу инлайн кнопка с текстом "Пополнить баланс".', reply_markup=inl_markup_balance)


# баланс
async def check_balance(callback: types.CallbackQuery):
    await callback.message.answer(f"Ваш баланс: <b>{sql_read(callback.from_user.username)}</b> рублей.")


# пополнение баланса
async def pay_func(callback: types.CallbackQuery):
    await callback.message.answer("Введите сумму, на которую Вы хотите пополнить баланс (<b>минимум 1 рубль</b>)")
    await callback.answer()


# создание платёжа на введенную сумму
async def get_amount(message: types.Message):
    amount = message.text
    if int(amount) > 0:
        global new_bill
        new_bill = p2p.bill(amount=int(amount),
                            lifetime=5,
                            comment=(comment := str(message.from_user.id) + amount)
                            )
        await message.answer(f'Платеж на сумму {amount} рублей успешно создан!\nПроверьте комментарий {comment}',
                             reply_markup=inl_markup_pay.row(InlineKeyboardButton(text='Оплатить',
                                                                                  url=str(new_bill.pay_url)),
                                                             InlineKeyboardButton(text='Проверить платёж',
                                                                                  callback_data='check_status')
                                                             ))
    else:
        await message.answer('Минимальная сумма - 1 рубль.')


# статус платёжа ("ожидание", "отменён", "успешен, последующее зачисление на баланс бота")
async def status_payment(callback: types.CallbackQuery):
    status = p2p.check(new_bill.bill_id).status
    if status == 'WAITING':
        await callback.answer('Ожидаю платёж')
    elif status == 'REJECTED':
        await callback.answer('Платёж не прошёл или был отменён', show_alert=True)
    else:
        if str(callback.from_user.id) in sql_get_user():
            await sql_update_money(
                sql_read(callback.from_user.username) + int(float((am := p2p.check(new_bill.bill_id).amount))),
                callback.from_user.username)
            await callback.message.answer(f'На ваш счёт зачислено {int(float(am))} рублей!')
            await callback.answer()
        else:
            await sql_new_insert(callback.from_user.username, int(float((am := p2p.check(new_bill.bill_id).amount))))
            await callback.message.answer(f'На ваш счёт зачислено {int(float(am))} рублей!')
            await callback.answer()


# хэндлеры(удобнее, нежели декораторы)
def register_handler_user(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_callback_query_handler(check_balance, text='balance_data')
    dp.register_callback_query_handler(pay_func, text='pay_data')
    dp.register_message_handler(get_amount)
    dp.register_callback_query_handler(status_payment, text='check_status')
