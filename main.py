from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove
from keyboard import kb, btnsDoc, btnsDate
import pandas as pd

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>Список команд</em>
<b>/start</b> - <em>Начало работы с ботом</em>
<b>/register</b> - <em>Записаться к врачу</em>
"""

dict_doc_list = {}
list_doc = []
list_name = []
list_date = []


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode='HTML', reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Добро пожаловать в Телеграмм бота нашей поликлиники!",
                           parse_mode='HTML', reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['register'])
async def register_command(message: types.Message):
    await message.answer(text='Выберите доктора: ', parse_mode='HTML', reply_markup=btnsDoc)
    await message.delete()

    @dp.message_handler(commands=['Терапевт', 'Хирург', 'Невролог'])
    async def reg_name(message: types.Message):
        await message.answer(text="Выберите дату и время: ", parse_mode='HTML', reply_markup=btnsDate)
        text = message.text
        list_doc.append(text)

    @dp.message_handler(commands=['12:00(01.06.2023)', '13:00(01.06.2023)', '14:00(01.06.2023)', '15:00(01.06.2023)'])
    async def reg_doctor(message: types.Message):
        await message.answer(text="Введите ваше ФИО: ", parse_mode='HTML', reply_markup=ReplyKeyboardRemove())
        text = message.text
        list_date.append(text)

    @dp.message_handler()
    async def reg_date(message: types.Message):
        text = message.text
        if message.text.count(' ') == 2:
            await message.reply(text="Вы записались!", parse_mode='HTML', reply_markup=kb)
            list_name.append(text)
            for i in range(len(list_name)):
                name = list_name[i]
                date = list_date[i]
                dict_doc_list[list_doc[i]] = name + ": " + date

            df = pd.DataFrame(data=dict_doc_list, index=['клиенты'])
            df = (df.T)
            df.to_excel('Doctor_List.xlsx')
        else:
            await message.reply(text="ФИО не коректно! Попробуйте еще раз!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
