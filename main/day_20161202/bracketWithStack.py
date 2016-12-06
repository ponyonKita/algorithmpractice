
# 괄호(parentheses) 란,
# 문장부호의 하나. 수식이나 문장 등에서 어느 부분을 다른 부분과 구별하거나 강조하기 위하여 그 앞뒤에 치는 기호로 묶음표라고 하며 기호는 (), { }, , 〔 〕, [ ], 「 」, (()), 《 》, 〚〛, 〖 〗, 『 』 등이 있다.
#
# 계산기를 구현하기에 앞서 수식에 괄호가 정상적으로 열고 닫혔는지 검사할 필요가 있다.
# 아래 6가지 경우에 대해서 정상여부를 판단하고 스택(Stack)으로 구현하시오.
#
# ‘{2 + 4 x (3 + 5)}’ -> True
# ‘[3 + 2 / (7 x 2] }’ -> False
# ‘(4 + 1) x (3 x 4)’ -> True
# ‘3 * 2 + [4 x 3]’ -> True
# ‘(){[]}’ -> True
# ‘[3 + 2] x 4 + (3 + 6}’ -> False


class CustomStack():
    def __init__(self):
        self.stack = []

    def push(self, parameter):
        return self.stack.append(parameter)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []


def openBracket(bracketList, inputString):
    return inputString in bracketList.keys()

def closeBracket(bracketList, inputString):
    return inputString in bracketList.values()

def isPairBracket(bracketList, stackValue, inputString):
    return bracketList.get(stackValue) == inputString

def bracketCheckWithStack(inputString):
    stack = CustomStack()

    bracketList = {
        '{': '}',
        '(': ')',
        '〔': '〕',
        '[': ']',
        '「': '」',
        '((': '))',
        '《': '》',
        '〚': '〛',
        '〖': '〗',
        '『': '』'
    }

    for checkString in inputString:

        if openBracket(bracketList, checkString):
            stack.push(checkString)
        elif closeBracket(bracketList, checkString):
            if stack.isEmpty():
                return False
            if isPairBracket(bracketList, stack.pop(), checkString):
                return False

    return stack.isEmpty()




