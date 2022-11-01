all_dgt_set = set('123456789')

def is_pan_digit(a,b,c):
    all_dgits = str(a) + str(b) + str(c)
    
    if len(all_dgits)!=9:
        return False
    return set(all_dgits)==all_dgt_set


all_product = []
for i in range(99):    
    if i%11==0 or i%10==0:
        continue    
    for j in range(99,9999):        
        if j%10==0:
            continue        
        if is_pan_digit(i,j,i*j):
            # print(i,j)
            all_product.append(i*j)


print(sum(set(all_product)))