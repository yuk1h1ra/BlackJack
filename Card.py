from enum import Enum

class Card:
    def __init__(self, a_mark, a_num):
        self.mark = Mark[a_mark]
        self.num = a_num

    def get_mark(self):
        return self.mark.name

    def get_number(self):
        this_num = self.num
        if this_num == 1:
            this_num = 'A'
        elif this_num == 11:
            this_num = 'J'
        elif this_num == 12:
            this_num = 'Q'
        elif this_num == 13:
            this_num = 'K'
        return this_num

class Mark(Enum):
    SPADE = 1
    HEART = 2
    CLOVER = 3
    DIAMOND = 4
