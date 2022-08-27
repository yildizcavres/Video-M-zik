import yt_dlp
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaAudio,
                            InputMediaDocument, InputMediaVideo, Message)


def YT_info(yturl):
    ydl = yt_dlp.YoutubeDL()
    with ydl:
        formats_available = []
        r = ydl.extract_info(yturl, download=False)
        for format in r["formats"]:
            # Filter dash video(without audio)
            if not "dash" in str(format["format"]).lower():
                formats_available.append(
                    {
                        "format": format["format"],
                        "filesize": format["filesize"],
                        "format_id": format["format_id"],
                        "yturl": yturl,
                    }
                )

        return formats_available


def humanbytes(num, suffix="B"):
    if num is None:
        num = 0
    else:
        num = int(num)

    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, "Yi", suffix)


async def get_formats(CallbackQuery, videoid, user_id, type):
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        formats = YT_info(url)
    except Exception:
        return await CallbackQuery.message.reply_text(
            "Yt'den Veri Alınamadı...YTDL sorunu olabilir."
        )
    j = 0
    for x in formats:
        check = x["format"]
        if type == "audio":
            if "audio" in check:
                j += 1
                if j == 4:
                    a4 = InlineKeyboardButton(
                        text=f"ᴋᴀʟɪᴛᴇ: ᴅᴜ̈şᴜ̈ᴋ",
                        callback_data=f"ytdata audio||{x['format_id']}||{videoid}",
                    )
                if j == 5:
                    a5 = InlineKeyboardButton(
                        text=f"ᴋᴀʟɪᴛᴇ: ᴏʀᴛᴀ",
                        callback_data=f"ytdata audio||{x['format_id']}||{videoid}",
                    )
                if j == 6:
                    a6 = InlineKeyboardButton(
                        text=f"ᴋᴀʟɪᴛᴇ: ʏᴜ̈ᴋsᴇᴋ",
                        callback_data=f"ytdata audio||{x['format_id']}||{videoid}",
                    )
        elif type == "video":
            if str(135) in check:
                j += 1
                a3 = InlineKeyboardButton(
                    text=f"ᴋᴀʟɪᴛᴇ: (480)p",
                    callback_data=f"ytdata video||{x['format_id']}||{videoid}",
                )
            if str(136) in check:
                j += 1
                a4 = InlineKeyboardButton(
                    text=f"ᴋᴀʟɪᴛᴇ: (720)p",
                    callback_data=f"ytdata video||{x['format_id']}||{videoid}",
                )
            if str(137) in check:
                j += 1
                a5 = InlineKeyboardButton(
                    text=f"ᴋᴀʟɪᴛᴇ: (1080)p",
                    callback_data=f"ytdata video||{x['format_id']}||{videoid}",
               )
        else:
            return await CallbackQuery.message.reply_text(
                "𝗩𝗶𝗱𝗲𝗼 𝗙𝗼𝗿𝗺𝗮𝘁𝗹𝗮𝗿𝗶 𝗕𝘂𝗹𝘂𝗻𝗮𝗺𝗮𝗱𝗶. 𝗗𝗶𝗴̆𝗲𝗿 𝗠𝘂̈𝘇𝗶𝗸𝗹𝗲𝗿𝗶 𝗔𝗿𝗮𝗺𝗮𝘆𝗶 𝗗𝗲𝗻𝗲"
            )
    if j == 0:
        return await CallbackQuery.message.reply_text(
            "𝗩𝗶𝗱𝗲𝗼 𝗙𝗼𝗿𝗺𝗮𝘁𝗹𝗮𝗿𝗶 𝗕𝘂𝗹𝘂𝗻𝗮𝗺𝗮𝗱𝗶. 𝗗𝗶𝗴̆𝗲𝗿 𝗠𝘂̈𝘇𝗶𝗸𝗹𝗲𝗿𝗶 𝗔𝗿𝗮𝗺𝗮𝘆𝗶 𝗗𝗲𝗻𝗲"
        )
    elif j == 1:
        key = InlineKeyboardMarkup(
            [
                [
                    a1,
                ],
                [
                    InlineKeyboardButton(
                        text="🔙 Geri",
                        callback_data=f"good {videoid}|{user_id}",
                    ),
                    InlineKeyboardButton(
                        text="🗑 Menüyü Kapat", callback_data=f"close2"
                    ),
                ],
            ]
        )
    elif j == 2:
        key = InlineKeyboardMarkup(
            [
                [
                    a1,
                    a2,
                ],
                [
                    InlineKeyboardButton(
                        text="⇠ Geri Git",
                        callback_data=f"good {videoid}|{user_id}",
                    ),
                    InlineKeyboardButton(
                        text="🗑 Menüyü Kapat", callback_data=f"close2"
                    ),
                ],
            ]
        )
    elif j == 3:
        key = InlineKeyboardMarkup(
            [
                [
                    a1,
                    a2,
                ],
                [
                    a3,
                ],
                [
                    InlineKeyboardButton(
                        text="⇠ Geri Git",
                        callback_data=f"good {videoid}|{user_id}",
                    ),
                    InlineKeyboardButton(
                        text="🗑 Menüyü Kapat", callback_data=f"close2"
                    ),
                ],
            ]
        )
    elif j == 4:
        key = InlineKeyboardMarkup(
            [
                [
                    a1,
                    a2,
                ],
                [
                    a3,
                    a4,
                ],
                [
                    InlineKeyboardButton(
                        text="⇠ Geri Git",
                        callback_data=f"good {videoid}|{user_id}",
                    ),
                    InlineKeyboardButton(
                        text="🗑 Menüyü Kapat", callback_data=f"close2"
                    ),
                ],
            ]
        )
    elif j == 5:
        key = InlineKeyboardMarkup(
            [
                [
                    a1,
                    a2,
                ],
                [
                    a3,
                    a4,
                ],
                [
                    a5,
                ],
                [
                    InlineKeyboardButton(
                        text="⇠ Geri Git",
                        callback_data=f"good {videoid}|{user_id}",
                    ),
                    InlineKeyboardButton(
                        text="🗑 Menüyü Kapat", callback_data=f"close2"
                    ),
                ],
            ]
        )
    elif j == 6:
        key = InlineKeyboardMarkup(
            [
                [
                    a1,
                    a2,
                ],
                [
                    a3,
                    a4,
                ],
                [
                    a5,
                    a6,
                ],
                [
                    InlineKeyboardButton(
                        text="⇠ Geri Git",
                        callback_data=f"good {videoid}|{user_id}",
                    ),
                    InlineKeyboardButton(
                        text="🗑 Menüyü Kapat", callback_data=f"close2"
                    ),
                ],
            ]
        )
    else:
        return await CallbackQuery.message.reply_text(
            "𝗩𝗶𝗱𝗲𝗼 𝗙𝗼𝗿𝗺𝗮𝘁𝗹𝗮𝗿𝗶 𝗕𝘂𝗹𝘂𝗻𝗮𝗺𝗮𝗱𝗶. 𝗗𝗶𝗴̆𝗲𝗿 𝗠𝘂̈𝘇𝗶𝗸𝗹𝗲𝗿𝗶 𝗔𝗿𝗮𝗺𝗮𝘆𝗶 𝗗𝗲𝗻𝗲"
        )
    return key


def get_type(type, format, videoid, user_id):
    if type == "audio":
        a1 = InlineKeyboardButton(
            text=f"Şarkı Formu",
            callback_data=f"boom audio||{format}||{videoid}",
        )
        a2 = InlineKeyboardButton(
            text=f"Belge Formu",
            callback_data=f"boom docaudio||{format}||{videoid}",
        )
    else:
        a1 = InlineKeyboardButton(
            text=f"Video Formu",
            callback_data=f"boom video||{format}||{videoid}",
        )
        a2 = InlineKeyboardButton(
            text=f"Belge Formu",
            callback_data=f"boom docvideo||{format}||{videoid}",
        )
    key = InlineKeyboardMarkup(
        [
            [
                a1,
                a2,
            ],
            [
                InlineKeyboardButton(
                    text="⇠ Geri Git",
                    callback_data=f"good {videoid}|{user_id}",
                ),
                InlineKeyboardButton(
                    text="🗑 Menüyü Kapat", callback_data=f"close2"
                ),
            ],
        ]
    )
    return key
