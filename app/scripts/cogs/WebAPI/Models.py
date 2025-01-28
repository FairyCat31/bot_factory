from datetime import datetime
from disnake.ext import commands
from typing import Dict, Any
from hypercorn.config import Config
from app.scripts.cogs.WebAPI.WebSecure import load_tokens, DataCrypter
from app.scripts.components.smartdisnake import SmartBot
from quart import Quart
from app.scripts.components.crypter import CrypterDict, Hasher
from app.scripts.components.jsonmanager import JsonManagerWithCrypt


class WebSession:
    def __init__(self, ip: str, token_data: JsonManagerWithCrypt, life_time: int = 3600):
        self.ip = ip
        self.auth = False
        self.token_data = token_data
        self.dead_time = datetime.now().timestamp() + life_time
        self.session_crypter = DataCrypter()
        self.session_crypter.generate_keys(key_size=2048)
        self.token_crypter = CrypterDict(crypt_key=token_data['key'].encode())
        self.session_hasher = Hasher('sha256', 32)

    def is_dead(self) -> bool:
        return datetime.now().timestamp() > self.dead_time

    def is_valid(self) -> bool:
        return not self.is_dead() and self.auth


class WebPacket:
    def __init__(self):
        self.json_data = {}
        self.send_data = ""
        # s or g ~ name
        self.packet_type = ""
        self.arrive_time = datetime.now().timestamp()
    """
    Method for handling raw request
    return
    0 - if all ok
    1 - Incorrect format
    2 - Bad packet (something was going wrong, when packet was decrypted)
    3 - Corrupted format"""
    # def handle_raw_request(self, raw_request: MultiDict) -> int:
    #     if "file" not in raw_request:
    #         return 1
    #     data = raw_request["file"].read()
    #     code, result = self._session.session_crypter.data_decrypt(data)
    #     if code:
    #         return 2
    #     try:
    #         self.json_data = loads(result.decode())
    #     except JSONDecodeError:
    #         return 3
    #     return 0

    def is_correct_format(self, json_pattern: Dict[str, Any], json_data=None):
        if json_data is None:
            json_data = self.json_data
        for key, value in json_pattern.items():
            if type(value) is dict:
                sub_json_data = json_data.get(key)
                if type(sub_json_data) is not dict:
                    return False
                if not self.is_correct_format(value, json_data=sub_json_data):
                    return False
                continue
            if type(json_data.get(key)) is not value:
                return False
        return True

    def is_alive(self) -> bool:
        return self.arrive_time < self.json_data['dead_time']

    def is_valid(self, json_pattern: Dict[str, Any]):
        is_c_f = self.is_correct_format(json_pattern)
        if not is_c_f:
            return False
        return self.is_alive()


class WebBase(commands.Cog):
    def __init__(self, bot: SmartBot, name: str):
        self.bot = bot
        self.tokens = load_tokens()
        self.sessions: Dict[str, WebSession] = {}
        self.temp_sessions: Dict[str, WebSession] = {}
        self.web_app = Quart(name)

    @staticmethod
    def init_config_quart() -> Config:
        config = Config()
        config.keyfile = "app/data/sys/cert.key"
        config.certfile = "app/data/sys/cert.crt"
        config.bind = ['localhost:8080']
        return config

    @commands.Cog.listener(name="on_ready")
    async def on_ready(self):
        self.bot.log.printf(f"Serving Quart app '{self.web_app.name}'")


def setup(bot: SmartBot):
    pass
    # bot.add_cog(CogWebAPIBase(bot))

