from VegetaRobot import pgram as bot
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import *

SOURCE_IMAGE = "http://telegra.ph/file/e4781c5d359939627904d.jpg"

SOURCE_TEXT = """**Hello!  Searching for Vegeta's Repository?
We're kindly asking Vegeta have Some Errors! But it's Also have some good modules you can use your bots to are else you can run whole repository to your own! And We're Only helps you to fix common Errors Not at All! 

Vegeta's Codes Based On Some Different Bots Codes One More Times Thanks to All! (for using Vegeta/for helping Vegeta)

You can find Repository to using Below link.**
"""

SOURCE_BUTTONS = [[ InlineKeyboardButton(text="Repository Link", url="https://github.com/nandhaxd/VegetaRobot"),
                  ],[ InlineKeyboardButton(text="Contributors", callback_data="contributors")]]

@bot.on_message(filters.command(["repo","source"]))
async def repository(_, message):
        global user_id
        user_id = message.from_user.id
        await message.reply_photo(SOURCE_IMAGE,caption=SOURCE_TEXT,
        parse_mode=ParseMode.MARKDOWN,                      
        reply_markup=InlineKeyboardMarkup(SOURCE_BUTTONS))
       
CONTRIBUTORS = """
**CONTRIBUTORS**:

**Here the following list who's helpful for Make Vegeta's Repository!**

• [- 𝚁𝚊𝚑𝚞𝚕 𝙿 𝚁 -](t.me/itzme_rahul) 

**Thanks for you all Supporting Our Bots And We're happy to Say This!**
"""
@bot.on_callback_query(filters.regex("contributors"))
async def contributors(_, query):
      if query.from_user.id == user_id:
          return await query.message.edit_caption(CONTRIBUTORS,parse_mode=ParseMode.MARKDOWN)
      else: 
         await query.answer("This Message Not for You", show_alert=True)