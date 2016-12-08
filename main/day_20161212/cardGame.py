import random


def cardGame():
  player1 = []
  player2 = []
  player3 = []
  player4 = []

  card = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'
          , 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13'
          , 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13'
          , 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13']


  for i in range(0, 7):
    random.shuffle(card)
    player1.append(card.pop())
    player2.append(card.pop())
    player3.append(card.pop())
    player4.append(card.pop())


  player1Score = sum([int(score[1:]) for score in player1])
  player2Score = sum([int(score[1:]) for score in player2])
  player3Score = sum([int(score[1:]) for score in player3])
  player4Score = sum([int(score[1:]) for score in player4])


  print(player1)
  print(player2)
  print(player3)
  print(player4)
  print(player1Score)
  print(player2Score)
  print(player3Score)
  print(player4Score)


print(cardGame())