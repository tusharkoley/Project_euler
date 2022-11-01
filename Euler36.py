def get_dgt_from_nbr(num, div=10):
    
    lst = [] 
    while num>=div:
        d = num%div
        lst.append(d)
        num=num//div
    lst.append(num)
    return lst[::-1]

def is_pal(lst):
    return lst==lst[::-1]


lst = []

for num in range(1000_000):
    lst_num = get_dgt_from_nbr(num)
    lst_bin = get_dgt_from_nbr(num,2)
    
    if is_pal(lst_num) and is_pal(lst_bin):
        lst.append(num)

print(sum(lst))