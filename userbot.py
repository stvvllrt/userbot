from pyrogram import Client, filters
from datetime import datetime, timedelta
from pyrogram.types import ChatPermissions
from pyrogram import enums

app = Client("my_account")

#heeeeeeeeeeeeeeeeeelp

@app.on_message(filters.chat("vk_tea_chat"))
async def hello(client, message):
    user_id = message.from_user.id
    if str(user_id) == "5628179702":
        msg = message.text
        msg = msg.split()
        if msg[0] == ".tmute":
            await app.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id ,ChatPermissions(can_send_messages=False), datetime.now() + timedelta(hours=int(msg[1])))
        if msg[0] == ".pardon":
            await app.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id ,ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_add_web_page_previews=True,can_send_other_messages=True,can_send_polls=True)) 
app.run()