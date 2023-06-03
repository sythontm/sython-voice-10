from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests

sython1.start()
sython2.start()
sython3.start()
sython4.start()
sython5.start()
sython6.start()
sython7.start()
sython8.start()
sython9.start()
sython10.start()

c = requests.session()
ownerhson_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [5159123009]
ownerhson_idd = 5159123009
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass        
        
        
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@SY_TEM"))
    except BaseException:
        pass        
        
      
@sython2.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython2(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass        
        
        
        
@sython2.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython2(JoinChannelRequest("@SY_TEM"))
    except BaseException:
        pass        
  
  
@sython3.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython3(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass        
        
        
        
@sython3.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython3(JoinChannelRequest("@SY_TEM"))
    except BaseException:
        pass        
  


@sython4.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython4(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass        
        
        
        
@sython4.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython4(JoinChannelRequest("@SY_TEM"))
    except BaseException:
        pass   

@sython5.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython5(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass        
        
        
        
@sython5.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython5(JoinChannelRequest("@SY_TEM"))
    except BaseException:
        pass     



@sython6.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython6(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass        
        
        
        
@sython6.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython6(JoinChannelRequest("@SY_TEM"))
    except BaseException:
        pass        
        
      
@sython7.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython7(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass        
        
        
        
@sython7.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython7(JoinChannelRequest("@SY_TEM"))
    except BaseException:
        pass        
  
  
@sython8.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython8(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass        
        
        
        
@sython8.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython8(JoinChannelRequest("@SY_TEM"))
    except BaseException:
        pass        
  


@sython9.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython9(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass        
        
        
        
@sython9.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython9(JoinChannelRequest("@SY_TEM"))
    except BaseException:
        pass   

@sython10.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython10(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass        
        
        
        
@sython10.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython10(JoinChannelRequest("@SY_TEM"))
    except BaseException:
        pass     
        
        
        
    
@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice1 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')


@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice2 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice3 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice4 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice5 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')


@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice2 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice3 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice4 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice5 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')


@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')



@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice3 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice4 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice5 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')


@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice3 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice4 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice5 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')


@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')



@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice4 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')

@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice5 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')

@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')

@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')

@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')

@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')


@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')



@sython5.on(events.NewMessage(outgoing=False, pattern='^/voice5 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython5.get_entity(chn)
        join = await sython5(JoinChannelRequest(chn))
        joion = await sython5(JoinChannelRequest('saythonh'))
        somy = await sython5.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython5.send_message(CHNA,'**Done Send Voice**')

@sython5.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython5.get_entity(chn)
        join = await sython5(JoinChannelRequest(chn))
        joion = await sython5(JoinChannelRequest('saythonh'))
        somy = await sython5.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython5.send_message(CHNA,'**Done Send Voice**')

@sython5.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython5.get_entity(chn)
        join = await sython5(JoinChannelRequest(chn))
        joion = await sython5(JoinChannelRequest('saythonh'))
        somy = await sython5.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython5.send_message(CHNA,'**Done Send Voice**')

@sython5.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython5.get_entity(chn)
        join = await sython5(JoinChannelRequest(chn))
        joion = await sython5(JoinChannelRequest('saythonh'))
        somy = await sython5.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython5.send_message(CHNA,'**Done Send Voice**')

@sython5.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython5.get_entity(chn)
        join = await sython5(JoinChannelRequest(chn))
        joion = await sython5(JoinChannelRequest('saythonh'))
        somy = await sython5.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython5.send_message(CHNA,'**Done Send Voice**')


@sython5.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython5.get_entity(chn)
        join = await sython5(JoinChannelRequest(chn))
        joion = await sython5(JoinChannelRequest('saythonh'))
        somy = await sython5.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython5.send_message(CHNA,'**Done Send Voice**')




@sython6.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython6.get_entity(chn)
        join = await sython6(JoinChannelRequest(chn))
        joion = await sython6(JoinChannelRequest('saythonh'))
        somy = await sython6.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython6.send_message(CHNA,'**Done Send Voice**')

@sython6.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython6.get_entity(chn)
        join = await sython6(JoinChannelRequest(chn))
        joion = await sython6(JoinChannelRequest('saythonh'))
        somy = await sython6.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython6.send_message(CHNA,'**Done Send Voice**')

@sython6.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython6.get_entity(chn)
        join = await sython6(JoinChannelRequest(chn))
        joion = await sython6(JoinChannelRequest('saythonh'))
        somy = await sython6.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython6.send_message(CHNA,'**Done Send Voice**')

@sython6.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython6.get_entity(chn)
        join = await sython6(JoinChannelRequest(chn))
        joion = await sython6(JoinChannelRequest('saythonh'))
        somy = await sython6.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython6.send_message(CHNA,'**Done Send Voice**')


@sython6.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython6.get_entity(chn)
        join = await sython6(JoinChannelRequest(chn))
        joion = await sython6(JoinChannelRequest('saythonh'))
        somy = await sython6.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython6.send_message(CHNA,'**Done Send Voice**')






@sython7.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython7.get_entity(chn)
        join = await sython7(JoinChannelRequest(chn))
        joion = await sython7(JoinChannelRequest('saythonh'))
        somy = await sython7.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython7.send_message(CHNA,'**Done Send Voice**')

@sython7.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython7.get_entity(chn)
        join = await sython7(JoinChannelRequest(chn))
        joion = await sython7(JoinChannelRequest('saythonh'))
        somy = await sython7.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython7.send_message(CHNA,'**Done Send Voice**')

@sython7.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython7.get_entity(chn)
        join = await sython7(JoinChannelRequest(chn))
        joion = await sython7(JoinChannelRequest('saythonh'))
        somy = await sython7.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython7.send_message(CHNA,'**Done Send Voice**')


@sython7.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython7.get_entity(chn)
        join = await sython7(JoinChannelRequest(chn))
        joion = await sython7(JoinChannelRequest('saythonh'))
        somy = await sython7.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython7.send_message(CHNA,'**Done Send Voice**')






@sython8.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython8.get_entity(chn)
        join = await sython8(JoinChannelRequest(chn))
        joion = await sython8(JoinChannelRequest('saythonh'))
        somy = await sython8.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython8.send_message(CHNA,'**Done Send Voice**')

@sython8.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython8.get_entity(chn)
        join = await sython8(JoinChannelRequest(chn))
        joion = await sython8(JoinChannelRequest('saythonh'))
        somy = await sython8.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython8.send_message(CHNA,'**Done Send Voice**')


@sython8.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython8.get_entity(chn)
        join = await sython8(JoinChannelRequest(chn))
        joion = await sython8(JoinChannelRequest('saythonh'))
        somy = await sython8.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython8.send_message(CHNA,'**Done Send Voice**')







@sython9.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython9.get_entity(chn)
        join = await sython9(JoinChannelRequest(chn))
        joion = await sython9(JoinChannelRequest('saythonh'))
        somy = await sython9.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython9.send_message(CHNA,'**Done Send Voice**')


@sython9.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython9.get_entity(chn)
        join = await sython9(JoinChannelRequest(chn))
        joion = await sython9(JoinChannelRequest('saythonh'))
        somy = await sython9.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython9.send_message(CHNA,'**Done Send Voice**')


@sython10.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython10.get_entity(chn)
        join = await sython10(JoinChannelRequest(chn))
        joion = await sython10(JoinChannelRequest('saythonh'))
        somy = await sython10.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython10.send_message(CHNA,'**Done Send Voice**')


#####
@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice1 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')


@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice2 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice3 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice4 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice5 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')


@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice2 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice3 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice4 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice5 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')

@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')


@sython2.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython2.get_entity(chn)
        join = await sython2(JoinChannelRequest(chn))
        joion = await sython2(JoinChannelRequest('saythonh'))
        somy = await sython2.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython2.send_message(CHNA,'**Done Send Voice**')



@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice3 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice4 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice5 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')


@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice3 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice4 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice5 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')

@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')


@sython3.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython3.get_entity(chn)
        join = await sython3(JoinChannelRequest(chn))
        joion = await sython3(JoinChannelRequest('saythonh'))
        somy = await sython3.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython3.send_message(CHNA,'**Done Send Voice**')



@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice4 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')

@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice5 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')

@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')

@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')

@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')

@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')


@sython4.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython4.get_entity(chn)
        join = await sython4(JoinChannelRequest(chn))
        joion = await sython4(JoinChannelRequest('saythonh'))
        somy = await sython4.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython4.send_message(CHNA,'**Done Send Voice**')



@sython5.on(events.NewMessage(outgoing=False, pattern='^/voice5 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython5.get_entity(chn)
        join = await sython5(JoinChannelRequest(chn))
        joion = await sython5(JoinChannelRequest('saythonh'))
        somy = await sython5.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython5.send_message(CHNA,'**Done Send Voice**')

@sython5.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython5.get_entity(chn)
        join = await sython5(JoinChannelRequest(chn))
        joion = await sython5(JoinChannelRequest('saythonh'))
        somy = await sython5.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython5.send_message(CHNA,'**Done Send Voice**')

@sython5.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython5.get_entity(chn)
        join = await sython5(JoinChannelRequest(chn))
        joion = await sython5(JoinChannelRequest('saythonh'))
        somy = await sython5.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython5.send_message(CHNA,'**Done Send Voice**')

@sython5.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython5.get_entity(chn)
        join = await sython5(JoinChannelRequest(chn))
        joion = await sython5(JoinChannelRequest('saythonh'))
        somy = await sython5.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython5.send_message(CHNA,'**Done Send Voice**')

@sython5.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython5.get_entity(chn)
        join = await sython5(JoinChannelRequest(chn))
        joion = await sython5(JoinChannelRequest('saythonh'))
        somy = await sython5.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython5.send_message(CHNA,'**Done Send Voice**')


@sython5.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython5.get_entity(chn)
        join = await sython5(JoinChannelRequest(chn))
        joion = await sython5(JoinChannelRequest('saythonh'))
        somy = await sython5.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython5.send_message(CHNA,'**Done Send Voice**')




@sython6.on(events.NewMessage(outgoing=False, pattern='^/voice6 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython6.get_entity(chn)
        join = await sython6(JoinChannelRequest(chn))
        joion = await sython6(JoinChannelRequest('saythonh'))
        somy = await sython6.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython6.send_message(CHNA,'**Done Send Voice**')

@sython6.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython6.get_entity(chn)
        join = await sython6(JoinChannelRequest(chn))
        joion = await sython6(JoinChannelRequest('saythonh'))
        somy = await sython6.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython6.send_message(CHNA,'**Done Send Voice**')

@sython6.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython6.get_entity(chn)
        join = await sython6(JoinChannelRequest(chn))
        joion = await sython6(JoinChannelRequest('saythonh'))
        somy = await sython6.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython6.send_message(CHNA,'**Done Send Voice**')

@sython6.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython6.get_entity(chn)
        join = await sython6(JoinChannelRequest(chn))
        joion = await sython6(JoinChannelRequest('saythonh'))
        somy = await sython6.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython6.send_message(CHNA,'**Done Send Voice**')


@sython6.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython6.get_entity(chn)
        join = await sython6(JoinChannelRequest(chn))
        joion = await sython6(JoinChannelRequest('saythonh'))
        somy = await sython6.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython6.send_message(CHNA,'**Done Send Voice**')






@sython7.on(events.NewMessage(outgoing=False, pattern='^/voice7 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython7.get_entity(chn)
        join = await sython7(JoinChannelRequest(chn))
        joion = await sython7(JoinChannelRequest('saythonh'))
        somy = await sython7.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython7.send_message(CHNA,'**Done Send Voice**')

@sython7.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython7.get_entity(chn)
        join = await sython7(JoinChannelRequest(chn))
        joion = await sython7(JoinChannelRequest('saythonh'))
        somy = await sython7.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython7.send_message(CHNA,'**Done Send Voice**')

@sython7.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython7.get_entity(chn)
        join = await sython7(JoinChannelRequest(chn))
        joion = await sython7(JoinChannelRequest('saythonh'))
        somy = await sython7.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython7.send_message(CHNA,'**Done Send Voice**')


@sython7.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython7.get_entity(chn)
        join = await sython7(JoinChannelRequest(chn))
        joion = await sython7(JoinChannelRequest('saythonh'))
        somy = await sython7.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython7.send_message(CHNA,'**Done Send Voice**')






@sython8.on(events.NewMessage(outgoing=False, pattern='^/voice8 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython8.get_entity(chn)
        join = await sython8(JoinChannelRequest(chn))
        joion = await sython8(JoinChannelRequest('saythonh'))
        somy = await sython8.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython8.send_message(CHNA,'**Done Send Voice**')

@sython8.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython8.get_entity(chn)
        join = await sython8(JoinChannelRequest(chn))
        joion = await sython8(JoinChannelRequest('saythonh'))
        somy = await sython8.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython8.send_message(CHNA,'**Done Send Voice**')


@sython8.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython8.get_entity(chn)
        join = await sython8(JoinChannelRequest(chn))
        joion = await sython8(JoinChannelRequest('saythonh'))
        somy = await sython8.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython8.send_message(CHNA,'**Done Send Voice**')







@sython9.on(events.NewMessage(outgoing=False, pattern='^/voice9 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython9.get_entity(chn)
        join = await sython9(JoinChannelRequest(chn))
        joion = await sython9(JoinChannelRequest('saythonh'))
        somy = await sython9.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython9.send_message(CHNA,'**Done Send Voice**')


@sython9.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython9.get_entity(chn)
        join = await sython9(JoinChannelRequest(chn))
        joion = await sython9(JoinChannelRequest('saythonh'))
        somy = await sython9.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython9.send_message(CHNA,'**Done Send Voice**')


@sython10.on(events.NewMessage(outgoing=False, pattern='^/voice10 (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_idd:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython10.get_entity(chn)
        join = await sython10(JoinChannelRequest(chn))
        joion = await sython10(JoinChannelRequest('saythonh'))
        somy = await sython10.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython10.send_message(CHNA,'**Done Send Voice**')

#work1206
sython1.run_until_disconnected()
sython2.run_until_disconnected()
sython3.run_until_disconnected()
sython4.run_until_disconnected()
sython5.run_until_disconnected()
sython6.run_until_disconnected()
sython7.run_until_disconnected()
sython8.run_until_disconnected()
sython9.run_until_disconnected()
sython10.run_until_disconnected()
