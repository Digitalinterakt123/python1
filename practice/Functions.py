# def add(x, y) :
#     return (x + y)
#
# print(add(3, 5))

# def student(name, study) :
#     study = 'mca'
#     print('Name : ',name)
#     print('Study : ',study)
#
# # student('praneeth', 'mca')
# # student(study='mca', name='praneeth')
# student(name='ntr',study='mba')


def add(*b) :
    c = 0

    for i in b :
        c = c + i
    print(c)


add(2, 3, 4, 5, 10)
