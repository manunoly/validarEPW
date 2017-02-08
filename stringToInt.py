__author__ = 'manuel'


def getNumber(stringvar):
    return {
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        '0':0,
    }.get(stringvar,10)

stringvar = raw_input("Please insert String that will be converted to Int:")

stringLength = stringvar.__len__()
finalNumber = 0

for char in stringvar:
    tmpNumber = getNumber(char)
    if (tmpNumber == 10):
        exit("The String can't be convert to Int, Exit!!!")
    for i in range(1,stringLength):
        tmpNumber = tmpNumber * 10
    stringLength -= 1
    finalNumber = finalNumber + tmpNumber
print("Number format to Int")
print(finalNumber)