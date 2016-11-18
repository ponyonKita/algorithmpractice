

#1,2,3 으로 조합해서 만들수 있는 경우의
# 1 -> (1) : 1가지
# 2 -> (1, 1), (2) : 2가지
# 3 -> (1, 1, 1), (1, 2), (2, 1), (3) : 4가지
# 4 -> (1, 1, 1, 1), (1, 3), (3, 1), (2, 2), (1, 1, 2), (1, 2, 1), (2, 1, 1) : 7가지

def numberOfCasesAll(inputNum):
  list = []
  list2 = []
  list3 = []

  for i in range(1, 4):
    list.insert(i, i)
    #print(list)
    if sum(int(j) for j in list) < inputNum:
      list.insert(i, i)
      if sum(int(j) for j in list) < inputNum:
        list.insert(i, i)
      elif sum(int(j) for j in list) > inputNum:
        list.remove(i)
      elif sum(int(j) for j in list) == inputNum:
        list.insert(i, i)
        list2.append(list)
    elif sum(int(j) for j in list) > inputNum:
      list.remove(i)
    elif sum(int(j) for j in list) == inputNum:
      list.insert(i, i)
      list2.append(list)

  print(list)
  print(list2)






  #insertNum = [1,2,3]
  # for i in range(1, inputNum+1):
  #   for j in range(1, 4):
  #     total = i + j
  #   list.append(i)
  #   list.append(j)
  #   if sum(int(j) for j in list) <= inputNum:
  #     list2.append(list)
  #


  #
  # for i in range(1, 4):
  #   list.insert(i, i)
  #   print(list)
  #   if sum(int(j) for j in list) > inputNum:
  #     list.remove(i)
  #   elif sum(int(j) for j in list) < inputNum:
  #     list.insert(i, i)
  #
  #     if sum(int(j) for j in list2) < inputNum:
  #       list.insert(i, i)
  #     elif sum(int(j) for j in list2) == inputNum:
  #       #list.append(i, i)
  #       pass
  #   elif sum(int(j) for j in list) == inputNum:
  #     list2.insert(i, i)
  #     if sum(int(j) for j in list2) > inputNum:
  #       list2.remove(i)
  #     elif sum(int(j) for j in list2) < inputNum:
  #       while sum(int(j) for j in list2) == inputNum:
  #         list2.insert(i, i)



      # if total <= inputNum:
      #   if total == inputNum:
      #     pass
      #   if total < inputNum:
      #     list.append(i)
      #     list.append(j)
      #     if sum(int(j) for j in list) < inputNum:
      #       #list.append(i)
      #       print(list)
      #
      #   break






  return True


