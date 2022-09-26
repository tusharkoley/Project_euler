
def get_fib_seq(num):
    
    return fib_dict[num-1]+fib_dict[num-2]

fib_dict={}
fib_dict[1]=1
fib_dict[2]=1

curr_fib=1
i=3
while len(str(curr_fib))<1000:
    curr_fib=get_fib_seq(i)
    fib_dict[i] = curr_fib    
    i+=1

print(i-1)