import asyncio
from os import environ as env
from time import perf_counter

from logger import logger
from settings import command_prefix, intents, cogs
from utils.smartdisnake import SmartBot


class BotManager:
    def __init__(self):
        self.bot: SmartBot = SmartBot(intents=intents, command_prefix=command_prefix)
        self.log = logger.bind(component="manager")
        self.log.success("Successful initialization of Bot manager")

    def init_bot(self):
        self.log.info("Start to initialize a bot")

        for cog in cogs:
            self.log.info(f"Import '{cog}' to bot")
            self.bot.load_extension(f"cogs.{cog}")

        self.log.success("Successful initialization of bot")

    async def start_timer(self):
        start_time = perf_counter()
        await self.bot.wait_until_ready()
        elapsed_time = perf_counter() - start_time
        self.log.success(f"Bot has successfully started up! (elapsed: {elapsed_time:.2f}s)")


    async def run_bot(self):
        token = env["BOT_TOKEN"]
        self.log.info("Starting bot...")
        asyncio.create_task(self.start_timer())
        await self.bot.start(token)
