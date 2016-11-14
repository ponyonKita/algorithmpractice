

#1,2,3 으로 조합해서 만들수 있는 경우의
# 1 -> (1) : 1가지
# 2 -> (1, 1), (2) : 2가지
# 3 -> (1, 1, 1), (1, 2), (2, 1), (3) : 4가지
# 4 -> (1, 1, 1, 1), (1, 3), (3, 1), (2, 2), (1, 1, 2), (1, 2, 1), (2, 1, 1) : 7가지

def numberOfCases(inputNum):
  if inputNum == 1:
    lastNum = 1
  elif inputNum == 2:
    lastNum = 2
  elif inputNum == 3:
    lastNum = 4
  else:
    return numberOfCases(inputNum-1)+numberOfCases(inputNum-2)+numberOfCases(inputNum-3)


  return lastNum


