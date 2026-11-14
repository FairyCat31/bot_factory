from os import environ as env

from logger import logger
from settings import command_prefix, intents, cogs
from utils.smartdisnake import SmartBot


class BotManager:
    def __init__(self):
        self.bot: SmartBot | None = None
        self.log = logger.bind(component="manager")
        self.log.success("Successful initialization of Bot manager")

    def init_bot(self, **kwargs):
        self.log.info("Start to initialize a bot")
        self.bot = SmartBot(intents=intents, command_prefix=command_prefix, **kwargs)
        for cog in cogs:
            self.log.info(f"Import '{cog}' to bot")
            self.bot.load_extension(f"cogs.{cog}")

        self.log.success("Successful initialization of bot")

    def run_bot(self):
        token = env["BOT_TOKEN"]
        logger.info("Starting bot...")
        self.bot.run(token)
