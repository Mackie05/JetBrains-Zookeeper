deposit = input()
year_counter = 0
while int(deposit) <= 700000:
    deposit = int(deposit) * 1.071
    year_counter += 1
    if int(deposit) > 700000:
        print(year_counter)