import pyrogram
import os
from pyrogram import filters
from pyrogram.types import Message, User
from pyrogram import Client as NaysaBots



       
       
   
  
@NaysaBots.on_message(filters.forwarded & filters.channel)
async def nstag(bot, message):
   try:
       chat_id = message.chat.id
       forward_msg = await message.copy(chat_id)
       await message.delete()
   except:
       await message.reply_text("Check My Admin Permissions and Try again")
    
