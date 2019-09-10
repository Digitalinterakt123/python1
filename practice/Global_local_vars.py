
a = 10

def something():
    global a
    a = 20
    print("local var : ", a)



something()
print("Global var : ", a)