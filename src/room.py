# Implement a class to hold room information. This should have name and
# description attributes.
from player import Player


class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None

    # def player_direction(self, direction):
    #     if self.direction == 'n':
    #         return self.n_to
    #     elif self.direction == 'e':
    #         return self.e_to
    #     elif self.direction == 's':
    #         return self.s_to
    #     else:
    #         return None

    # def __str__(self):
    #     return f"{self.name}"
