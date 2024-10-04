import asyncio
import psutil
from datetime import datetime
from config import X1, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from telethon import events

LOG_GROUP_ID = -1002183841044  # Log group ID for bot logs

@X1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(legend):
    if legend.sender_id == OWNER_ID:
        start = datetime.now()
        fetch = await legend.reply("__Fetching Bot and VPS Status...__")

        # Fetching bot and VPS status
        cpu_usage = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')
        bot_uptime = datetime.now() - start

        # Format uptime into hours, minutes, seconds
        uptime_seconds = int(bot_uptime.total_seconds())
        hours, remainder = divmod(uptime_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Get number of SUDO Users
        total_users = len(SUDO_USERS)

        log_content = "🔧 𝖵𝖯𝖲 𝖲𝗍𝖺𝗍𝗎𝗌 🔧\n\n"
        log_content += f" 𝖡𝗈𝗍 𝖴𝗉𝗍𝗂𝗆𝖾: `{hours}h {minutes}m {seconds}s`\n"
        log_content += f" 𝖢𝖯𝖴 𝖴𝗌𝖺𝗀𝖾: `{cpu_usage}%`\n"
        log_content += f" 𝖬𝖾𝗆𝗈𝗋𝗒 𝖴𝗌𝖺𝗀𝖾: `{memory_info.percent}%`\n"
        log_content += f" 𝖣𝗂𝗌𝗄 𝖴𝗌𝖺𝗀𝖾: `{disk_usage.percent}%`\n"
        log_content += f" 𝖭𝗎𝗆𝖻𝖾𝗋 𝗈𝖿 𝖲𝖴𝖣𝖮 𝖴𝗌𝖾𝗋𝗌: `{total_users}`\n\n"

        # Add current timestamp
        log_content += f"𝖳𝗂𝗆𝖾𝗌𝗍𝖺𝗆𝗉: `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`\n\n"

        # Adding SUDO Users with profile links
        log_content += "⦿ 𝖲𝖴𝖣𝖮 𝖴𝗌𝖾𝗋𝗌:\n"
        for user_id in SUDO_USERS:
            user_profile_link = f"tg://openmessage?user_id={user_id}"
            log_content += f"• [{user_id}]({user_profile_link})\n"

        # Send the logs to the log group
        try:
            await X1.send_message(LOG_GROUP_ID, log_content)
            await fetch.edit("𝖫𝗈𝗀𝗌 𝗌𝖾𝗇𝗍 𝗍𝗈 𝗍𝗁𝖾 𝗅𝗈𝗀 𝗀𝗋𝗈𝗎𝗉 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒!!")
        except Exception as e:
            await fetch.edit(f"❌ **An Exception Occurred!**\n\n**ERROR:** {str(e)}")

    elif legend.sender_id in SUDO_USERS:
        await legend.reply("🚫 » 𝖮𝗇𝗅𝗒 𝖮𝗐𝗇𝖾𝗋 𝖼𝖺𝗇 𝖺𝖼𝖼𝖾𝗌𝗌 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽!!")
