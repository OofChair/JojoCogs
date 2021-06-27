# Copyright (c) 2021 - Jojo#7791
# Licensed under MIT


from redbot.core import commands, Config
from redbot.core.bot import Red

from .utils import create_doc, PetConverter


_config_structure: dict = {
    "global": {},
    "user": {},
    "guild": {},
}


@create_doc(override=True)
class Pets(commands.Cog):
    _user_cache: dict
    _global_cache: dict
    _guild_cache: dict

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, 544974305445019651, True)
        self.config.register_global(**_config_structure["global"])
        self.config.register_user(**_config_structure["guild"])
        self.config.register_guild(**_config_structure["guild"])

    @classmethod
    async def init(cls, bot: Red):
        self = cls(bot)
        self._user_cache = await self.config.all_users()
        self._global_cache = await self.config.all()
        self._guild_cache = await self.config.all_guilds()
        return self

    @commands.group()
    @create_doc(override=True)
    async def pets(self, ctx: commands.Context):
        pass

    @pets.command(name="buy")
    @create_doc(override=True)
    async def pets_buy(self, ctx: commands.Context, *, pet: PetConverter):
        ...
