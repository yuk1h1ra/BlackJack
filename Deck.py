from Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        for rep_mark in ["SPADE", "HEART", "CLOVER", "DIAMOND"]:
            for rep_num in range(1, 14):
                self.cards.append(Card(rep_mark, rep_num))

    def shuffle(self):
        random.shuffle(self.cards)


    def pop(self):
        return self.cards.pop()
