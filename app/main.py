import asyncio

from config import configs
from bot_manager import BotManager
from logger import setup_logger


def main():
    configs.load()
    setup_logger(configs.logger)
    bm = BotManager()
    bm.init_bot()
    asyncio.run(bm.run_bot())



if __name__ == "__main__":
    main()
