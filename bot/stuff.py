#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`\nThis is A CompressorQueue Which Can Encode Videos.\nReduce Size of Videos With Negligible Quality Change\nU can Generate Samples/screenshots too.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("CHANNEL", url="t.me/animes_encoded"),
                Button.url("BOSS", url="t.me/Bro_isDarkal"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**🥇 Fastest Encoding Bot Used By @Animes_Encoded**\n\n+This Bot Encodes Videos With Negligible Quality Change.\n+Generate Sample Compressed Video To check Quality\n+Easy to Use\n+This Bot is fast as fek and it gives files encoded in 480p.\nSo Its not for public use! Nd join @Anime_Encoded.\nDont Spam Bot.\n\nEnjoy!",
    )
