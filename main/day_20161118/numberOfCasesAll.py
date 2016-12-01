
#1,2,3 으로 조합해서 만들수 있는 경우의
# 1 -> (1) : 1가지
# 2 -> (1, 1), (2) : 2가지
# 3 -> (1, 1, 1), (1, 2), (2, 1), (3) : 4가지
# 4 -> (1, 1, 1, 1), (1, 3), (3, 1), (2, 2), (1, 1, 2), (1, 2, 1), (2, 1, 1) : 7가지
#


def numberOfCasesAll(insertNumber, targetNumber, numberList):
  if insertNumber == targetNumber:
    print(numberList)
    return 1
  elif insertNumber < targetNumber:
    return numberOfCasesAll(insertNumber+1, targetNumber, numberList+[1]) + numberOfCasesAll(insertNumber+2, targetNumber, numberList+[2]) + numberOfCasesAll(insertNumber+3, targetNumber, numberList+[3])
  else:
    return 0

def getNumberCase(targetNumber):
  insertNumber = numberOfCasesAll(0, targetNumber, [])
  return insertNumber