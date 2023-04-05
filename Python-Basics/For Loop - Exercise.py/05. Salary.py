facebook = 150
instagram = 100
reddit = 50
salary_condition = True
n = int(input())
salary = int(input())
for i in range(n):
    name_of_website = str(input())
    if name_of_website == 'Facebook':
        salary -= 150
    elif name_of_website == 'Reddit':
        salary -= 50
    elif name_of_website == 'Instagram':
        salary -= 100

    if salary <= 0:
        salary_condition = False
        break
if salary_condition:
    print(salary)
else:
    print(f'You have lost your salary.')