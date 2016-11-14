def getFibonacciNumberByIterate(number):
  if number == 0:
    return 0
  if number == 1:
    return 1
  return getFibonacciNumberByIterate(number-2)-getFibonacciNumberByIterate(number-1)


def getFibonacciNumberByRecursive(number):
  for i in range(10):
    print(getFibonacciNumberByIterate(i))
