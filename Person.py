from Card import Card

class Person:
    def __init__(self):
        self.cards = []

    def draw_card(self, card):
        self.cards.append(card)

    def show_card(self, number):
        return self.cards[number]

    def sum_number(self):
        sum_num = 0
        count_A = 0
        for card in self.cards:
            if card.num == 1:
                count_A += 1
                sum_num += 11
            elif card.num >= 10:
                sum_num += 10
            else:
                sum_num += card.num
        for i in range(count_A):
            if sum_num <= 21:
                break
            sum_num -= 10
        return sum_num

    def number_of_cards(self):
        return len(self.cards)
