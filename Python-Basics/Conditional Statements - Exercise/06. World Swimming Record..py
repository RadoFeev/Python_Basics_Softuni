import math
record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())
Ivan_have_to_swim = distance_in_meters * time_in_seconds_for_one_meter
time_he_delay = int(distance_in_meters / 15) * 12.5
sum_time = Ivan_have_to_swim + time_he_delay
if sum_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {sum_time:.2f} seconds.")
else:
    diff = sum_time - record_in_seconds
    print(f"No, he failed! He was {diff:.2f} seconds slower.")