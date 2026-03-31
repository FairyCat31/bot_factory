from disnake.ext import commands
from app.utils.smartdisnake import SmartBot




class DynamicConfig(commands.Cog):
    def __init__(self, bot: SmartBot):
        self.bot = bot


def build(bot: SmartBot):
    class BuildDynamicConfig(DynamicConfig):
        pass

    return BuildDynamicConfig


def setup(bot: SmartBot):
    build_class = build(bot)
    bot.add_cog(build_class(bot))
