from telegram import Bot
import asyncio

# Конфигурация
TOKEN = "8189040421:AAGr_Y32jcTxuR4qLTN3sPzYfdqEewkEPxI"
CHAT_ID = "5164380779"


def send_metrics(pressure: float, flow: float, filter_status: float):

    async def async_send():
        bot = Bot(token=TOKEN)
        message = (
            "🚨 *Новые показания системы*\n\n"
            f"• *Давление*: `{pressure:.1f}` Паскаль\n"
            f"• *Поток*: `{flow:.1f}` кг/с\n"
            f"• *Состояние фильтра*: `{filter_status:.1f}%`"
        )
        await bot.send_message(
            chat_id=CHAT_ID,
            text=message,
            parse_mode="Markdown"
        )

    try:
        asyncio.run(async_send())
    except Exception as e:
        print(f"⚠️ Ошибка отправки в Telegram: {str(e)}")

def send_mail_need_help():

    async def async_send():
        bot = Bot(token=TOKEN)
        message = (
            "🚨 *Пользователь вызвал работника*\n\n"
            f"• *Пользователю требуется помощь работника на фильтре №1 сектра B"
        )
        await bot.send_message(
            chat_id=CHAT_ID,
            text=message,
            parse_mode="Markdown"
        )

    try:
        asyncio.run(async_send())
    except Exception as e:
        print(f"⚠️ Ошибка отправки в Telegram: {str(e)}")
