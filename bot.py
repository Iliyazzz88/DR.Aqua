import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# تنظیمات لاگ‌گیری
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# تابع شروع
def start(update, context):
    update.message.reply_text('سلام! من ربات iKavar هستم. سوالات آکواریومی خود را بپرسید.')

# تابع پاسخ به پیام‌ها
def echo(update, context):
    text = update.message.text.lower()
    if 'ماهی' in text:
        update.message.reply_text('برای نگهداری ماهی، دمای مناسب آب را بین ۲۴ تا ۲۶ درجه نگه دارید.')
    elif 'آکواریوم' in text:
        update.message.reply_text('تمیز نگه داشتن آکواریوم بسیار مهم است. فیلتر را هر هفته بررسی کنید.')
    else:
        update.message.reply_text('متأسفم، متوجه نشدم. لطفاً سوال خود را دقیق‌تر بپرسید.')

def main():
    # توکن ربات را از متغیر محیطی دریافت می‌کنیم
    import os
    TOKEN = os.environ.get('BOT_TOKEN')
    if not TOKEN:
        print("توکن ربات تنظیم نشده است.")
        return

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
