
available = 5

num = int(input("How many Candies you want : "))
i = 1
while i <= num :
    if i > available :
        print("Sorry Out Of Stock")
        break
    print("candy : ", i)
    i += 1
print("bye")