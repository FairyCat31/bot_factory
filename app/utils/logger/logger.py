from pathlib import Path

from rich.console import Console
import loguru

from app.utils.logger import LoggerConfig


logger = loguru.logger
output = Console()


class LogConfiguration:
    def __init__(self, config: LoggerConfig):
        self._cfg = config
        self._filepath = Path(config.file.filepath)

    def setup(self) -> None:
        logger.remove()

        rich_sink = lambda msg: output.print(msg, end="")
        console_format = lambda record: getattr(self._cfg.console.format, record["level"].name)
        file_format = lambda record: getattr(self._cfg.file.format, record["level"].name)


        # Add console handler
        logger.add(sink=rich_sink,
                 level=self._cfg.console.level,
                 format=console_format,
                 colorize=True)

        file_cfg = self._cfg.file
        # Add file handler
        logger.add(sink=file_cfg.filepath,
                level=file_cfg.level,
                format=file_format,
                rotation=file_cfg.rotation,
                retention=file_cfg.retention,
                encoding=file_cfg.encoding,
                compression=file_cfg.compression,
                colorize=False)
