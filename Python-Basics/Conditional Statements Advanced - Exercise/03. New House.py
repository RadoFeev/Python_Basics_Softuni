type_flowers = input()
num_flowers = int(input())
budget = int(input())
costs = 0
if type_flowers == "Roses":
    costs = num_flowers * 5
    if num_flowers > 80:
        costs -= costs * 0.1
elif type_flowers == "Dahlias":
    costs = num_flowers * 3.8
    if num_flowers > 90:
        costs -= costs * 0.15
elif type_flowers == "Tulips":
    costs = num_flowers * 2.8
    if num_flowers > 80:
        costs -= costs * 0.15
elif type_flowers == "Narcissus":
    costs = num_flowers * 3
    if num_flowers < 120:
        costs += costs * 0.15
elif type_flowers == "Gladiolus":
    costs = num_flowers * 2.50
    if num_flowers < 80:
        costs += costs * 0.20
diff = abs(budget - costs)
if budget >= costs:
    print(f"Hey, you have a great garden with {num_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")