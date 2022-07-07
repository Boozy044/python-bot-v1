from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ContentType
import logging
import config
from databese import get_answer, get_not_answer, make_logs
from keyboards import get_main_keyboard

logging.basicConfig(level=logging.ERROR)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


def get_full_name(message):
    name = ''
    if message.chat.first_name:
        name += message.chat.first_name
    if message.chat.last_name:
        name += ' '
        name += message.chat.last_name
    return str(name)


@dp.message_handler(content_types=[ContentType.TEXT])
async def user_answer(message: Message):
    full_name = get_full_name(message)
    corrective, answers = await get_answer(message.text)

    if answers:
        for answer in answers:
            await message.answer(f'{answer[0]}', reply_markup=await get_main_keyboard())
            await make_logs(message.chat.id, full_name, message.text, answer[0], corrective[0])
    else:
        answers = await get_not_answer()
        await message.answer(f'{answers[0]}', reply_markup=await get_main_keyboard())
        await make_logs(message.chat.id, full_name, message.text, answers[0], corrective[0])


@dp.message_handler(content_types=[ContentType.VOICE])
async def voice_message_handler(message: Message):
    full_name = get_full_name(message)
    corrective, answers = await get_answer("VOICE")

    if answers:
        for answer in answers:
            await message.answer(f'{answer[0]}')
            await make_logs(message.chat.id, full_name, message.text, answer[0], corrective[0])
    else:
        answers = await get_not_answer()
        await message.answer(f'{answers[0]}')
        await make_logs(message.chat.id, full_name, message.text, answers[0], corrective[0])


@dp.message_handler(content_types=[ContentType.PHOTO])
async def photo_message_handler(message: Message):
    full_name = get_full_name(message)
    corrective, answers = await get_answer("PHOTO")

    if answers:
        for answer in answers:
            await message.answer(f'{answer[0]}')
            await make_logs(message.chat.id, full_name, message.text, answer[0], corrective[0])
    else:
        answers = await get_not_answer()
        await message.answer(f'{answers[0]}')
        await make_logs(message.chat.id, full_name, message.text, answers[0], corrective[0])


@dp.message_handler(content_types=[ContentType.VIDEO])
async def video_message_handler(message: Message):
    full_name = get_full_name(message)
    corrective, answers = await get_answer("VIDEO")

    if answers:
        for answer in answers:
            await message.answer(f'{answer[0]}')
            await make_logs(message.chat.id, full_name, message.text, answer[0], corrective[0])
    else:
        answers = await get_not_answer()
        await message.answer(f'{answers[0]}')
        await make_logs(message.chat.id, full_name, message.text, answers[0], corrective[0])


@dp.message_handler(content_types=[ContentType.DOCUMENT])
async def document_message_handler(message: Message):
    full_name = get_full_name(message)
    corrective, answers = await get_answer("DOCUMENT")

    if answers:
        for answer in answers:
            await message.answer(f'{answer[0]}')
            await make_logs(message.chat.id, full_name, message.text, answer[0], corrective[0])
    else:
        answers = await get_not_answer()
        await message.answer(f'{answers[0]}')
        await make_logs(message.chat.id, full_name, message.text, answers[0], corrective[0])


if __name__ == '__main__':
    print('Бот запущен!')
    executor.start_polling(dp, skip_updates=True)
