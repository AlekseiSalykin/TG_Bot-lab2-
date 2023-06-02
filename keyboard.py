from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
btnHelp = KeyboardButton('/help')
btnReg = KeyboardButton('/register')
kb.add(btnHelp).insert(btnReg)

btnsDoc = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите врача ниже")
btnDoc1 = KeyboardButton('/Терапевт')
btnDoc2 = KeyboardButton('/Хирург')
btnDoc3 = KeyboardButton('/Невролог')
btnsDoc.add(btnDoc1, btnDoc2, btnDoc3)

btnsDate = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите время ниже")
btnDate1 = KeyboardButton('/12:00(01.06.2023)')
btnDate2 = KeyboardButton('/13:00(01.06.2023)')
btnDate3 = KeyboardButton('/14:00(01.06.2023)')
btnDate4 = KeyboardButton('/15:00(01.06.2023)')
btnsDate.add(btnDate1, btnDate2, btnDate3, btnDate4)
