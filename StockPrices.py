__author__ = 'Herr'

def my_function (arg):
    min = arg[0]
    max = 0
    for i in arg:
        if i < min:
            min = i
    for j in arg[arg.index(min):]:
        if j > max:
            max = j
    return max, min


list = [10,9,8,7,6,5,4]
print (my_function(list))
