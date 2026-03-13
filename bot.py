from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "Here is the token for bot تحميل من سناب شات 👻 @snpFlashbot:

8744821732:AAFZxvZsKT93pVhjOAJ7O3q-UCU38aWDUZs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت اشتغل بنجاح ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
