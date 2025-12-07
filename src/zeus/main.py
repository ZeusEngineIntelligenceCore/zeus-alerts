import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN: str | None = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN missing! Set it before running.")
assert TOKEN is not None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text("Zeus Alerts bot is online!")
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(f"You said: {update.message.text}")

async def async_main() -> None:
    """
    Initializes and runs the Telegram bot application.
    """
    app = ApplicationBuilder().token(TOKEN).build() # type: ignore

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot is running… send /start in Telegram.")
    await app.run_polling(allowed_updates=Update.ALL_TYPES) # pyright: ignore[reportGeneralTypeIssues]

if __name__ == "__main__":
    import asyncio
    asyncio.run(async_main())