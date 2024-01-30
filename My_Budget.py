import prettytable

print('Monthly Budget')

income = {
          1: ["Przychód", int(input('Define your monthly income: '))],
          2: ["ZUS", int(input('Define ZUS amount: '))],
          3: ["Podatek", int(input('Define Tax amount: '))],
          4: ["VAT", int(input('Define VAT amount: '))],
          5: ["Księgowa", int(input('Define accountant costs: '))],
          6: ["Dochód", "Here goes a sum of costs minus income value"],
          }
print("{:<10} {:<10} ".format('Nazwa', 'Kwota'))

for key, value in income.items():
    name, sum  = value
    print("{:<10} {:<10}".format(name, sum))


