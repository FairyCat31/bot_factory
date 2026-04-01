from disnake import ApplicationCommandInteraction
from disnake.ext import commands

from app.utils.smartdisnake import SmartBot, SmartEmbed


class DynamicConfigCog(commands.Cog):
    def __init__(self, bot: SmartBot):
        self.bot = bot

    async def config(self, inter: ApplicationCommandInteraction):
        embed = SmartEmbed(self.bot.cfg.embeds["dynamic_config_main"].model_dump(exclude_none=True),
                           dyn_vars={"SettingFields": "- hello\n- world"})
        await inter.response.send_message("hehe", embed=embed)


def build(bot: SmartBot):
    cfg_cmd = bot.cfg.cmds["main_cfg"]

    class BuildDynamicConfigCog(DynamicConfigCog):
        @commands.guild_only()
        @commands.has_guild_permissions(administrator=True)
        @commands.slash_command(name=cfg_cmd.name, description=cfg_cmd.description)
        async def config(self, inter: ApplicationCommandInteraction):
            await super().config(inter)

    return BuildDynamicConfigCog


def setup(bot: SmartBot):
    build_class = build(bot)
    bot.add_cog(build_class(bot))
