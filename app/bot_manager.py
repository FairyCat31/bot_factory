import sys
from os import environ as env

from disnake import Intents

from utils.logger import logger, LogConfiguration, LoggerConfig
from utils.ujson import JsonManager, JsonManager5
from utils.smartdisnake import SmartBot




class BotManager:
    def __init__(self):
        self.bot: SmartBot | None = None

        # load json files
        self.bot_properties = JsonManager("bot_properties.json")
        self.factory_jsm = JsonManager("factory.json")
        self.bot_properties.load_from_file()
        self.factory_jsm.load_from_file()

        logger_jsm = JsonManager5("logger_conf.json5")
        logger_jsm.load()
        LogConfiguration(LoggerConfig.model_validate(logger_jsm.buffer)).setup()
        

        logger.info(self.factory_jsm["init_bm"])

    def init_bot(self, **kwargs):
        logger.info(self.factory_jsm["init_bot"])

        command_prefix = self.bot_properties["command_prefix"]
        intents = Intents.all()
        self.bot = SmartBot(intents=intents, command_prefix=command_prefix, **kwargs)
        for cog in self.bot_properties["cogs"]:
            logger.info(self.factory_jsm["import_cog"].format(cog=cog))
            self.bot.load_extension(cog)

        logger.info(self.factory_jsm["init_successful_bot"])

    def run_bot(self):
        token = env["BOT_TOKEN"]
        logger.info(self.factory_jsm["st_bot"])
        self.bot.run(token)
