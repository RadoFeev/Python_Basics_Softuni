number_of_climbers = int(input())
musala = 0
kilimandjaro = 0
k2 = 0
everest = 0
monblan = 0
all_climbers = 0

for _ in range(number_of_climbers):
    current_climbers = int(input())
    all_climbers += current_climbers

    if current_climbers <= 5:
        musala += current_climbers
    elif 6 <= current_climbers <= 12:
        kilimandjaro += current_climbers
    elif 13 <= current_climbers <= 25:
        k2 += current_climbers
    elif 26 <= current_climbers <= 40:
        everest += current_climbers
    elif current_climbers >= 41:
        monblan += current_climbers

musala = musala / all_climbers * 100
kilimandjaro = kilimandjaro / all_climbers * 100
k2 = k2 / all_climbers * 100
everest = everest / all_climbers * 100
monblan = monblan / all_climbers * 100

print(f'{musala:.2f}%')
print(f'{kilimandjaro:.2f}%')
print(f'{k2:.2f}%')
print(f'{everest:.2f}%')
print(f'{monblan:.2f}%')