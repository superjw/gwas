with open('tmp', 'r') as f:
    lst = []
    for l in f:
        efo = l.strip().split('\t')[1]
        lst.append(efo)
    print(lst)
    print('========================================')
    print(set(lst))
    print(len(set(lst)))