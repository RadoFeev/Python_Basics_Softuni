budget = float(input())
number_video_cards = int(input())
number_processor = int(input())
number_ram_memory = int(input())
price_video_cards = number_video_cards * 250
price_processor = price_video_cards * 0.35
price_ram_memory = price_video_cards * 0.10
all_price = price_video_cards + number_processor * price_processor + number_ram_memory * price_ram_memory
if number_video_cards > number_processor:
    all_price -= all_price * 0.15
if all_price < budget:
    needed_money = budget - all_price
    print(f"You have {needed_money:.2f} leva left!")
else:
    diff = all_price - budget
    print(f"Not enough money! You need {diff:.2f} leva more!")