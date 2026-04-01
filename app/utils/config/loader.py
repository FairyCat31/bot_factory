from pathlib import Path

from json5 import load

from app.factory.settings import ConfigSettings
from app.utils.config.config import BotConfig


def load_config(path: str | Path  = ConfigSettings.CONFIG_PATH) -> BotConfig:
    if isinstance(path, str):
        path = Path(path)

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open('w', encoding=ConfigSettings.ENCODING) as f:
            f.write(ConfigSettings.DEFAULT_CONFIG)

    with path.open('r', encoding=ConfigSettings.ENCODING) as f:
        return BotConfig.model_validate(load(f))
