import os
import re
from telethon import events, Button
from telethon import TelegramClient, events
from telethon.tl import functions
import telethon as tbot
from Config import SUDO_USERS

PHOTO = "https://te.legra.ph/file/d3d7861305fe0b833fa11.jpg"

async def awake(event):
  TEXT = f"𝐇𝐈 [{event.sender.first_name}](tg://user?id={event.sender.id}), 𝐈'𝐌 𝐀𝐋𝐄𝐗𝐀 \n\n"
  TEXT += "✨ 𝐈'𝐌 𝐖𝐎𝐑𝐊𝐈𝐍𝐆 𝐏𝐑𝐎𝐏𝐄𝐑𝐋𝐘 \n\n"
  TEXT += f"✨ 𝐎𝐖𝐍𝐄𝐑 ☞︎︎︎ [𝐑𝐎𝐘𝐀𝐋 𝐊𝐈𝐍𝐆](https://t.me/R0Y41_KING) \n\n"
  TEXT += f"✨ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 ☞︎︎︎ [𝐉𝐎𝐈𝐍](https://t.me/DARKAMANSUPPORT) \n\n"
  TEXT += f"✨ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ☞︎︎︎ [𝐉𝐎𝐈𝐍](https://t.me/DARKAMANCHANNEL) \n\n"
  TEXT += "𝐓𝐇𝐀𝐍𝐊𝐒 𝐅𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐄 𝐇𝐄𝐑𝐄 ❤️"
  BUTTON = [[Button.url("༎⃝✨𝐇𝐄𝐋𝐏༎⃝➤", "https://t.me/ALEXA_ROBOT_ROBOT?start=help"), Button.url("༎⃝🌺 𝐒𝐔𝐏𝐏𝐎𝐑𝐓༎⃝➤", "https://t.me/DARKAMANSUPPORT")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)

@alive.on(events.NewMessage(incoming=True, pattern=r"\*alive"))
