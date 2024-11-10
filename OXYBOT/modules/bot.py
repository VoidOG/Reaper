import sys
import heroku3
from pymongo import MongoClient
from config import (
    X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, MONGO_DB_URL, CMD_HNDLR as hl
)
from os import execl
from telethon import events
from datetime import datetime

# MongoDB Client
client = MongoClient(MONGO_DB_URL)
db = client["reaper_bot"]
sudo_collection = db["sudo_users"]

def get_sudo_users():
    """Fetch sudo users from MongoDB."""
    sudo_users = sudo_collection.find_one({"_id": "sudo_list"})
    return sudo_users.get("users", []) if sudo_users else []

def add_sudo_user(user_id):
    """Add a new sudo user to MongoDB."""
    sudo_collection.update_one(
        {"_id": "sudo_list"},
        {"$addToSet": {"users": user_id}},
        upsert=True
    )

def remove_sudo_user(user_id):
    """Remove a sudo user from MongoDB."""
    sudo_collection.update_one(
        {"_id": "sudo_list"},
        {"$pull": {"users": user_id}}
    )

# Ping Command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))

async def ping(e):
    if e.sender_id in get_sudo_users():
        start = datetime.now()
        jarvis = await e.reply("ʀᴇᴀᴘᴇʀ ɪꜱ ʀᴇᴀᴅʏ ᴛᴏ ʀᴀᴘᴇ ᴇᴠᴇʀʏᴏɴᴇ")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await jarvis.edit(f"[ʀᴇᴀᴘᴇʀ ɪꜱ ʀᴇᴀᴅʏ ᴛᴏ ʀᴀᴘᴇ ᴇᴠᴇʀʏᴏɴᴇ 👾](https://t.me/Reaper_Support)\n» `{mp} ᴍꜱ`")

# Reboot Command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in get_sudo_users():
        await e.reply("Reaper is starting...")
        # Disconnect clients before restarting
        for client in [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]:
            try:
                await client.disconnect()
            except Exception:
                pass
        execl(sys.executable, sys.executable, *sys.argv)

# Add Sudo Command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        reply_msg = await event.get_reply_message()
        if reply_msg:
            target_id = reply_msg.sender_id
            if target_id not in get_sudo_users():
                add_sudo_user(target_id)
                await event.reply(f"New sudo user added: `{target_id}`")
            else:
                await event.reply("User is already a sudo user.")
        else:
            await event.reply("Reply to a user's message to add them as sudo.")
    else:
        await event.reply("Only the owner can add sudo users.")

# Remove Sudo Command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
async def removesudo(event):
    if event.sender_id == OWNER_ID:
        reply_msg = await event.get_reply_message()
        if reply_msg:
            target_id = reply_msg.sender_id
            if target_id in get_sudo_users():
                remove_sudo_user(target_id)
                await event.reply(f"Sudo user removed: `{target_id}`")
            else:
                await event.reply("User is not in the sudo list.")
        else:
            await event.reply("Reply to a user's message to remove them from sudo.")
    else:
        await event.reply("Only the owner can remove sudo users.")

# List Sudo Users
@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
async def list_sudos(event):
    if event.sender_id in get_sudo_users():
        sudo_users = get_sudo_users()
        users_list = "\n".join([f"- `{user}`" for user in sudo_users])
        await event.reply(f"Current sudo users:\n{users_list}")
    else:
        await event.reply("Only sudo users can view the sudo list.")

