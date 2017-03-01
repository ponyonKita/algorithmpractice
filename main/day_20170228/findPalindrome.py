
'''
존과 김도균님은 대학에서 문자열 이론을 공부하고 있습니다. 김도균님은 회문을 아주 좋아합니다.
회문은 앞에부터 읽으나, 뒤에서부터 읽으나 같은 단어를 말합니다. 존은 김도균님을 임의의 문자열로
회문을 만들어 김도균님을 깜짝 놀래켜주고 싶습니다. 이때 존은 문자열 뒤에 0 이상의 숫자를 추가해 회문을 생성하려고 합니다.
존이 생성할 수 있는 가장 짧은 회문의 길이를 리턴하세요.

함수정의
find(inputString)

예시 데이터와 출력 데이터
(1) inputString = 'abab'
Returns : 5

(2) inputString = 'abacaba'
Returns : 7

(3) inputString = 'qwerty'
Returns : 11

(4) inputString = 'abdfhdyrbdbsdfghjkllkjhgfds'
Returns : 38

'''

def find(inputString):

    resultString = inputString
    for index, string in enumerate(inputString):

        if palindromeCheck(resultString) == resultString:
            return len(resultString)

        if string != inputString[-(index+1)]:
            reversedString = reverseString(inputString)
            resultString = inputString + reversedString[:(index+1)]

    return len(resultString)

def palindromeCheck(inputString):
    return inputString[::-1]

def reverseString(inputString):
    inputString = inputString[:-1]
    return inputString[::-1]


