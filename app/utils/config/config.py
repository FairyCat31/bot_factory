from typing import Literal, Union, Annotated, Any

from pydantic import BaseModel, Field, BeforeValidator, AnyHttpUrl

'''
{
  "command_prefix": ".",
  "dynamic_config_file_name": "dyn_conf.json",
  "cogs": ["cogs.Main", "cogs.DynamicConfig"],
  "def_phrases": {
    "start" : "Successful starting\nI logged as {user}\nStarting during: {during_time}",
    "FormatErrorDynConfig" : "Ошибка обновления параметра.\\nНе удалось преобразовать {value} в {data_type_need}",
    "ConsoleFormatErrorDynConfig": "IncorrectTypeParameter: Failed to update parameter value",
    "ConsoleEditInfo": "Параметр {parameter} изменён ---> {convert_value}",
    "RunErrorDynConfig": "Parameter \"%s\" not set. Func can't start correctly",
    "PermErrorDynConfig": "У вас нету прав использовать эту команду",
    "ping": "Успешно передано"
  },
  "phrases": {
  },
  "buttons": {
  },
  "embeds": {
  },
  "modals": {
  },
  "cmds": {
    "main_cfg": {"name": "config", "description": "Команда для настройки бота"},
    "set_cfg": {"name": "set", "description": "Изменить настройки бота"},
    "del_cfg": {"name": "reset", "description": "Сбросить настройки/настройку бота"},
    "show_cfg": {"name": "show", "description": "Показать настройки бота"},
    "main_ping": {"name": "ping", "description":  "Проверка ответа от бота"}
  }
}
'''

class SlashCommand(BaseModel):
    """Slash command configuration"""
    name: str
    description: str

class Modal(BaseModel):
    """Modal configuration"""
d = {
      "color": 16518578,
      "fields": [
        {
          "name": "Вы подключаетесь не из РФ или СНГ?",
          "value": "Скорее всего фаерволл Российской федерации вас не пускает на наши сервера авторизации. \n- Временное решение : включите ВПН в регионе RU\n\nМы уже работает над решением этой проблемы.",
          "inline": True
        },
        {
          "name": "Лагает на серверах?",
          "value": "Возможно у вас запустилась игра на встроенной видеокарте. Это можно проверить, нажав f3 в игре. И справа вверху найти пункт display, чуть ниже будет указана ваша видеокарта. Если это не так, то:\n- Попробуйте перезагрузить лаунчер/ПК\n- Попробуйте выполнить эти инструкции\n[ГАЙД /  Переключаем встроенную видеокарту](https://youtu.be/_KSBj1jSeis?si=kH9y2MIC1t66q2T3)\n"
        }
      ],
      "title": "Частые проблемы",
      "url": "sfb",
      "image": {
        "url": "srh"
      },
      "thumbnail": {
        "url": "dfn"
      },
      "author": {
        "url": "dfb",
        "name": "Sb",
        "icon_url": "srtj"
      },
      "description": "zdmsfm",
      "footer": {
        "text": "dfgmgm",
        "icon_url": "zdgmdfgmgd"
      },
      "timestamp": "2026-03-11T21:00:00.000Z"
    }
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


class Button(BaseModel):
    """Buttons configuration"""

class BotConfig(BaseModel):
    """Root configuration model for the logger"""
    command_prefix: str
