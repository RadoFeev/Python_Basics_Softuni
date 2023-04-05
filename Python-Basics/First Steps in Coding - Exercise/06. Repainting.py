# •	Предпазен найлон - 1.50 лв. за кв. метър
# •	Боя - 14.50 лв. за литър
# •	Разредител за боя - 5.00 лв. за литър
# 1.	Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
# 2.	Необходимо количество боя (в литри) - цяло число в интервала [1…100]
# 3.	Количество разредител (в литри) - цяло число в интервала [1…30]
# 4.	Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]
protective_nylon = 1.50
paint = 14.50
paint_thinner = 5
needed_quantity_nylon = int(input())
needed_quantity_paint = int(input())
amount_of_thinner = int(input())
hour_workers_job_done = int(input())
price_nylon = (needed_quantity_nylon + 2) * protective_nylon
price_paint = (needed_quantity_paint + (needed_quantity_paint * 0.1)) * paint
price_paint_thinner = paint_thinner * amount_of_thinner
price_for_nylon = 0.40
all_sum = price_nylon + price_paint + price_paint_thinner + price_for_nylon
sum_for_worker_to_pay = (all_sum * 0.3) * 8
final_pay = all_sum + sum_for_worker_to_pay
print(final_pay)