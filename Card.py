from enum import Enum

class Card:
    def __init__(self, a_mark, a_num):
        self.mark = Mark[a_mark]
        self.num = a_num

    def show(self):
        return self.mark.name, self.num

    def get_mark(self):
        return self.mark.name

    def get_number(self):
        return self.num

class Mark(Enum):
    SPADE = 1
    HEART = 2
    CLOVER = 3
    DIAMOND = 4
