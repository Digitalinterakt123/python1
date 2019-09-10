def fibonacci(n):
    a = 0
    b = 1
    if n > 0 :
        if n == 1 :
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2, n):
                c = a + b
                a = b
                b = c
                if(c < n):
                    print(c)
                else:
                    break;
    else :
        print("please enter positive numbers only")


number = int(input("Enter number : "))
fibonacci(number)