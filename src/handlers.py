from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from src.keyboard import reply_keyboard, inline_keyboard



router = Router()


class Quiz(StatesGroup):
    waiting_answer = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет,{message.from_user.full_name}",
     reply_markup=reply_keyboard
    )



@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        "/start - запуск \n"
        "/help - список команд \n"
        "/docs - документация языков программирования \n"
    )




@router.message(F.text == "Python")
async def get_python_info(message: Message):
    await message.answer("Python (Пайтон) — это высокоуровневый язык программирования с простым и понятным синтаксисом, ориентированный на читаемость кода и продуктивность разработчика.")





@router.message(F.text == "Java")
async def get_java_info(message: Message):
    await message.answer("Java — строгий, строго типизированный компилируемый язык программирования, заточенный под надежность, масштабируемость и безопасность.")






@router.message(F.text == "JavaScript")
async def get_javascript_info(message: Message):
    await message.answer("JavaScript — динамический интерпретируемый язык, созданный как «язык сценариев» для оживления веб-страниц, а сегодня ставший одним из самых популярных языков в мире.")





@router.message(Command('docs'))
async def cmd_docs(message: Message):
    await message.answer(
        "выберите документацию",
        reply_markup=inline_keyboard
    )







