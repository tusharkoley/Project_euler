def get_fact(num):
    
    if num==1:
        return 1
    return num*get_fact(num-1)

fact_dict = {}

fact_dict[0]=1

for i in range(1,10):
    fact_dict[i]=get_fact(i)

def get_dgt_from_nbr(num):
    lst = []    
    while num>=10:
        d = num%10
        lst.append(d)
        num = num//10
        
    lst.append(num)    
    return lst[::-1]

def get_fact_sum(num):
    dgt_list = get_dgt_from_nbr(num)
    
    sm=0
    for dgt in dgt_list:
        sm+=fact_dict[dgt]
    return sm

s=0
for i in range(10,1000_000):
    if get_fact_sum(i)==i:
        s+=i

print(s)
