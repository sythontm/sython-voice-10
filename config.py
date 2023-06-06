from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
AIP_ID = os.environ.get("AIP_ID")
AIP_HASH = os.environ.get("AIP_HASH")

BIP_ID = os.environ.get("BIP_ID")
BIP_HASH = os.environ.get("BIP_HASH")


CIP_ID = os.environ.get("CIP_ID")
CIP_HASH = os.environ.get("CIP_HASH")


DIP_ID = os.environ.get("DIP_ID")
DIP_HASH = os.environ.get("DIP_HASH")

EIP_ID = os.environ.get("EIP_ID")
EIP_HASH = os.environ.get("EIP_HASH")

FIP_ID = os.environ.get("FIP_ID")
FIP_HASH = os.environ.get("FIP_HASH")

GIP_ID = os.environ.get("GIP_ID")
GIP_HASH = os.environ.get("GIP_HASH")

HIP_ID = os.environ.get("HIP_ID")
HIP_HASH = os.environ.get("HIP_HASH")

IIP_ID = os.environ.get("IIP_ID")
IIP_HASH = os.environ.get("IIP_HASH")

JIP_ID = os.environ.get("JIP_ID")
JIP_HASH = os.environ.get("JIP_HASH")

CHNA = os.environ.get("ZCHNA")

BOT_USERNAME = os.environ.get("BOT_USERNAME")
session1 = os.environ.get("ATERMUX")
SESSION1 = os.environ.get("ATERMUX")
token = os.environ.get("TOKEN")
DEVLOO = os.environ.get("ZDEVLO")

sython1 = TelegramClient(StringSession(session1), AIP_ID, AIP_HASH)
bot = TelegramClient("bot", AIP_ID, AIP_HASH).start(bot_token=token)


session2 = os.environ.get("BTERMUX")
SESSION2 = os.environ.get("BTERMUX")
sython2 = TelegramClient(StringSession(session2), BIP_ID, BIP_HASH)


session3 = os.environ.get("CTERMUX")
SESSION3 = os.environ.get("CTERMUX")
sython3 = TelegramClient(StringSession(session3), CIP_ID, CIP_HASH)


session4 = os.environ.get("DTERMUX")
SESSION4 = os.environ.get("DTERMUX")
sython4 = TelegramClient(StringSession(session4), DIP_ID, DIP_HASH)


session5 = os.environ.get("ETERMUX")
SESSION5 = os.environ.get("ETERMUX")
sython5 = TelegramClient(StringSession(session5), EIP_ID, EIP_HASH)

session6 = os.environ.get("FTERMUX")
SESSION6 = os.environ.get("FTERMUX")
sython6 = TelegramClient(StringSession(session6), FIP_ID, FIP_HASH)


session7 = os.environ.get("GTERMUX")
SESSION7 = os.environ.get("GTERMUX")
sython7 = TelegramClient(StringSession(session7), GIP_ID, GIP_HASH)

session8 = os.environ.get("HTERMUX")
SESSION8 = os.environ.get("HTERMUX")
sython8 = TelegramClient(StringSession(session8), HIP_ID, HIP_HASH)

session9 = os.environ.get("ITERMUX")
SESSION9 = os.environ.get("ITERMUX")
sython9 = TelegramClient(StringSession(session9), IIP_ID, IIP_HASH)

session10 = os.environ.get("JTERMUX")
SESSION10 = os.environ.get("JTERMUX")
sython10 = TelegramClient(StringSession(session10), JIP_ID, JIP_HASH)


ispay = ['yes']
ispay2 = ['yes']
bot.start()

