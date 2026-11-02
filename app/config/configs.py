from pydantic import ValidationError

from config import load_config
from config.models import Buttons, Commands, Modals, Phrases, Embeds
from settings import ConfigSettings

embeds: Embeds | None = None
modals: Modals | None = None
buttons: Buttons | None = None
commands: Commands | None = None
phrases: Phrases | None = None


def load():
    global embeds, modals, buttons, commands, phrases

    try:
        embeds = load_config(ConfigSettings.embeds_path, Embeds)
        modals = load_config(ConfigSettings.modals_path, Modals)
        buttons = load_config(ConfigSettings.buttons_path, Buttons)
        commands = load_config(ConfigSettings.commands_path, Commands)
        phrases = load_config(ConfigSettings.phrases_path, Phrases)

    except ValidationError as e:
        pass

