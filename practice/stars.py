
# for i in range(1,5):
#     for j in range(i, 5):
#         print(j, end="")
#     print()

x = 'ABCD'
y = 'PQR'
for i in range(4):
    print(x[:i + 1]+y[i:]+" ")

# for i in range(4):
#     for j in range(4):
#         if(j <= i):
#             print(" #", end="")
#     print()
# result :
# #
# # #
# # # #
# # # # #

# for i in range(4):
#     for j in range(4):
#         if(i <= j):
#             print(" #", end="")
#     print()
# result :
# # # # #
# # # #
# # #
# #