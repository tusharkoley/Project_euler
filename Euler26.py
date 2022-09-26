def  get_list_den(n):
    lst = []
    num = 1
    num_set = set()
    while True:        
        div = num//n
        num = num%n        
        lst.append(div)           
        if num==0 or (num in num_set):
            break              
        num_set.add(num)         
        num=num*10        
    return (lst[1:])


mx=0
mx_idx = 0
for i in range(2,1000):
    val = len(get_list_den(i))
    if val>mx:
        mx=val
        mx_idx=i 


print(mx_idx)