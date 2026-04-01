from json import load, dump
from pathlib import Path
from typing import Optional, Literal

from pydantic import BaseModel

from app.factory.settings import DynamicConfigSettings as Settings


_path = Path(Settings.CONFIG_PATH)


class Variable(BaseModel):
    value: Optional[str | int] = None
    type: Literal["STR", "INT", "FLOAT", "BOOL", "USERID", "ROLEID", "CHANNELID"]
    description: Optional[str] = None


class DynamicConfig(BaseModel):
    variables: dict[str, Variable]


def init_cfg():
    if not _path.exists():
        _path.parent.mkdir(parents=True, exist_ok=True)

        dump_cfg(DynamicConfig.model_validate(Settings.DEFAULT_CONFIG))

def load_cfg() -> DynamicConfig:
    with _path.open("r", encoding=Settings.ENCODING) as file:
        return DynamicConfig.model_validate(load(file))


def dump_cfg(cfg: DynamicConfig) -> None:
    with _path.open("w", encoding=Settings.ENCODING) as file:
        dump(cfg.model_dump(), file)
