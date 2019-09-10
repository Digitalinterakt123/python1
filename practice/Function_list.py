
def count(lst) :
    even = 0
    odd = 0
    for i in lst :
        if(i % 2 == 0) :
            even += 1
        else :
            odd += 1
    return even, odd



lst = [10, 20, 25, 30, 90, 13, 65, 7, 41]
even, odd = count(lst)

print(even)
print(odd)