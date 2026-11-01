from pathlib import Path

from json5 import load

from settings import logger_config_path, logger_config_encoding
from utils.logger import LoggerConfig, setup
from bot_manager import BotManager


def setup_logger():
    with Path(logger_config_path).open(encoding=logger_config_encoding) as f:
        setup(LoggerConfig.model_validate(load(f)))


def main():
    setup_logger()
    bm = BotManager()
    bm.init_bot(name="test")
    bm.run_bot()


if __name__ == "__main__":
    main()
