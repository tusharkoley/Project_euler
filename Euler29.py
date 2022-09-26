all_nums = set()
for a in range(2,101):
    for b in range(2,101):
        all_nums.add(a**b)

print(len(all_nums))