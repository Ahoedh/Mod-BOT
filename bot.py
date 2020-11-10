import asyncio
import discord
import time
from discord.ext import commands
from discord import Embed, Color
from typing import Optional
from pathlib import Path

class ModBot(commands.Bot):
    def __init__(self):
        self._cogs = [p.stem for p in Path(".").glob("./bot/cogs/*.py")]
        super().__init__(command_prefix=self.prefix, case_insensitive=True)

    def setup(self):
        print("[RUNNING]")

        for cog in self._cogs:
            self.load_extension(f"bot.cogs.{cog}")
            print(f"[LOADING] {cog}")

        print("[SUCCESSFULL] loaded all the cogs.")

    async def on_ready(self):
        print("ModBot ready")

    async def prefix(self, bot, msg):
        return commands.when_mentioned_or("!")(bot, msg)
