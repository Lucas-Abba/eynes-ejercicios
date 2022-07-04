from random import randint

def listOfAges():
    l = []
    for i in range(10):
        l.append({'id':i, 'edad':randint(1, 100)})
    return l

def sortListOfAges(l):
    sortedList = sorted( l, key=lambda item: item.get('edad'))
    print('El id de la persona mas joven ' + str(sortedList[0].get('id')))
    print('El id de la persona mas vieja ' + str(sortedList[9].get('id')))
    return sortedList


l = listOfAges()
sortedList = sortListOfAges(l)
print('Lista ordenada:')
print(sortedList)