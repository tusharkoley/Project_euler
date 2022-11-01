def get_trunc_nbrs(num):
    
    lst = []
    n=num
    while n>0:
        lst.append(n)
        n=n//10
    
    n=num
    div=10
    while n>div:
        div=div*10
        
    div = div//10
    
    while n>0:
        n=n%div
        div=div//10
        lst.append(n)
        
    return lst[:-1]


def is_prime(num):
    if num==2:
        return True    
    if num%2 ==0 :
        return False    
    for i in range(3,int(num**.5)+1,2): 
        if num%i==0:
            return False        
    return True 


prime_dict = {}
prime_dict[1]=False
for num in range(2,1000_000):
    prime_dict[num]=is_prime(num)


cnt=1
tr_prim_lst = []
cur_num = 11

while cnt<=11:
    lst = get_trunc_nbrs(cur_num)
    pr_flag=True
    for num in lst:
        if not prime_dict[num]:
            pr_flag=False
            
    if pr_flag:
        cnt+=1
        tr_prim_lst.append(cur_num)
        # print(cur_num)
        
    cur_num=cur_num+2


print(sum(tr_prim_lst))