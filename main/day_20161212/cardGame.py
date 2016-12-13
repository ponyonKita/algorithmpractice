import random


class Dealer:
    def __init__(self):

        heart_card = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13']
        spade_card = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13']
        diamond_card = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13']
        clover_card = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13']

        self.card = heart_card + spade_card + diamond_card + clover_card

    def shuffleCard(self, card):
        random.shuffle(card)
        return card

    #나누다
    def distributeCard(self, card):
        return card.pop()


class Player:

    def __init__(self):
        self.player1 = []
        self.player2 = []
        self.player3 = []
        self.player4 = []

    #카드 받는다
    def receiveCard(self, card):
        for count in range(7):
            self.player1.append(Dealer().distributeCard(card))
            self.player2.append(Dealer().distributeCard(card))
            self.player3.append(Dealer().distributeCard(card))
            self.player4.append(Dealer().distributeCard(card))


    def sumOfMyCard(self):
        scores = []

        player1Score = sum([int(score[1:]) for score in self.player1])
        player2Score = sum([int(score[1:]) for score in self.player2])
        player3Score = sum([int(score[1:]) for score in self.player3])
        player4Score = sum([int(score[1:]) for score in self.player4])

        scores.append(player1Score)
        scores.append(player2Score)
        scores.append(player3Score)
        scores.append(player4Score)

        return scores

    def winnerCheck(self, scores):

        for score in scores:
         if scores.count(score) >= 2:
               return GameStart()

        winnerPlayer = int(scores.index(max(scores)) + 1)

        return winnerPlayer


class GameStart:
    dealer = Dealer()
    player = Player()

    card = dealer.card
    shuffleCard = dealer.shuffleCard(card)

    player.receiveCard(shuffleCard)

    print('winner: player', +player.winnerCheck(player.sumOfMyCard()))




