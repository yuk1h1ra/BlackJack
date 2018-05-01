from Deck import Deck
from Card import Card
import sys

def sum_number(cards):
    sum_num = 0
    count_A = 0
    for card in cards:
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

def main():
    deck = Deck()
    user_cards = []
    dealer_cards = []

    deck.shuffle()

    print("これからBJを始めます\n")

    # 初期セットアップ
    user_cards.append(deck.pop())
    print("あなたの1枚めは" + str(user_cards[0].get_mark()) + "の" + str(user_cards[0].get_number()) + "です")
    user_cards.append(deck.pop())
    print("あなたの2枚めは" + str(user_cards[1].get_mark()) + "の" + str(user_cards[1].get_number()) + "です")

    dealer_cards.append(deck.pop())
    print("CPUの1枚めは" + str(dealer_cards[0].get_mark()) + "の" + str(dealer_cards[0].get_number()) + "です")
    dealer_cards.append(deck.pop())
    print("CPUの2枚めは伏せられています")

    print("あなたの合計数は" +
            str(sum_number(user_cards)) + "です")

    # ユーザーの番
    print("あなたの番です")
    while True:
        print("\nカードを引きますか？")
        print("[0]: 引く")
        print("[1]: 引かない")

        input_line = int(input())
        # Loopを抜ける
        if input_line == 1:
            break

        user_cards.append(deck.pop())
        print("あなたの" + str(len(user_cards)) + "枚めは" + str(user_cards[-1].get_mark()) + "の" + str(user_cards[-1].get_number()) + "です")

        print("あなたの合計数は" +
                str(sum_number(user_cards)) + "です")

        if sum_number(user_cards) >= 22:
            print("バーストしました。あなたの負けです")
            sys.exit()

    # CPUのカード引き
    print("CPUの番です")
    print("CPUの" + str(len(dealer_cards)) + "枚めは" + str(dealer_cards[-1].get_mark()) + "の" + str(dealer_cards[-1].get_number()) + "です")
    print("CPUの合計数は" +
            str(sum_number(dealer_cards)) + "です")
    while True:
        # 17以上のときはカードを引かない
        if sum_number(dealer_cards) >= 17:
            break

        dealer_cards.append(deck.pop())
        print("CPUの" + str(len(dealer_cards)) + "枚めは" + str(dealer_cards[-1].get_mark()) + "の" + str(dealer_cards[-1].get_number()) + "です")

        print("CPUの合計数は" +
                str(sum_number(dealer_cards)) + "です")

        if sum_number(dealer_cards) >= 22:
            print("バーストしました。あなたの勝ちです")
            sys.exit()

    # 結果発表
    print("あなたの合計数は" +
            str(sum_number(user_cards)) + "です")
    print("CPUの合計数は" +
            str(sum_number(dealer_cards)) + "です")
    if sum_number(user_cards) > sum_number(dealer_cards):
        print("あなたの勝ちです")
    elif sum_number(user_cards) < sum_number(dealer_cards):
        print("CPUの勝ちです")
    else:
        print("引き分けです")

if __name__ == '__main__':
    main()
