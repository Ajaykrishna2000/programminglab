import csv
field_name = ['No', 'Company', 'Car Model']
car = [{'No' : 1, 'Company' : 'Ferrari',  'Car Model' : 'F8'},
       {'No' : 2, 'Company' : 'BMW',  'Car Model' : 'M6'},
       {'No' : 3, 'Company' : 'Bugatti',  'Car Model' : 'Chiron'},
       {'No' : 4, 'Company' : 'Benz',  'Car Model' : 'AMG-GT'},
       {'No' : 5, 'Company' : 'Audi',  'Car Model' : 'R8'}]
with open('sports.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames= field_name)
    writer.writeheader()
    writer.writerows(car)

with open('sports.csv', newline='') as csvfile:
    d = csv.reader(csvfile, delimiter='|')
    for r in d:
        print(','.join(r))