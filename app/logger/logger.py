from rich.console import Console
import loguru

from utils.logger import LoggerConfig


logger = loguru.logger
output = Console()


def setup(config: LoggerConfig) -> None:
    logger.remove()

    rich_sink = lambda msg: output.print(msg, end="")
    console_format = lambda record: getattr(config.console.format, record["level"].name)
    file_format = lambda record: getattr(config.file.format, record["level"].name)


    # Add console handler
    logger.add(sink=rich_sink,
             level=config.console.level,
             format=console_format,
             colorize=True)

    file_cfg = config.file
    # Add file handler
    logger.add(sink=file_cfg.filepath,
            level=file_cfg.level,
            format=file_format,
            rotation=file_cfg.rotation,
            retention=file_cfg.retention,
            encoding=file_cfg.encoding,
            compression=file_cfg.compression,
            colorize=False)
