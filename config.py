import logging

from telethon import TelegramClient

from os import getenv
from OXYBOT.data import OXYGEN


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default="6636960153:AAE-I_EzI-B-c_xoAfk_kEsZAJKHNjhNH7s")
BOT_TOKEN2 = getenv("BOT_TOKEN2", default="6973619618:AAERC40Khl5U8UM3wKOJoDbCnK7yUEvCl88")
BOT_TOKEN3 = getenv("BOT_TOKEN3", default="6372495588:AAFJTPJ4zthJHET_0YGVF2ch8hvfaEn0cLY")
BOT_TOKEN4 = getenv("BOT_TOKEN4", default="6469472885:AAESzwiDkJay02o6hvEIfGjY05zxORdHiA4")
BOT_TOKEN5 = getenv("BOT_TOKEN5", default="7032578227:AAGjf_V1ZIV_W4BSIykYNNikKK_UAjnadm8")
BOT_TOKEN6 = getenv("BOT_TOKEN6", default="7007795486:AAHKpZJcgL5dr2qdVT_MCD_fVLWEDIZveq0")
BOT_TOKEN7 = getenv("BOT_TOKEN7", default="7160410112:AAE3Hx4N8zsNs_h9LLwQN2iSOZfKJPuUGeQ")
BOT_TOKEN8 = getenv("BOT_TOKEN8", default="5802395579:AAE5klWOOz3rbft0L32B5HSHO9PnJTg4QM8")
BOT_TOKEN9 = getenv("BOT_TOKEN9", default="5802395579:AAE5klWOOz3rbft0L32B5HSHO9PnJTg4QM8")
BOT_TOKEN10 = getenv("BOT_TOKEN10", default="5802395579:AAE5klWOOz3rbft0L32B5HSHO9PnJTg4QM8")

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="6551446148 7752022981 7633073399 6497946619 1977918659 6946715424 6589879577 6787993615  6730517246 5269893269 6455590065 5269893269 6975633027 6951750255 7008340745 6913928646 6552389144 6974802421 6229500355 7039337017 6788996816 5798892219 5350097210 5980074706 7163357187 6951777422 2108102800 6394476577 6731047041 6541098533 6334111685 7095814705 1184463729 6382216159 6481726308 6837090390 6643029630 6997261710 6946715424 6815088777 6753234881 7469343986 7261874964 6698364560 1110013191 5424613374 6689654756 5782133057 6312774570 7092676507 7352925204").split()))
for x in OXYGEN:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6663845789"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
