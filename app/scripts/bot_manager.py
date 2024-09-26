import disnake
from dotenv import dotenv_values
from components.jsonmanager import JsonManager, AddressType
from components.logger import Logger, PrintHandler, ErrorHandler
import sys
from components.smartdisnake import SmartBot
# from console_manager import Console


class BotManager:
    def __init__(self, debug: dict):
        # init logger and redirect standard err and out streams to logger
        self.log = Logger(module_prefix="Bot Manager", debug_mess=debug["debug_mode"])
        sys.stderr = ErrorHandler(self.log)
        sys.stdout = PrintHandler(self.log, debug_mess=debug["debug_mode"])
        self.json_manager = JsonManager(AddressType.FILE, "bot_properties.json")
        self.bot_man_props = JsonManager(AddressType.FILE, "factory.json")
        self.json_manager.load_from_file()
        self.bot_man_props.load_from_file()
        self.__env_val = dotenv_values(self.bot_man_props[".env"])
        self.bot = None
        self.log.printf(self.bot_man_props["init_bm"])

    def init_bot(self, **kwargs):
        command_prefix = self.json_manager["command_prefix"]
        self.log.printf(self.bot_man_props["init_bot"])
        intents = disnake.Intents.all()
        self.bot = SmartBot(intents=intents, command_prefix=command_prefix, **kwargs)

        for cog in self.json_manager["cogs"]:
            self.log.printf(self.bot_man_props["import_cog"].format(
                                                            cog=cog))
            self.bot.load_extension(cog)

        self.log.printf(self.bot_man_props["init_successful_bot"])

    def run_bot(self):
        token = self.__env_val["BOT_TOKEN"]
        self.log.printf(self.bot_man_props["st_bot"])
        self.bot.run(token)
