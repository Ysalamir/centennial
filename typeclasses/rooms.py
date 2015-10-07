"""
Room

Rooms are simple containers that has no location of their own.

"""
from typeclasses.characters import Character
from typeclasses.objects import Object
from typeclasses.ship import ShipObject
from evennia import DefaultRoom
from commands.library import header, subheader, make_table, tabular_table
from evennia.utils import evtable


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
        message.append(header())
        chars = self.list_characters()
        objects = self.list_non_characters()
        table = evtable.EvTable("{wCharacters:{n", "{wObjects:{n", table=[chars, objects], border=None)
        table.reformat_column(0, width=39, align="l")
        message.append(table)
        # if chars:
        #     message.append("\nCharacters:")
        #     for char in chars:
        #         message.append(char.key + "\n")

        if self.exits:
             message.append("\nExits:")
             for exit in self.exits:
                 message.append(exit.format_output(caller))
        message2 = []
        for line in message:
            message2.append(unicode(line))
        return "\n".join(message2)

    def list_characters(self):
        return sorted([char for char in self.contents if char.is_typeclass(Character, exact=False)])

    def online_characters(self, viewer=None):
        characters = [char for char in self.list_characters() if char.sessions]
        if viewer:
            characters = [char for char in characters if viewer.can_see(char)]

    def list_non_characters(self):
        #return sorted([object for object in self.contents if object.is_typeclass(Object, exact=False)])
        return list(Object.objects.filter_family(db_location=self))