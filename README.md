# ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) telegram_qiwi_payment_bot

Telegram bot with Qiwi payment. This is my test project.
--------------------------
### <b>pip<b>
##### pip install aiogram
##### pip install pyQiwiP2P==2.0.1

### <b>Description<b>
##### переменной [admin_id](]https://github.com/gest0rbn/telegram_qiwi_payment_bot/blob/main/config.py#:~:text=%2712345%3AAB1CD2EFGH3%27-,admin_id) в [config.py](https://github.com/gest0rbn/telegram_qiwi_payment_bot/blob/main/config.py) присваиваем ваш user id (целое число)
    admin_id = 123456789
##### в переменных <b>prvt_key<b> и <b>bot_token<b> в [config.py](https://github.com/gest0rbn/telegram_qiwi_payment_bot/blob/main/config.py) указываем приватный ключ из Qiwi Api и токен бота.
    prvt_key = 'abCDEFGhijklmoP='
    bot_token = '12345:AB1CD2EFGH3'

#### Используется встроенная в Python база данных SQLite3. Указываетете сумму оплаты, оплачиваете счёт и информация отправляется в базу данных в виде user_id:total (никнейм тг:баланс)

### Admin functions
##### Администратор только парсит базу данных и ему одним сообщением отправляются данные Telegram @nickname amount 12345 (как пр-р)
    ![image](https://user-images.githubusercontent.com/66784042/178778128-f2e85e53-5cc1-42ca-bc29-504aaa6f952d.png)
    
### Коротко в скриншотах:
    
