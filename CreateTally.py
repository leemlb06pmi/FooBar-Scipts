def createTally():
    rows = 5
    columns = 3
    array = [[0 for x in range(columns)]for y in range(rows)]
    with open ('input.txt') as ins:
        content = ins.readlines()
        content = [x.strip() for x in content]
        for j in range(rows):
            for k in range(columns):
                array[j][k] = content[j].split(' ')[k]
        print array

createTally()
