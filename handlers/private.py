from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAECyw9hI11WAc0e3ijfjWbk1o6Ot2qkBgACDgADBxSGH0BLwmepu3YDIAQ")
    await message.reply_text(
        f"""**- 𝙃𝙚𝙮 𝘼𝙢 {bn} 💛🐬,

- 𝙄 𝙘𝙖𝙣 𝙥𝙡𝙖𝙮 𝙢𝙪𝙨𝙞𝙘 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥'𝙨 𝙫𝙤𝙞𝙘𝙚 𝙘𝙖𝙡𝙡. 𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙙 𝙗𝙮 [𝙈𝘼𝙃𝙄](https://t.me/ALONE_BOY_XD_01) 💛🤞.

𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥 𝙖𝙣𝙙 𝙥𝙡𝙖𝙮 𝙢𝙪𝙨𝙞𝙘 𝙛𝙧𝙚𝙚𝙡𝙮 🐬💕**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         " 𝙊𝙬𝙣𝙚𝙧 ", url="https://t.me/ALONE_BOY_XD_01")
                  ],[
                    InlineKeyboardButton(
                        "💬 𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url="https://t.me/shivamdemon"
                    ),
                    InlineKeyboardButton(
                        "🔊 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url="https://t.me/BESTIES_FOREVER_LOVE"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ 𝘼𝙙𝙙 𝙏𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 ➕", url="https://t.me/LEGEND_ALONE_MUSIC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** 𝘼𝙡𝙤𝙣𝙚 𝙈𝙪𝙨𝙞𝙘 𝙋𝙡𝙖𝙮𝙚𝙧 𝙄𝙨 𝙊𝙣𝙡𝙞𝙣𝙚 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url="https://t.me/BESTIES_FOREVER_LOVE")
                ]
            ]
        )
   )


