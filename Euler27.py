def is_prime(num):
    if num==2:
        return True    
    if num%2 ==0 :
        return False    
    for i in range(3,int(num**.5)+1,2): 
        if num%i==0:
            return False        
    return True

def get_quadric_prime_cnt(a,b):    
    n=0
    y = b
    cnt=0
    pr_lst = []
    while is_prime(y):
        n+=1
        pr_lst.append(y)
        y = n**2+a*n+b        
        cnt+=1        
   
    return cnt


mx=0
mx_a=0
mx_b =0
for a in range(-999,999,2):
    for b in range(-999,999,2):
        try:
            cnt = get_quadric_prime_cnt(a,b)
            if cnt>mx:
                    mx=cnt
                    mx_a=a
                    mx_b=b
                    
        except:
            pass



print(mx_a*mx_b)