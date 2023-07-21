from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

async def start_menu_btn():
  btn = ReplyKeyboardMarkup(resize_keyboard=True)
  btn.row("🗳 Ovoz berish","💰 Balans")
  btn.row("🔗 Referal ssilka", "📝 Qo'llanma")

  return btn


async def mtart_menu_btn():
  btn = ReplyKeyboardMarkup(resize_keyboard=True)
  btn.row("💳yechib olish")
  btn.row("🚫bekor qilish")

  return btn