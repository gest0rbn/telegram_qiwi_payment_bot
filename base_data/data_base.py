import sqlite3
from bot_create import bot


# функция запуска бд
def sql_start():
    global base, cur
    base = sqlite3.connect('users_wallet.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS wallet(user_id TEXT PRIMARY_KEY, total TEXT)')
    base.commit()


# добавить новое лицо (кошелёк) в бд
async def sql_new_insert(callback, amount):
    cur.execute('INSERT INTO wallet VALUES (?, ?)', (callback, amount))
    base.commit()


# обновить баланс уже существующего кошелька
async def sql_update_money(amount, callback):
    cur.execute('UPDATE wallet SET total = ? WHERE user_id = ?', (amount, callback))
    base.commit()


# спарсить кошельки
async def sql_get_wallets(callback):
    res = []
    for i in cur.execute('SELECT * FROM wallet').fetchall():
        res.append(f'Telegram @{i[0]} amount {i[1]}')
    res.sort()
    await bot.send_message(callback.from_user.id, '\n'.join(res))


# прочитать и взять значение баланса
def sql_read(callback):
    money = cur.execute('SELECT total FROM wallet WHERE user_id = ?', (callback,)).fetchone()
    return int(float(money[0]))


# взять user_id
def sql_get_user():
    payer = cur.execute('SELECT user_id FROM wallet').fetchone()
    return payer[0]
