#REBELBOT 
from . import *
from telethon import Button, custom

from userbot import bot

from userbot import ALIVE_NAME
OWNER_NAME = ALIVE_NAME
OWNER_ID = bot.uid


REBELBOT = bot.me.first_name
REBEL = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={REBEL})"
REBEL_logo =  "https://telegra.ph/file/874648f62d9b055b17974.jpg"
REBEL_logo1 = "https://telegra.ph/file/67fde58014d6e898685ba.jpg"
REBEL_logo2 =  "https://telegra.ph/file/391f33c13cc62439e3bb7.jpg"
REBEL_logo4 = "https://telegra.ph/file/2625e188425c8cab5a244.jpg"
REBEL_logo3 = "https://telegra.ph/file/dbc482d8055522ac3296d.jpg"
REBELversion = "𝚅2.3"

perf = "[ 𝐑𝐄𝐁𝐄𝐋 𝐁𝐎𝐓 ]"


DEVLIST = [
    "1858407508 1418571871"
]

async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button