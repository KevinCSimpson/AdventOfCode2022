from operator import truediv


with open('day01\sample1.txt','r') as reader:
    raw = reader.read()
elves = raw.split('\n\n')
calorieTotals = []
for elf in elves:
    calorieTotal = 0
    snacks = elf.split('\n')
    for snack in snacks:
        calorieTotal = calorieTotal + int(snack)
    calorieTotals.append(calorieTotal)
calorieTotals.sort(reverse = True)
print(calorieTotals[0] + calorieTotals[1] + calorieTotals[2])
