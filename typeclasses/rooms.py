"""
Room

Rooms are simple containers that has no location of their own.

"""
from typeclasses.characters import Character
from evennia import DefaultRoom
from commands.library import header, subheader, make_table, tabular_table


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    def return_appearance(self, caller):
        message = []
        message.append(header(self.key, viewer=caller))
        message.append(self.db.desc)
        chars = self.list_characters()
        if chars:
            message.append("\nCharacters:")
            for char in chars:
                message.append(char.key + "\n")

        if self.exits:
             message.append("Exits:")
             for exit in self.exits:
                 message.append(exit.format_output(caller))
        message2 = []
        for line in message:
            message2.append(unicode(line))
        return "\n".join(message2)

    def list_characters(self):
        return sorted([char for char in self.contents if char.is_typeclass(Character, exact=False)], key=lambda char: char.key.lower())

    def online_characters(self, viewer=None):
        characters = [char for char in self.list_characters() if char.sessions]
        if viewer:
            characters = [char for char in characters if viewer.can_see(char)]

