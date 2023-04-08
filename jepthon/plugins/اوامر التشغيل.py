import sys
from asyncio.exceptions import CancelledError
from time import sleep
import asyncio
from jepthon import jepiq

from ..core.logger import logging
from ..core.managers import edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID, HEROKU_APP

LOGS = logging.getLogger(__name__)
plugin_category = "tools"


@jepiq.ar_cmd(
    pattern="اعادة تشغيل$",
    command=("اعادة تشغيل", plugin_category),
    info={
        "header": "Restarts the bot !!",
        "usage": "{tr}restart",
    },
    disable_errors=True,
)
async def _(event):
    "Restarts the bot !!"
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "**⌔︙القرش ↻** \n" "**𓆝︙ تم اعادة تشغيل السورس بنجاح ✅ ↻**")
    lMl10l = await edit_or_reply(event, "𓆝︙ سيتم اعادة التشغيل انتظر ")
    await event.edit("0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    await asyncio.sleep(2)
    await event.edit("4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    await asyncio.sleep(2)
    await event.edit("8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    await asyncio.sleep(2)
    await event.edit("20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    await asyncio.sleep(2)
    await event.edit("36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    await asyncio.sleep(2)
    await event.edit("52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒")
    await asyncio.sleep(2)
    await event.edit("84%\n█████████████████████▒▒▒▒")
    await asyncio.sleep(2)
    await event.edit("100%\n████████████████████████")
    await asyncio.sleep(2)
    await event.edit("**𓆝︙ تم اعادة تشغيل بنجاح ✓ \nانتظر 2-5 دقائق**")
    await asyncio.sleep(2)
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
    try:
        add_to_collectionlist("restart_update", [lMl10l.chat_id, lMl10l.id])
    except Exception as e:
        LOGS.error(e)
    try:
        delgvar("ipaddress")
        await jepiq.disconnect()
    except CancelledError:
        pass
    except Exception as e:
        LOGS.error(e)


@jepiq.ar_cmd(
    pattern="اطفاء$",
    command=("اطفاء", plugin_category),
    info={
        "header": "Shutdowns the bot !!",
        "description": "To turn off the dyno of heroku. you cant turn on by bot you need to got to heroku and turn on or use @hk_heroku_bot",
        "usage": "{tr}shutdown",
    },
)
async def _(event):
    "Shutdowns the bot"
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "**𓆝︙ إيقاف التشغيـل ✕ **\n" "**𓆝︙ تـم إيقـاف تشغيـل البـوت بنجـاح ✓**")
    await edit_or_reply(event, "**𓆝︙ جـاري إيقـاف تشغيـل البـوت الآن ..**\n𓆝︙  **أعـد تشغيـلي يدويـاً لاحقـاً عـبر هيـروڪو ..**\n⌔︙**سيبقى البـوت متوقفـاً عن العمـل**")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)

@jepiq.ar_cmd(
    pattern="التحديثات (تشغيل|ايقاف)$",
    command=("التحديثات", plugin_category),
    info={
        "header": "𓆝︙ لتحديـث الدردشـة بعـد إعـادة التشغيـل  أو إعـادة التحميـل  ",
        "description": "⌔︙سيتـم إرسـال بنـك cmds ڪـرد على الرسالـة السابقـة الأخيـرة لـ (إعادة تشغيل/إعادة تحميل/تحديث cmds) 💡.",
        "usage": [
            "{tr}التحديثات <تشغيل/ايقاف",
        ],
    },
)
async def set_pmlog(event):
    "𓆝︙ لتحديـث الدردشـة بعـد إعـادة التشغيـل  أو إعـادة التحميـل  "
    input_str = event.pattern_match.group(1)
    if input_str == "ايقاف":
        if gvarstatus("restartupdate") is None:
            return await edit_delete(event, "**𓆝︙ تـم تعطيـل التـحديـثات بالفعـل ❗️**")
        delgvar("restartupdate")
        return await edit_or_reply(event, "**⌔︙تـم تعطيـل التـحديـثات بنجـاح ✓**")
    if gvarstatus("restartupdate") is None:
        addgvar("restartupdate", "turn-oned")
        return await edit_or_reply(event, "**⌔︙تـم تشغيل التـحديـثات بنجـاح ✓**")
    await edit_delete(event, "**𓆝︙ تـم تشغيل التـحديـثات بالفعـل ❗️**")
