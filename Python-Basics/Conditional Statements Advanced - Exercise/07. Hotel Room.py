month = input()
number_of_nights = int(input())
studio = 0
apartment = 0
if month in "May October":
    studio = 50
    apartment = 65
    if 7 < number_of_nights <= 14:
        studio -=  studio * 0.05
    elif number_of_nights > 14:
        studio -= studio * 0.30

elif month in 'June September':
    studio = 75.20
    apartment = 68.70
    if number_of_nights > 14:
        studio -= studio * 0.20

elif month in 'July August':
    studio = 76
    apartment = 77
if number_of_nights > 14:
    apartment -= apartment * 0.10
apartment *= number_of_nights
studio *= number_of_nights
print(f"Apartment: {apartment:.2f} lv." )
print(f"Studio: {studio:.2f} lv.")