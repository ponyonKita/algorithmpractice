def getFibonacciNumberByIterate(number):
  if number == 0:
    return 0
  elif number == 1:
    return 1
  else:
    return getFibonacciNumberByIterate(number-2)+getFibonacciNumberByIterate(number-1)

