#  Брой пилешки менюта – цяло число в интервала [0 … 99]
#  Брой менюта с риба – цяло число в интервала [0 … 99]
# Брой вегетариански менюта – цяло число в интервала [0 … 99]
num_chicken_menu = int(input())
num_fish_menu = int(input())
num_vegan_menu = int(input())
sum_chicken = num_chicken_menu * 10.35
sum_fish = num_fish_menu * 12.40
sum_vegan = num_vegan_menu * 8.15
total_sum = (sum_chicken + sum_vegan + sum_fish)
desert_sum = total_sum * 0.2
sum_with_delivery = total_sum + desert_sum + 2.50
print(sum_with_delivery)
