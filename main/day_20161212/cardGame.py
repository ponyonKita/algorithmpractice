import random
"""

H1, H2, ....H13,
C1, C2, ....C13,
으로 표시된다.
Player 는 7 장의 카드를 가지며, 숫자의 합이 제일 작은 사람이 이긴다.

4명의 Player 에게 중복없이 랜덤하게 카드를 나누고, 이긴 Player 를 출력하는 프로그램을 완성하시오.
숫자의 합이 제일 작은 Player가 2명 이상이면 1명이 승리할 때까지 반복한다.

출력예)
Player 1 : H2, H8, D5, D9, S12, S9, C13 : sum = 58
Player 2 : C8, C6, S4, D4, D12, C2, C12 : sum = 48
Player 3 : C10, S1, D2, D7, D10, C11, C9 : sum = 50
Player 4 : D8, D1, H6, H13, C7, H10, S8 : sum = 53

Winner : Player 2

"""

class Dealer:
    def __init__(self):

        heart_card = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13']
        spade_card = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13']
        diamond_card = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13']
        clover_card = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13']

        self.card = heart_card + spade_card + diamond_card + clover_card

    def shuffleCard(self):
        random.shuffle(self.card)

    #나누다
    def distributeCard(self, card):
        return card.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.myCard = []

    #카드 받는다
    def receiveCard(self, card):
        self.myCard.append(card)


    def sumOfMyCard(self):

        sumOfMyCard = sum([int(card[1:]) for card in self.myCard])
        return sumOfMyCard



class GameStart:
    dealer = Dealer()
    card = dealer.card
    player1 = Player('1')
    player2 = Player('2')
    player3 = Player('3')
    player4 = Player('4')

    dealer.shuffleCard()

    for i in range(7):
        player1.receiveCard(dealer.distributeCard(card))
        player2.receiveCard(dealer.distributeCard(card))
        player3.receiveCard(dealer.distributeCard(card))
        player4.receiveCard(dealer.distributeCard(card))

    print('player1 :', ",".join(player1.myCard), 'SUM:', + player1.sumOfMyCard())
    print('player2 :', ",".join(player2.myCard), 'SUM:', + player2.sumOfMyCard())
    print('player3 :', ",".join(player3.myCard), 'SUM:', + player3.sumOfMyCard())
    print('player4 :', ",".join(player4.myCard), 'SUM:', + player4.sumOfMyCard())

    scores = [player1.sumOfMyCard(), player2.sumOfMyCard(), player3.sumOfMyCard(), player4.sumOfMyCard()]

    for score in scores:
        if scores.count(score) >= 2:
            game = GameStart()

    winnerPlayer = int(scores.index(max(scores)) + 1)


    print('winner: player', +winnerPlayer)












