from pydantic import BaseModel, Field, AnyHttpUrl, RootModel


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
    fields: list[EmbedField] = Field(..., max_length=25)
    title: str
    url: AnyHttpUrl
    image: Image
    thumbnail: Thumbnail
    author: Author
    description: str
    footer: Footer


class Embeds(RootModel[dict[str, Embed]]):
    """Embeds configuration"""
    ...


class Modals(RootModel[dict[str, Modal]]):
    """Modals configuration"""
    ...


class Buttons(RootModel[dict[str, Button]]):
    """Buttons configuration"""
    ...


class Commands(RootModel[dict[str, SlashCommand]]):
    """Slash commands configuration"""
    ...


class Phrases(RootModel[dict[str, str]]):
    """Phrases configuration"""
    ...
