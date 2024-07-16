from aiogram import Bot, Dispatcher, html
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

class Form(StatesGroup):
    waiting_for_city = State()

bold_text = html.bold("""АКТУАЛЬНЫЕ КОНТАКТЫ ТЕХНИЧЕСКОЙ ПОДДЕРЖКИ НАХОДЯТСЯ В НАШЕМ БОТЕ, НАПИСАТЬ В ПОДДЕРЖКУ МОЖНО НАЖАВ НА КНОПКУ НИЖЕ, НЕ ПЕРЕХОДИТЕ ПО КОНТАКТАМ ТЕХ.ПОДДЕРЖКИ ЕСЛИ ВАМ ЕЕ СКИНУЛА МОДЕЛЬ!
НЕ ПЕРЕВОДИТЕ МОДЕЛЯМ СРЕДСТВА, ЕСЛИ НЕ ХОТИТЕ БЫТЬ ОБМАНУТЫМИ, ВСЕ ПЛАТЕЖИ ПРОХОДЯТ ИСКЛЮЧИТЕЛЬНО ЧЕРЕЗ АГЕНСТВО!""")

welcome_message = f"""❗️ ВНИМАНИЕ ❗️

{bold_text}

Администрация не несёт ответственность за потерю денежных средств! Остерегайтесь мошенников!"""

API_KEY = "6991255536:AAGPkpTyqGFF3VrmzIC1xh-z_dvkUay8SUI"

storage = MemoryStorage()

session = AiohttpSession(proxy='http://proxy.server:3128')

bot = Bot(API_KEY, default=DefaultBotProperties(parse_mode=ParseMode.HTML), session=session)

dp = Dispatcher(storage=storage)