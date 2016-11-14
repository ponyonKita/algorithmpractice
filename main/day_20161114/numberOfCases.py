

#1,2,3 으로 조합해서 만들수 있는 경우의
# 1 -> (1) : 1가지
# 2 -> (1, 1), (2) : 2가지
# 3 -> (1, 1, 1), (1, 2), (2, 1), (3) : 4가지
# 4 -> (1, 1, 1, 1), (1, 3), (3, 1), (2, 2), (1, 1, 2), (1, 2, 1), (2, 1, 1) : 7가지

def numberOfCases(inputNum):
  inputNum1 = inputNum

  for num in range(1,4):

    #입력된값과 처음이 같은숫자일때
    if num == inputNum:
      return num


    print(num)




  return True