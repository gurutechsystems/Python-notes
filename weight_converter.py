#Converting from kg to lb and vice-versa
weight = int(input('weight: ')) #since we cannot multiply a string by a float, we use int to convert weight to numerical values
unit = input('(L)bs or (K)g: ')

if unit.upper() == "L":
    converted = weight * 0.45
    print(f'your weight is {converted} kilos') #{} are use to dynamic add values
else:
    converted = weight / 0.45
    print(f'your weight {converted} pounds')    