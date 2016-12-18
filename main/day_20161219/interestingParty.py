

class InterestingParty:

    def __init__(self):
        pass

    def bestInvitation(self, first, second):
        result = 1
        countList = []
        allList = first + second
        for index in range(len(allList)):
            count = allList.count(allList[index])
            countList.append(count)
            result = max(countList)

        return result


