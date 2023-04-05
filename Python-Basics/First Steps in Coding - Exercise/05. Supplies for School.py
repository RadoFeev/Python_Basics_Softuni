# Пакет химикали - 5.80 лв.
# Пакет маркери - 7.20 лв.
# Препарат - 1.20 лв (за литър)
# Брой пакети химикали - цяло число в интервала [0...100]
# Брой пакети маркери - цяло число в интервала [0...100]
# Литри препарат за почистване на дъска - цяло число в интервала [0…50]
# Процент намаление - цяло число в интервала [0...100]
pack_of_pen = 5.80
pack_of_marker = 7.20
preparation_for_liter = 1.20
num_pack_pen = int(input())
num_pack_marker = int(input())
lither_all = int(input())
percentage = int(input())
in_percentage = percentage / 100
price_for_pen = pack_of_pen * num_pack_pen
price_for_marker = pack_of_marker * num_pack_marker
price_liter = preparation_for_liter * lither_all
cost = price_liter + price_for_pen + price_for_marker
final_res = cost - (cost * in_percentage)
print(final_res)

