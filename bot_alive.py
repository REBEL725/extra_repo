from telethon import events
from . import *
from userbot import ALIVE_NAME
from userbot import bot

REBEL_USER = bot.me.first_name
REBEL = bot.uid
mention = f"[{REBEL_USER}](tg://user?id={REBEL})"

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "REBEL"


PM_IMG = "https://telegra.ph/file/67fde58014d6e898685ba.jpg"
pm_caption += f"┏━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `𝚖𝚊𝚜𝚝𝚎𝚛:`{mention}` \n"
pm_caption += f"┣•➳➠ `𝚅𝚎𝚛𝚜𝚒𝚘𝚗:` `2.3`\n"
pm_caption += f"┣•➳➠ `𝙲𝚑𝚊𝚗𝚗𝚎𝚕:` [𝙹𝙾𝙸𝙽](https://t.me/REBELBOT_SUPPORT)\n"
pm_caption += f"┣•➳➠ `𝙲𝚛𝚎𝚊𝚝𝚘𝚛:` [𝚁𝙴𝙱𝙴𝙻](https://t.me/REBEL_IS_OP)\n"
pm_caption += f"┣•➳➠ `𝚂𝚞𝚙𝚙𝚘𝚛𝚝𝚎𝚛:` [𝙽𝙸𝚂𝙷𝚄](https://t.me/nishuop)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━\n"


# only Owner Can Use it

@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)