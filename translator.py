from telethon.sync import TelegramClient, events
from telethon.errors import MessageNotModifiedError
from translatepy import Translator, exceptions


# https://my.telegram.org/apps
API_ID = 123
API_HASH = "123"


client = TelegramClient("bot", API_ID, API_HASH)
client.start()

translator = Translator()

language = dict(lang="en", start=0)


@client.on(events.NewMessage(outgoing=True, pattern=r"(?i).trlang"))
async def languageset(event):
    await event.delete()
    lang = event.message.message.split(" ")[1].lower()
    language["lang"] = lang
    await client.send_message("me", "Translation language changed to {}".format(lang))


@client.on(events.NewMessage(outgoing=True, pattern=r"(?i).trstart"))
async def start_translating(event):
    await event.delete()
    language["start"] = 1
    await client.send_message(
        "me", "Automatic message translation started\nLanguage: {}".format(language["lang"])
    )


@client.on(events.NewMessage(outgoing=True, pattern=r"(?i).trstop"))
async def stop_translating(event):
    await event.delete()
    language["start"] = 0
    await client.send_message("me", "Auto-translate messages disabled")


@client.on(events.NewMessage(outgoing=True))
async def main(event):
    if language["start"] == 1 and not event.message.message.startswith(".tr"):
        try:
            message = translator.translate(event.message.message, language["lang"])
            await event.edit(message.result)
        except (exceptions.NoResult, exceptions.UnknownLanguage) as error:
            await event.delete()
            await client.send_message(
                "me",
                "An error occurred while translating message {} into language ({}):\n{}\n\nThis language may not exist, please try another one.".format(
                    event.message.message, language["lang"], error
                ),
            )
        except MessageNotModifiedError:
            pass


client.run_until_disconnected()