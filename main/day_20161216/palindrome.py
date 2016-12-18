


def palindrome(inputNumber):

    checkCount = 0
    nextNumber = inputNumber

    while checkCount < 100:

        checkCount += 1
        nextNumber = nextNumber + reverseNumber(nextNumber)

        if nextNumber == reverseNumber(nextNumber):
            result = str(inputNumber) + ' ' + str(checkCount) + ' ' + str(nextNumber)
            return result


    return str(inputNumber) + ' is not palindrome'


def reverseNumber(inputNumber):

    stringNumber = str(inputNumber)
    reverseNumber = stringNumber[::-1]

    return int(reverseNumber)


