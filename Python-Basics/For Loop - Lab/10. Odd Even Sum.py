n = int(input())
odd = 0
even = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        value = int(input())
        even += value
    else:
        value = int(input())
        odd += value
if even == odd:
    print(f'Yes')
    print(f'Sum = {even}')
else:
    print(f'No')
    print(f'Diff = {abs(even - odd)}')