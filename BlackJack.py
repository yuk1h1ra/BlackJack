from Deck import Deck
from Card import Card
from Person import Person
import sys

def main():
    deck = Deck()
    player = Person()
    dealer = Person()

    deck.shuffle()

    print("これからBJを始めます\n")

    # 初期セットアップ
    player.draw_card(deck.pop())
    print("あなたの1枚めは" + str(player.show_card(0).get_mark()) + "の" + str(player.show_card(0).get_number()) + "です")
    player.draw_card(deck.pop())
    print("あなたの2枚めは" + str(player.show_card(1).get_mark()) + "の" + str(player.show_card(1).get_number()) + "です")

    dealer.draw_card(deck.pop())
    print("CPUの1枚めは" + str(dealer.show_card(0).get_mark()) + "の" + str(dealer.show_card(0).get_number()) + "です")
    dealer.draw_card(deck.pop())
    print("CPUの2枚めは伏せられています")

    # ユーザーの番
    print("あなたの番です")
    print("あなたの合計数は" +
            str(player.total_number()) + "です")
    while True:
        print("\nカードを引きますか？")
        print("[Y]: 引く")
        print("[N]: 引かない")

        input_line = input()
        # Loopを抜ける
        if input_line == "N":
            break

        player.draw_card(deck.pop())
        print("あなたの" + str(player.number_of_cards()) + "枚めは" + str(player.show_card(-1).get_mark()) + "の" + str(player.show_card(-1).get_number()) + "です")

        print("あなたの合計数は" +
                str(player.total_number()) + "です")

        if player.total_number() >= 22:
            print("バーストしました。あなたの負けです")
            sys.exit()

    # ディーラーの番
    print("\nCPUの番です")
    print("CPUの" + str(dealer.number_of_cards()) + "枚めは" + str(dealer.show_card(-1).get_mark()) + "の" + str(dealer.show_card(-1).get_number()) + "です")
    print("CPUの合計数は" +
            str(dealer.total_number()) + "です")
    while True:
        # 17以上のときはカードを引かない
        if dealer.total_number() >= 17:
            break
        dealer.draw_card(deck.pop())
        print("CPUの" + str(dealer.number_of_cards()) + "枚めは" + str(dealer.show_card(-1).get_mark()) + "の" + str(dealer.show_card(-1).get_number()) + "です")

        print("CPUの合計数は" +
                str(dealer.total_number()) + "です")

        if dealer.total_number() >= 22:
            print("バーストしました。あなたの勝ちです")
            sys.exit()

    # 結果発表
    print("\nあなたの合計数は" +
            str(player.total_number()) + "です")
    print("CPUの合計数は" +
            str(dealer.total_number()) + "です")
    if player.total_number() > dealer.total_number():
        print("あなたの勝ちです")
    elif player.total_number() < dealer.total_number():
        print("CPUの勝ちです")
    else:
        print("引き分けです")

if __name__ == '__main__':
    main()
