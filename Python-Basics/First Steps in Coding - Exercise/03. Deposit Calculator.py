# сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
deposit_sum = float(input())
months = int(input())
percent = float(input())
total_sum = deposit_sum + months * ((deposit_sum * (percent / 100)) / 12)
print(total_sum)


