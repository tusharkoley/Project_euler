max_num = 6*9**5

def get_dgt_sm(p):
    lst = []
    for i in range(2,max_num):
        if i==get_dgt_pow_sm(i,p):
            lst.append(i)
    return sum(lst)


def get_dgt_pow_sm(num, p):
    s=0
    for d in str(num):
        s+=(int(d))**p
    return s


print(get_dgt_sm(5))