from typing import Optional

from pydantic import BaseModel

from .types import UserID, RoleID, ChannelID


class Variable(BaseModel):
    value: str
    type: int | str | bool | RoleID | UserID | ChannelID
    description: Optional[str] = None

class DynamicConfig(BaseModel):
    variables: dict[str, Variable]