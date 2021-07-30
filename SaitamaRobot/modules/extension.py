import random

from telegram import Update

from telegram.ext import CallbackContext

from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot import dispatcher

GIF = "https://telegra.ph/file/7f4e379a8095b8e9ac648.mp4"

def extension(update: Update, context: CallbackContext)
      bot = context.bot
            msg = update.effective_message
                  bot.send_video(DARE)
EXTENSION_HANDLER = DisableAbleCommandHandler = ("extension", run_async=True)

dispatcher.add_handler(EXTENSION_HANDLER)
