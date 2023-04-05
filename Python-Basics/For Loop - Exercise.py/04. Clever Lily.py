age_of_lily = int(input())
washing_mashine_price = float(input())
price_of_toy = int(input())
saved_money = 0
numbers_of_toys = 0

for num in range(1, age_of_lily + 1):

    if num % 2 == 0:
        saved_money += ((num / 2) * 10) - 1
    else:
        numbers_of_toys += 1


total_saved_money = saved_money + (numbers_of_toys * price_of_toy)
diff = abs(total_saved_money - washing_mashine_price)

if total_saved_money >= washing_mashine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')