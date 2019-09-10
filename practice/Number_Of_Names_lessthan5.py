def count(list) :
    more = 0
    less = 0

    for i in range(len(list)) :
        if(len(list[i]) > 5) :
            more += 1
        else :
            less += 1
    return more, less


list = []

size = int(input("Enter List Size : "))

for i in range(size):
    list.append(input())

more, less = count(list)

print("Morethan 5 char {} less than 5 char {}".format(more, less))