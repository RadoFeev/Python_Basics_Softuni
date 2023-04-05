hour_exam = int(input())
minutes_exam = int(input())
time_arrived = int(input())
minutes_arrived = int(input())
exam_time_in_minutes = (hour_exam * 60) + minutes_exam
arrive_time_in_minutes = (time_arrived * 60) + minutes_arrived
diff = abs(exam_time_in_minutes - arrive_time_in_minutes)
hour = diff // 60
minutes = diff % 60
if exam_time_in_minutes == arrive_time_in_minutes:
    print('On time')
elif exam_time_in_minutes > arrive_time_in_minutes:
    if diff <= 30:
        print('On time')
        print(f'{diff} minutes before the start')
    elif 30 < diff <= 59:
        print('Early')
        print(f'{diff} minutes before the start')
    else:
        print('Early')
        print(f'{hour}:{minutes:02d} hours before the start')
elif exam_time_in_minutes < arrive_time_in_minutes:
    print('Late')
    if diff < 60:
        print(f'{diff} minutes after the start')
    else:
        print(f'{hour}:{minutes:02d} hours after the start')