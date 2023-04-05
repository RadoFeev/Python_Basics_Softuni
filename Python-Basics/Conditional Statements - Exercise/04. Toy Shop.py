price_on_vacation = float(input())
num_saws = int(input())
num_talking_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_truck = int(input())

order_sum = num_saws * 2.60 + num_talking_dolls * 3 + num_bears * 4.10 + num_minions * 8.20 + num_truck * 2
order_toys = num_saws + num_talking_dolls + num_bears + num_minions + num_truck
if order_toys >= 50:
	order_sum -= order_sum * 0.25
rent = order_sum * 0.10
profit = order_sum - rent
diff = abs(profit - price_on_vacation)
if profit >= price_on_vacation:
	print(f"Yes! {diff:.2f} lv left.")
else:
	print(f"Not enough money! {diff:.2f} lv needed.")