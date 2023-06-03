from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")

CHNA = os.environ.get("CHNA")

APP_IDD = os.environ.get("APP_IDD")
APP_HASHH = os.environ.get("APP_HASHH")


BOT_USERNAME = os.environ.get("BOT_USERNAME")
session1 = os.environ.get("TERMUXA")
SESSION1 = os.environ.get("TERMUXA")
token = os.environ.get("TOKEN")
DEVLOO = os.environ.get("DEVLO")

sython1 = TelegramClient(StringSession(session1), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)


session2 = os.environ.get("TERMUXB")
SESSION2 = os.environ.get("TERMUXB")
sython2 = TelegramClient(StringSession(session2), APP_ID, APP_HASH)


session3 = os.environ.get("TERMUXC")
SESSION3 = os.environ.get("TERMUXC")
sython3 = TelegramClient(StringSession(session3), APP_ID, APP_HASH)


session4 = os.environ.get("TERMUXD")
SESSION4 = os.environ.get("TERMUXD")
sython4 = TelegramClient(StringSession(session4), APP_ID, APP_HASH)


session5 = os.environ.get("TERMUXE")
SESSION5 = os.environ.get("TERMUXE")
sython5 = TelegramClient(StringSession(session5), APP_ID, APP_HASH)

session6 = os.environ.get("TERMUXF")
SESSION6 = os.environ.get("TERMUXF")
sython6 = TelegramClient(StringSession(session6), APP_IDD, APP_HASHH)


session7 = os.environ.get("TERMUXG")
SESSION7 = os.environ.get("TERMUXG")
sython7 = TelegramClient(StringSession(session7), APP_IDD, APP_HASHH)

session8 = os.environ.get("TERMUXH")
SESSION8 = os.environ.get("TERMUXH")
sython8 = TelegramClient(StringSession(session8), APP_IDD, APP_HASHH)

session9 = os.environ.get("TERMUXI")
SESSION9 = os.environ.get("TERMUXI")
sython9 = TelegramClient(StringSession(session9), APP_IDD, APP_HASHH)

session10 = os.environ.get("TERMUXJ")
SESSION10 = os.environ.get("TERMUXJ")
sython10 = TelegramClient(StringSession(session10), APP_IDD, APP_HASHH)


ispay = ['yes']
ispay2 = ['yes']
bot.start()

