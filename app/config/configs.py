from .loader import load_config
from .models import Buttons, Commands, Modals, Phrases, Embeds
from settings import ConfigSettings
from logger.config import LoggerConfig


class Configs:
    def __init__(self):
        self.embeds: Embeds | None = None
        self.modals: Modals | None = None
        self.buttons: Buttons | None = None
        self.commands: Commands | None = None
        self.phrases: Phrases | None = None
        self.logger: LoggerConfig | None = None


    def load(self):
        self.embeds = load_config(ConfigSettings.embeds_path, Embeds)
        self.modals = load_config(ConfigSettings.modals_path, Modals)
        self.buttons = load_config(ConfigSettings.buttons_path, Buttons)
        self.commands = load_config(ConfigSettings.commands_path, Commands)
        self.phrases = load_config(ConfigSettings.phrases_path, Phrases)
        self.logger = load_config(ConfigSettings.logger_path, LoggerConfig)


configs = Configs()
