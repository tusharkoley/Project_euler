def get_len_int(num):
    l=1
    div=10
    while num>div:
        div*=10
        l+=1
    return l

def concat_nbrs(nums):
    c_num = nums[0]
    
    for num in nums[1:]:
        c_num=c_num*10**get_len_int(num)+num
    return c_num


def get_dgt_from_num(num):
    
    lst = []
    
    while num>=10:
        d = num%10
        lst.append(d)
        num=num//10
        
    lst.append(num)
    return lst[::-1]


def is_pan_dgt(num):
    
    return sorted(get_dgt_from_num(num))==[1,2,3,4,5,6,7,8,9]



pan_lst = []

for num in range(2,9999):
    n=2
    con_num=num
    while get_len_int(con_num)<9:
        con_num = concat_nbrs([con_num,num*n])
        n = n+1
        
        
    if is_pan_dgt(con_num):
        pan_lst.append(con_num)


print(max(pan_lst))