# Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999]
year_tax = int(input())
# Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
basketball_shoe = year_tax - (year_tax * 0.4)
basketball_tech = basketball_shoe - (basketball_shoe * 0.2)
basketball_ball = basketball_tech / 4
basketball_ace = basketball_ball / 5
all_sum = year_tax + basketball_shoe + basketball_tech + basketball_ball + basketball_ace
print(all_sum)