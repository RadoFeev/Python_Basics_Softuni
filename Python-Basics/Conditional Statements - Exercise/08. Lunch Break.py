import math
name_of_the_serial = input()
movie_duration = int(input())
break_duration = int(input())
time_for_lunch = break_duration / 8
time_for_break = break_duration / 4
left_time = break_duration - time_for_lunch - time_for_break
diff = abs(left_time - movie_duration)
if left_time >= movie_duration:
    print(f"You have enough time to watch {name_of_the_serial} and left with {math.ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_the_serial}, you need {math.ceil(diff)} more minutes.")
