from disnake.ext import commands
from app.scripts.components.smartdisnake import SmartBot


class Main(commands.Cog):
    def __init__(self, bot: SmartBot):
        self.bot = bot

    @commands.slash_command(name="ping",
                            description="Проверка респонса от бота")
    @commands.default_member_permissions(administrator=True)
    async def ping(self, inter):
        author = inter.author
        print(author.name, author.nick, author.global_name)
        await inter.response.send_message("Successful request")


def setup(bot: SmartBot):
    bot.add_cog(Main(bot))
