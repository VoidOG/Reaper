import sys
from pymongo import MongoClient
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, CMD_HNDLR as hl
from os import execl
from telethon import events
from datetime import datetime

# MongoDB connection
mongo_client = MongoClient("mongodb+srv://Cenzo:Cenzo123@cenzo.azbk1.mongodb.net/")  # Adjust MongoDB URI if needed
db = mongo_client['bot_database']
sudo_users_collection = db['sudo_users']

# Function to get current sudo users from MongoDB
def get_sudo_users():
    sudo_users = sudo_users_collection.find_one({"_id": "sudo_users"})
    if sudo_users:
        return sudo_users.get('users', [])
    return []

# Function to update sudo users in MongoDB
def update_sudo_users(users):
    sudo_users_collection.update_one(
        {"_id": "sudo_users"},
        {"$set": {"users": users}},
        upsert=True
    )


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in get_sudo_users():
        start = datetime.now()
        jarvis = await e.reply(f"REAPER")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await jarvis.edit(f"[ʀᴇᴀᴘᴇʀ ɪꜱ ʀᴇᴀᴅʏ ᴛᴏ ʀᴇᴀᴘ ᴇᴠᴇʀʏᴏɴᴇ 👾](https://t.me/reaper_support)\n» `{mp} ᴍꜱ`")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in get_sudo_users():
        await e.reply(f"Reaper is starting.....")
        execl(sys.executable, sys.executable, *sys.argv)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply(f"New Sudo User added")
        target = ""
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("Reply on user  !!")
            return

        sudo_users = get_sudo_users()
        if str(target) in sudo_users:
            await ok.edit(f"Reaper Sudo User !!")
        else:
            sudo_users.append(str(target))
            update_sudo_users(sudo_users)
            await ok.edit(f"» **New Sudo User**: `{target}`")

    else:
        await event.reply("Only Owner can give sudo")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
async def removesudo(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply(f"Lund Chusle Owner ka...")
        target = ""
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("Reply to a message to remove the user.")
            return
        
        sudo_users = get_sudo_users()
        if str(target) not in sudo_users:
            await ok.edit("User is not in the sudo list.")
        else:
            sudo_users.remove(str(target))
            update_sudo_users(sudo_users)
            await ok.edit(f"Removed sudo user: `{target}`")

    else:
        await event.reply("Only owner can remove sudo users.")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
async def sudolist(event):
    if event.sender_id in get_sudo_users():
        sudo_users = get_sudo_users()
        sudo_list = "\n".join(sudo_users) if sudo_users else "No sudo users found."
        await event.reply(f"**Sudo Users List**:\n{sudo_list}")
