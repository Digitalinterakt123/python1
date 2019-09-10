def details(name, **data):
    print(name)

    for i, j in data.items() :
        print(i, j)


details('praneeth', age = 28, stream = 'mca', mob = 9493011497)