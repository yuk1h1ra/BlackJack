from Card import Card

class Person:
    def __init__(self):
        self.cards = []

    def draw_card(self, card):
        self.cards.append(card)

    def show_card(self, number):
        return self.cards[number]

    def total_number(self):
        total_num = 0
        count_A = 0
        for card in self.cards:
            if card.num == 1:
                count_A += 1
                total_num += 11
            elif card.num >= 10:
                total_num += 10
            else:
                total_num += card.num
        for i in range(count_A):
            if total_num <= 21:
                break
            total_num -= 10
        return total_num

    def number_of_cards(self):
        return len(self.cards)
