def prettylist(l):
    for i in l:
        if i == l[-1]:
            print(l[-1])
            break
        print(i, end = ", " if i != l[-2] else " and ")


spam = ['apples', 'bananas', 'tofu', 'cats', 'dildos', 'oranges', 'pussy', 'dick', 'ass', 'tits']
prettylist(spam)