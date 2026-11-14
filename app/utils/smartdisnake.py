from typing import List, Dict

from disnake import Embed, ButtonStyle
from disnake.ext import commands

from config import configs, Configs
from logger import logger


BTN_STYLE_MAP = {
    1: ButtonStyle.primary,
    2: ButtonStyle.secondary,
    3: ButtonStyle.success,
    4: ButtonStyle.danger,
    5: ButtonStyle.success
}

# main class of bot
class SmartBot(commands.Bot):
    def __init__(self, intents, command_prefix):
        super().__init__(intents=intents, command_prefix=command_prefix)
        self.cfg: Configs = configs
        self.log = logger.bind(component="Bot")

    async def on_ready(self):
        self.log.info(f"I logged as {self.user}")

    async def on_command_error(self,
                               context: commands.Context,
                               exception: commands.errors.CommandError) -> None:
        logger.warning("Ignoring command -> %s" % context.message.content, log_text_in_file=False)


class SmartEmbed(Embed):
    def __init__(self, cfg: dict, dyn_vars: Dict[str, str]):
        self.dyn_vars = dyn_vars
        embed_funcs = {
            "thumbnail": super().set_thumbnail,
            "author": super().set_author,
            "footer": super().set_footer,
            "image": super().set_image
        }

        # create init args and super init
        init_args = {"color": cfg.get("color"), "url": cfg.get("url")}
        for arg in ("title", "description"):
            value = cfg.get(arg)
            if value is not None:
                value = value.format(**dyn_vars)
            init_args[arg] = value

        super().__init__(**init_args)

        # create fields and call init methods
        if cfg.get("fields") is not None:
            self.add_fields(cfg["fields"])

        for key in embed_funcs:
            if cfg.get(key) is None:
                continue
            embed_funcs[key](**cfg[key])

    def add_fields(self, embeds: List[dict]):
        for embed in embeds:
            super().add_field(name=embed["name"].format(**self.dyn_vars),
                              value=embed["value"].format(**self.dyn_vars),
                              inline=embed.get("inline"))
