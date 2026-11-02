from pathlib import Path
from typing import Type

from json5 import load
from pydantic import BaseModel


def load_config[T: BaseModel](path: Path, model: Type[T]) -> T:
    with path.open('r') as f:
        return model.model_validate(load(f))
