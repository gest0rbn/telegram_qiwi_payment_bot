from aiogram.utils import executor
from bot_create import dp
from handlers import user, admin
from base_data import data_base

# запуск базы данных
data_base.sql_start()
# вызов функции, в которую записаны хэндлеры
admin.register_handler_admin(dp)
user.register_handler_user(dp)

executor.start_polling(dp, skip_updates=True)
