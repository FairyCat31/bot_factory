from os import environ as env

from disnake import Intents

from utils.logger import logger
from utils.ujson import JsonManager
from utils.smartdisnake import SmartBot
from config import load_config, BotConfig


class BotManager:
    def __init__(self):
        self.bot: SmartBot | None = None

        # load json files
        self.cfg: BotConfig = load_config()
        self.factory_jsm = JsonManager("factory.json")
        self.factory_jsm.load_from_file()

        logger.info(self.factory_jsm["init_bm"])

    def init_bot(self, **kwargs):
        logger.info(self.factory_jsm["init_bot"])

        command_prefix = self.cfg.command_prefix
        intents = Intents.all()
        self.bot = SmartBot(intents=intents, command_prefix=command_prefix, **kwargs)
        for cog in self.cfg.cogs:
            logger.info(self.factory_jsm["import_cog"].format(cog=cog))
            self.bot.load_extension(cog)

        logger.info(self.factory_jsm["init_successful_bot"])

    def run_bot(self):
        token = env["BOT_TOKEN"]
        logger.info(self.factory_jsm["st_bot"])
        self.bot.run(token)
