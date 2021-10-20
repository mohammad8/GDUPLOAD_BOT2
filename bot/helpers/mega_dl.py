import os
import shutil
#import filetype
#import moviepy.editor
import time
import asyncio
import logging
import subprocess
import datetime
from mega import Mega
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
#from hurry.filesize import size
#from megadl.progress import progress_for_pyrogram, humanbytes
#from megadl.forcesub import handle_force_subscribe
#from config import Config
#from megadl.file_handler import send_to_transfersh_async, progress
from bot import DOWNLOAD_DIRECTORY

# Logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Mega Client
mega = Mega()
m = mega.login()

# path we gonna give the download
basedir = DOWNLOAD_DIRECTORY

# Automatic Url Detect (From OneDLBot)
MEGA_REGEX = (r"^((?:https?:)?\/\/)"
              r"?((?:www)\.)"
              r"?((?:mega\.nz))"
              r"(\/)([-a-zA-Z0-9()@:%_\+.~#?&//=]*)([\w\-]+)(\S+)?$")



#@Client.on_message(filters.regex(MEGA_REGEX) & filters.private & filters.incoming & ~filters.edited)
async def megadl(client, message):

    url = message.text
    user = f'[Upload Done!](tg://user?id={message.from_user.id})'
    userpath = str(message.from_user.id)
    alreadylol = basedir + userpath
    if not os.path.isdir(alreadylol):
        megadldir = os.makedirs(alreadylol)
    try:
        download_msg = await message.reply_text(text=f"**Downloading:** `{url}` \n\nThis Process May Take Some Time 🤷‍♂️!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel Mega DL", callback_data="cancel")]]), reply_to_message_id=message.message_id)
        #ist = (datetime.datetime.utcnow() + datetime.timedelta(minutes=30, hours=5)).strftime("%d/%m/%Y, %H:%M:%S")
        #bst = (datetime.datetime.utcnow() + datetime.timedelta(minutes=00, hours=6)).strftime("%d/%m/%Y, %H:%M:%S")
        #now = f"\n{ist} (GMT+05:30)`\n`{bst} (GMT+06:00)"
        #download_start = await bot.send_message(Config.LOG_CHANNEL, f"**Bot Become Busy Now !!** \n\nDownload Started at `{now}`", parse_mode="markdown")
        magapylol = m.download_url(url, alreadylol)
        await download_msg.edit("**Downloaded Successfully 😉!**")
        return str(magapylol)
    except Exception as e:
        await download_msg.edit(f"**Error:** `{e}`")
        #ist = (datetime.datetime.utcnow() + datetime.timedelta(minutes=30, hours=5)).strftime("%d/%m/%Y, %H:%M:%S")
        #bst = (datetime.datetime.utcnow() + datetime.timedelta(minutes=00, hours=6)).strftime("%d/%m/%Y, %H:%M:%S")
        #now = f"\n{ist} (GMT+05:30)`\n`{bst} (GMT+06:00)"
        #await bot.send_message(Config.LOG_CHANNEL, f"**Bot Become Free Now !!** \n\nProcess Done at `{now}`", parse_mode="markdown")
        #await download_start.delete()
        shutil.rmtree(basedir + "/" + userpath)
        return