# Copyright (c) 2021 - Jojo#7791
# Licensed under MIT

from __future__ import annotations
from redbot.core import commands

from .exceptions import PetNotFound


__all__ = ["create_doc"]


def create_doc(default: str = None, *, override: bool = False):
    def inner(func):
        if not func.__doc__ or override:
            func.__doc__ = default or "Documentation pending."

        return func
    return inner


class PetConverter(commands.Converter):
    async def convert(self, ctx: commands.Context, arg: str):
        confs = [ctx.cog._global_cache["pets"]]
        if ctx.guild:
            confs.append(ctx.cog._guild_cache["pets"])
        for conf in confs:
            if arg.lower() in conf.keys():
                return conf[arg.lower()]
        raise PetNotFound(arg.lower())
