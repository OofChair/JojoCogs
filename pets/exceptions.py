from redbot.core import commands

__all__ = ["PetNotFound"]


class PetNotFound(commands.BadArgument):
    def __init__(self, pet: str = None):
        if pet:
            msg = f"Could not find a pet with the name '{pet}'."
        else:
            msg = "Could not find a pet with that name."
        super().__init__(msg)
