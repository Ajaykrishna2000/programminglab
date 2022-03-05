dict1 = {'Ajay': 7, 'Alan': 25, 'Benny': 84, 'Philip': 32}
l = list(dict1.items())
l.sort()
print('Ascending order of sorting is:', l)
l = list(dict1.items())
l.sort(reverse=True)
print('Descending order of sorting is:', l)
