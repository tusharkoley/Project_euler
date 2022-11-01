def get_circular_nums(num):
    num_lst = []    
    div = 10
    n=0
    while num>=div:
        div = div*10
        n = n+1    
    div=div//10    
    num_lst.append(num)    
    for _ in range(n):        
        f_dgit = num%10        
        other_digits = num//10        
        num = f_dgit*div + other_digits        
        num_lst.append(num)                
    return list(set(num_lst))

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

for i in range(1,1000_000):
    prime_dict[i] = is_prime(i)


cir_prime_lst= []

for i in range(2,1000_000):
    
    prime_flag = True    
    for num in get_circular_nums(i):
        if not prime_dict[num]:
            prime_flag=False
            
    if prime_flag:
        cir_prime_lst.append(i)


print(len(cir_prime_lst))
