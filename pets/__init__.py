import json
from pathlib import Path
from redbot.core.bot import Red
from .pets import Pets

_info = False
if _info:
    with open(Path(__file__).parent / "info.json") as fp:
        __red_end_user_data_statement__ = json.load(fp)


async def setup(bot: Red):
    bot.add_cog(await Pets.init(bot))
