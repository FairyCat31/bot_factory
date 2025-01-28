from app.scripts.components.smartdisnake import SmartBot
from app.scripts.cogs.WebAPI.Models import WebBase
from hypercorn.asyncio import serve


class CogWebAPIBase(WebBase):
    def __init__(self, bot: SmartBot):
        super().__init__(bot, name="Web Api")
        self.bot.add_async_task(serve(self.web_app, super().init_config_quart()))


def setup(bot: SmartBot):
    bot.add_cog(CogWebAPIBase(bot))
