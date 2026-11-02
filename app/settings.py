from pathlib import Path

command_prefix = "."

logger_config_path = Path("configs/logger.json5")
logger_config_encoding = "utf-8"


class ConfigSettings:
    embeds_path = Path("config/embeds.json5")
    modals_path = Path("config/modals.json5")
    buttons_path = Path("config/buttons.json5")
    commands_path = Path("config/commands.json5")
    phrases_path = Path("config/phrases.json5")
