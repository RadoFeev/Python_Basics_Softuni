# Ако числото е до 100 включително, бонус точките са 5; - < 100 bonus 5
# Ако числото е по-голямо от 100, бонус точките са 20% от числото; - > 100 * 0.2
# Ако числото е по-голямо от 1000, бонус точките са 10% от числото.>1000 * 0.1

number = int(input())
bonus_points = 0

if number <= 100:
    bonus_points = 5
elif 100 < number <= 1000:
    bonus_points = number * 0.2
elif number > 1000:
    bonus_points = number * 0.1

if number % 10 == 5:
    bonus_points += 2
elif number % 2 == 0:
    bonus_points += 1
all_points = (number + bonus_points)
print(bonus_points)
print(all_points)