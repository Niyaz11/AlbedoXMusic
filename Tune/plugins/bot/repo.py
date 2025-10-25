from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Tune import app
from config import BOT_USERNAME

repo_caption = """**
I'ᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇ ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ Mᴀɴʏ Fᴇᴀᴛᴜʀᴇs
Dɪᴛᴄʜ ᴛʜᴇ ᴛʜʀᴇᴀᴅs, ʟᴇᴛ's ᴠɪʙᴇ ᴛᴏ ᴛʜᴇ ʀʜʏᴛʜᴍ Jᴏɪɴ ᴍᴇ ᴏɴ Tᴇʟᴇɢʀᴀᴍ's ᴄᴜᴛᴇsᴛ ᴍᴜsɪᴄ ʙᴏᴛ.🎶

ɪꜰ ʏᴏᴜ ꜰᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ, ꜱᴇɴᴅ ꜱꜱ ɪɴ ꜱᴜᴘᴘᴏʀᴛ

sᴜᴘᴘᴏʀᴛ @EternalsHelplineBot
**"""

@app.on_message(filters.command("repo"))
async def show_repo(_, msg):
    buttons = [
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/EternalsHelplineBot"),
            InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/Anime_Chatting_Groups")
        ],
        [
            InlineKeyboardButton("ɴᴇᴛᴡᴏʀᴋ", url="https://t.me/AnimeNexusNetwork"),
            InlineKeyboardButton("ᴍᴏʀᴇ ʙᴏᴛs", url="https://t.me/AnimeNexusNetwork/160")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://files.catbox.moe/wu1bh0.jpg",
        caption=repo_caption,
        reply_markup=reply_markup
    )
