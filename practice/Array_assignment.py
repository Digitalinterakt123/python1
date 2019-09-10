from numpy import *

# arr = array([1, 2, 3, 4, 5])
# # Adding 5 to the each value in the array
#
# # for i in range(len(arr)) :
# #     arr[i]+= 5
#
# arr = arr + 5
# print(arr)

arr1 = array([
                [1, 2, 3, 4],
                [9, 8, 7, 6]
            ])

arr2 = arr1.reshape(4,2)
print(arr2)
