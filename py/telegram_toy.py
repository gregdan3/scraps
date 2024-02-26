#!/usr/bin/env python3
import os
import asyncio
from telethon import TelegramClient

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")


async def amain():
    async with TelegramClient("name", api_id, api_hash) as client:
        client.send_message("me", "Hello, myself!")
        k = client.get_dialogs()
        for dialog in k:
            print(dialog.name)
            print(dialog.id)
        participants = client.get_participants(1)  # REPLACEME
        print(participants)
        for user in participants:
            print(user.id)

        client.run_until_disconnected()


def main():
    asyncio.run(amain())


if __name__ == "__main__":
    main()
