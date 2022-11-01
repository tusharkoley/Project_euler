nums = []
dens = []
for i in range(10,100):
    for j in range(i+1,100):        
        num = i//10
        cmn1 = i%10
        den = j%10
        cmn2 = j//10        
        if den!=0 and i/j==num/den and cmn1==cmn2:           
            # print(i,j)            
            if den%num==0:
                den=den//num
                num=1            
            nums.append(num)
            dens.append(den)


num_mult = 1
for i in nums:
    num_mult*=i

den_mult = 1
for i in dens:
    den_mult*=i

print(den_mult//num_mult)