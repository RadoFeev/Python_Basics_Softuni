current_hour = int(input())
current_minutes = int(input())
hours_to_minutes = current_hour * 60
time_plus_15_minutes = hours_to_minutes + current_minutes + 15
hour = time_plus_15_minutes // 60
minutes = time_plus_15_minutes % 60
if hour > 23:
    print(f"0:{minutes:02d}")
else:
    print(f"{hour}:{minutes:02d}")