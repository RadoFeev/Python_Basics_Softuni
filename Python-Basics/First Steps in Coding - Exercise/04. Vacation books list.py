# Брой страници в текущата книга – цяло число в интервала [1…1000]
# Страници, които прочита за 1 час – цяло число в интервала [1…1000]
# Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]
num_paper = int(input())
papers_for_one_hour = int(input())
days_which_he_have_to_read = int(input())
all_hours = num_paper // papers_for_one_hour
final_res = all_hours / days_which_he_have_to_read
print(final_res)