from pathlib import Path

from disnake import Intents

command_prefix = "."
intents = Intents.all()
cogs = ["Main"]

class ConfigSettings:
    logger_path = Path("configs/logger.json5")
    embeds_path = Path("configs/embeds.json5")
    modals_path = Path("configs/modals.json5")
    buttons_path = Path("configs/buttons.json5")
    commands_path = Path("configs/commands.json5")
    phrases_path = Path("configs/phrases.json5")
