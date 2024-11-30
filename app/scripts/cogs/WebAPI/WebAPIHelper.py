import hashlib
import datetime
from json import loads
from disnake.ext import commands
from typing import Coroutine, Dict
from hypercorn.asyncio import serve
from hypercorn.config import Config
from string import ascii_letters, digits
from app.scripts.components.smartdisnake import SmartBot
from quart import Quart, request, render_template
from app.scripts.components.crypter import AsymmetricCrypter, Crypter
from app.scripts.factory.sysFuncs import check_requirements, generate_id
from app.scripts.components.jsonmanager import JsonManagerWithCrypt


REQS = []
COGS_DEP = []
check_requirements(REQS)


class CogWebAPIBase(commands.Cog):
    def __init__(self, bot: SmartBot):
        self.bot = bot
        self.web_app = Quart(__name__)
        self.__init_custom_quart()
        self.__config = Config()
        self.__config.keyfile = "app/data/sys/cert.key"
        self.__config.certfile = "app/data/sys/cert.crt"
        self.__config.bind = ['localhost:8080']
        self.bot.add_async_task(serve(self.web_app, self.__config))

    def __init_custom_quart(self):
        pass

    @commands.Cog.listener(name="on_ready")
    async def on_ready(self):
        self.bot.log.printf(f"Serving Quart app '{self.web_app.name}")


def setup(bot: SmartBot):
    bot.add_cog(CogWebAPIBase(bot))
