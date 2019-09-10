num1 = int(input('Enter 1st Number : '))
num2 = int(input('Enter 2nd Number : '))
num3 = int(input('Enter 3rd Number : '))

if((num1 > num2) & (num1 > num3)):
    print('num1 is greast number ', num1)
elif((num2 > num1) & (num2 > num3)):
    print('num1 is greast number ', num2)
elif((num3 > num1) & (num3 > num2)):
    print('num1 is greast number ', num3)
else :
    print('Not Distinct number ')
