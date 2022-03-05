d1 = {"Fruit": "Apple", "Climate": "Cold"}
d2 = {"Price": "100", "Quantity": "1kg"}
d = d1.copy()
d.update(d2)
print("First dictionary:", d1)
print("Second dictionary:", d2)
print("After merging dictionaries:", d)