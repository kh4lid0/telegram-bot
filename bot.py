from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


‏TOKEN = "8744821732:AAHnRuOBfmOgL8_iE_w9yK14-qOfYYN75kw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت اشتغل بنجاح ✅")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اكتب /start لتشغيل البوت")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
