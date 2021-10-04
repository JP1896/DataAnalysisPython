
def compareDataUnits(value1, value2):
    if value1 > value2:
        totalUnits = value1 - value2
        totalUnitsPercentage = abs(((totalUnits/value1)*100))
        print('Total Decrease:', totalUnitsPercentage,'%')
    elif value1 < value2:
        totalUnits = value1 - value2
        totalUnitsPercentage = abs(((totalUnits / value1) * 100))
        print('Total Growth:', totalUnitsPercentage, '%')

