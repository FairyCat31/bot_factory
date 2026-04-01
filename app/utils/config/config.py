from typing import Optional

from pydantic import BaseModel, Field, AnyHttpUrl

from app.utils.logger import LoggerConfig


class SlashCommand(BaseModel):
    """Slash command configuration"""
    name: str
    description: str

class Modal(BaseModel):
    """Modal configuration"""

class Button(BaseModel):
    """Buttons configuration"""

# --- Embed ---
class EmbedField(BaseModel):
    """Embed field configuration"""
    name: str
    value: str
    inline: bool

class Image(BaseModel):
    """Image configuration"""
    url: AnyHttpUrl

class Thumbnail(BaseModel):
    """Thumbnail configuration"""
    url: AnyHttpUrl
    
class Author(BaseModel):
    """Author configuration"""
    name: str
    icon_url: AnyHttpUrl

class Footer(BaseModel):
    """Footer configuration"""
    text: str
    icon_url: AnyHttpUrl

class Embed(BaseModel):
    """Embeds configuration"""
    color: int
    fields: Optional[list[EmbedField]] = Field(..., max_length=25)
    title: str
    url: Optional[AnyHttpUrl] = None
    image: Optional[Image] = None
    thumbnail: Optional[Thumbnail] = None
    author: Optional[Author] = None
    description: Optional[str] = None
    footer: Optional[Footer] = None

class BotConfig(BaseModel):
    """Root configuration model for the logger"""
    command_prefix: str
    cogs: list[str]
    phrases: dict[str, str]
    buttons: dict[str, Button]
    embeds: dict[str, Embed]
    modals: dict[str, Modal]
    cmds: dict[str, SlashCommand]
    logger: LoggerConfig
