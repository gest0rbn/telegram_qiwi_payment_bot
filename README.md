![Python310](https://img.shields.io/badge/python-3.10-green) <img alt="GitHub followers" src="https://img.shields.io/github/followers/gest0rbn?color=violet&style=plastic">

# ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54 'Родной') telegram_qiwi_payment_bot

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
##### Администратор только парсит базу данных и ему одним сообщением отправляются данные Telegram @nickname amount 12345 (см. скриншот)
![image](https://user-images.githubusercontent.com/66784042/178778128-f2e85e53-5cc1-42ca-bc29-504aaa6f952d.png)
    
### Коротко в скриншотах:
#### Admin
![image](https://user-images.githubusercontent.com/66784042/178778565-e3f6589a-57ed-4cee-9f35-1e565e76d19a.png)
#### User
#### база данных:
![image](https://user-images.githubusercontent.com/66784042/178785460-e0f9e528-8413-40b3-bd85-624be4d158ab.png)

![image](https://user-images.githubusercontent.com/66784042/178778463-e8408bce-5183-4150-b155-c76325875516.png)

![image](https://user-images.githubusercontent.com/66784042/178778490-d375261e-0e6c-40b3-8004-6fc9e2e4806b.png)

![image](https://user-images.githubusercontent.com/66784042/178778749-a39df357-f1bb-49a6-91ea-89f883b00493.png)

![image](https://user-images.githubusercontent.com/66784042/178778855-f1126844-cb3a-4f49-922e-92ffb22fbbe5.png)

![image](https://user-images.githubusercontent.com/66784042/178778996-c38fed07-e572-4476-b23f-50223626c68a.png)
###### P.S. да, я не закидывал 120000 рублей :grin:.

#### P.P.S. можете не обращать внимания на [pyqiwi_less](https://github.com/gest0rbn/telegram_qiwi_payment_bot/blob/main/pyqiwi_less.py). Разбирался, что в библиотеке pyqiwip2p да и как :blush:

# Спасибо за внимание! 
![heart](https://media1.giphy.com/media/jUKyEtnRx3OZQmQb2Q/giphy.gif?cid=6c09b952nxrtz7dsdw1y0lm418tip2kv83jlp5txzqelw9xt&rid=giphy.gif&ct=s)
