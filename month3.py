import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
BOT_TOKEN = "8962190292:AAEz4_06wiXub1T2mkYSJbVj37L4Yj7C0_k"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}, я твой первый бот"
    )


@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "/start - приветствие\n"
        "/help - список команд" \
        "/about - узнать о боте"
    )



@dp.message(F.text.lower() == "группа")
async def cmd_group(message: Message):
    await message.answer(f"Твоя группа 70-1 ")



@dp.message(F.text.lower() == "пока")
async def cmd_bye(message: Message):
    await message.answer(f"До свидания ")





@dp.message(F.text.lower() == "как ты относишься к курьерам")
async def cmd_kura(message: Message):
    await message.answer(f"да я на курьеров никогда не пизжу если там чет разливается вообще похуй я один раз заказывал сладости молоко,мне пришли блять мясо блять,какие то блять овощи блять и этот блять и уголь блять я подумал ну ладно на шашлыки сегодня блять")









@dp.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer(
        "этот бот помогает узнать свою группу,и у него есть эхо"  
    )









@dp.message()
async def echo(message: Message):
    await message.answer(f"Вы написали {message.text}") 





async def main():
    print("Бот успешно запущен")
    await dp.start_polling(bot)





if __name__ == "__main__":
    asyncio.run(main())


















