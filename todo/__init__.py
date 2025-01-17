import json
import pathlib

from redbot.core.bot import Red

from .todo import ToDo  # type:ignore[attr-defined] # Silly mypy

with open(pathlib.Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]


def setup(bot: Red):
    bot.add_cog(ToDo(bot))
