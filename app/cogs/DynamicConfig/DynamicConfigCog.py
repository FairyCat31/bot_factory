from disnake import ApplicationCommandInteraction, ButtonStyle, MessageInteraction
from disnake.ui import Button, StringSelect
from disnake.ext import commands

from .config import init_cfg, load_cfg, dump_cfg
from app.utils.smartdisnake import SmartBot, SmartEmbed
from app.utils.logger import logger


class DynamicConfigCog(commands.Cog):
    def __init__(self, bot: SmartBot):
        self.bot = bot
        init_cfg()
        self.cfg = load_cfg()


    def list_vars(self) -> str:
        lines = []
        for name, var in self.cfg.variables.items():
            line = f"- {name}"
            if var.description:
                line += f" - {var.description}"

            line += f"\n  - Значение: {var.value}"
            lines.append(line)

        return "\n".join(lines)


    async def config(self, inter: ApplicationCommandInteraction):
        await self.start_menu(inter)

    async def start_menu(self, inter: MessageInteraction | ApplicationCommandInteraction):
        embed = SmartEmbed(self.bot.cfg.embeds["dynamic_config_main"].model_dump(exclude_none=True),
                           dyn_vars={"SettingFields": self.list_vars()})
        button = [Button(label="Редактировать", emoji="🔧", style=ButtonStyle.primary, custom_id="settings_menu")]
        if isinstance(inter, MessageInteraction):
            await inter.response.edit_message("", embed=embed, components=button)
        else:
            await inter.response.send_message("", embed=embed, components=button, ephemeral=True)

    async def settings_menu(self, inter: MessageInteraction):
        button = Button(label="Назад", emoji="🔙", style=ButtonStyle.secondary, custom_id="start_menu")
        selector = StringSelect(custom_id="select_setting",
                     placeholder="Выберите опцию...",
                     options= [name for name in self.cfg.variables.keys()])
        await inter.response.edit_message("Test", components=[selector, button], embed=None)

    async def select_setting(self, inter: MessageInteraction):
        var_name = inter.values[0]
        if var := self.cfg.variables.get(var_name):
            ...
        else:
            await inter.response.send_message("Значение не найдено", ephemeral=True)

    @commands.Cog.listener("on_button_click")
    async def on_button_click(self, inter: MessageInteraction):
        match inter.component.custom_id:
            case "settings_menu":
                await self.settings_menu(inter)
            case "start_menu":
                await self.start_menu(inter)
            case _:
                logger.warning(f"Button {inter.component.custom_id} not recognized")
                await inter.response.defer()

    @commands.Cog.listener("on_dropdown")
    async def on_dropdown(self, inter: MessageInteraction):
        match inter.component.custom_id:
            case "select_setting":
                await self.select_setting(inter)
            case _:
                logger.warning(f"Select {inter.component.custom_id} not recognized")
                await inter.response.defer()


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
