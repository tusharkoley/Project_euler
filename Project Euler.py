#!/usr/bin/env python
# coding: utf-8

# ### Problem Number 1

# In[4]:


def get_sum_by3n5(num):    
    s=0
    for i in range(1000):

        if i%3 == 0 or i%5==0:
            s+=i
        
    return s


# In[5]:


get_sum_by3n5(1000)


# #### Problem # 2

# In[6]:


def fib(num):
    if num==1 or num==2:
        return num
    return fib(num-1)+fib(num-2)


# In[47]:


# for i in range(1,11):
#     print(fib(i))

num=0
i=2
s=0
while num <=4000_000:
    num=fib(i)
    i+=1
    if num%2==0:
        s+=num
    
print(s)


# #### Problem#3

# In[29]:


def is_prime(num):
    if num==2:
        return True    
    if num%2 ==0 :
        return False    
    for i in range(3,int(num**.5)+1,2): 
        if num%i==0:
            return False        
    return True
    


# In[30]:


is_prime(35)


# In[34]:


num = 13195
fac = int(num**0.5)
if fac%2==0:
    fac+=1


# In[35]:


fac


# In[36]:


for i in range(fac,3,-2):
    if is_prime(i):
        if num%i==0:
            print(i)


# In[37]:


num = 600851475143
fac = int(num**0.5)
if fac%2==0:
    fac+=1
for i in range(fac,3,-2):
    if is_prime(i):
        if num%i==0:
            print(i)
            #break


# #### Problem #4

# In[79]:


def is_palindrome(num):
    return str(num)==str(num)[::-1]


# In[82]:


is_palindrome(1112)


# In[102]:


max_j = 100
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if is_palindrome(i*j):            
            max_j = max(j, max_j)
            print(i,j, i*j)
            break
            
    if i < max_j:
        break


# #### Problem # 5

# In[165]:





# In[45]:


def get_smallest_div_nbr(n):
    num=1
    factors =[]
    for new_fac in range(2,n+1):
        for fac in factors:        
            if new_fac%fac==0:
                new_fac=new_fac//fac

        num=num*new_fac
        factors.append(new_fac)
    return num


# In[46]:


get_smallest_div_nbr(10)


# In[41]:


get_smallest_div_nbr(20)


# #### Problem #6

# In[176]:


def get_diff_sum_sq(num):
    
    return (num*(num+1)//2)**2 - sum([i**2 for i in range(num+1)])


# In[177]:


get_diff_sum_sq(10)


# In[178]:


get_diff_sum_sq(100)


# ### Problem  #7

# In[65]:


def get_nth_prime(n):
    
    last_prime = 3    
    prime_cnt = 3        
    while prime_cnt <= n :        
        last_prime = get_next_prime(last_prime+2)        
        prime_cnt+=1             
    return last_prime
                    


# In[66]:


get_nth_prime(2)


# In[229]:


get_nth_prime(10001)


# In[53]:


def get_next_prime(num):
    
    if num%2==0:
        num+=1        
    while not is_prime(num):
        num+=2        
    return num


# In[57]:


get_next_prime(2)


# #### Problem Nmber 8

# In[230]:


s_num = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""


# In[233]:


s_num = s_num.replace("\n",'')


# In[236]:


def get_prodcut(s_num):
    p=1
    for s in s_num:
        p*=int(s)
    return p


# In[255]:


def get_max_product(size):
    max_product = 0
    for i in range(1000-size+1):
        product = get_prodcut(s_num[i:i+size])
        if product>max_product:
            max_product = product
    
    return max_product
    


# In[258]:


get_max_product(10)


# #### Problem # 9

# In[259]:


def is_pytho_trip(a,b,c):
    
    return c**2==(a**2+b**2)


# In[262]:


is_pytho_trip(3,4,5)


# In[ ]:


a<b<c <1000
a+b+c=1000
a,b,c >0
a,b <500 
c=1000-a-b


# In[270]:


for a in range(500):
    for b in range(a,500):        
        if is_pytho_trip(a,b,1000-a-b):
            print(a,b)
    


# In[271]:


a=200
b=375
c=(1000-a-b)


# In[273]:


a*b*c


# #### Problem # 10

# In[38]:


get_next_prime(9)


# In[35]:


def is_prime(num):
    if num==2:
        return True    
    if num%2 ==0 :
        return False    
    for i in range(3,int(num**.5)+1,2): 
        if num%i==0:
            return False        
    return True
def get_next_prime(num):
    
    if num%2==0:
        num+=1        
    while not is_prime(num):
        num+=2        
    return num


# In[293]:


def get_prim_sum(u_limit):
    pr_num = 2
    sm = 0
    while pr_num <u_limit:   
        sm+=pr_num 
        pr_num = get_next_prime(pr_num+1)

    return sm
    


# In[295]:


get_prim_sum(2000_000)


# #### Problem Number 11

# In[39]:


st_mat = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""


# In[40]:


rows = st_mat.split("\n")


# In[47]:


import numpy as np
mat = np.zeros((20,20))
for index,row in enumerate(rows):
    mat[index,:] = row.split()
        


# In[52]:


size=4
tot_len = 20
product = 0
prod_lst = []
for i in range(tot_len):
    for j in range(tot_len):
        rgt_prod = np.product(mat[i,j:j+size])
        bottom_pord = np.product(mat[i:i+size,j])
        diog_prod1 = np.product(mat[i:i+size,j:j+size].diagonal())         
        diog_prod2 = np.product(np.fliplr(mat[i:i+size,j:j+size]).diagonal())    
        
        mx = max([rgt_prod, bottom_pord, diog_prod1,diog_prod2])        
        if mx>product:
            product = mx
        


# In[50]:


product


# #### Problem number 12

# In[125]:


def get_trng_nbr(num):
    return num*(num+1)//2

def get_num_of_divisor(num):        
    n_div=0 
    for i in range(2,num//2+1):        
        if num%i==0:
            n_div+=1            
    return n_div+2
            


# In[127]:


get_num_of_divisor(9*2)


# In[ ]:





# In[118]:


num = 0
n_div=1
size = 5
while n_div<size:   
    if num%2==0:
        n_div = get_num_of_divisor(num//2)*get_num_of_divisor(num+1)
    else:
        n_div = get_num_of_divisor(num)*get_num_of_divisor((num+1)//2)
        
    num+=1


# In[100]:





# #### Problem # 13

# In[128]:


s = """37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690"""


# In[129]:


lst = s.split()


# In[131]:


lst_num = list(map(int, lst))


# In[559]:


sm = sum(lst_num)


# In[560]:


sm


# In[561]:


len("5537376230")


# #### Problem Number 14

# In[139]:


def get_next_seq_num(num):
    
    if num%2==0:
        return num//2
    else:
        return 3*num+1
    


# In[133]:


seq_dict = {}


# In[140]:


def gen_seq(num):
    seq = []
    n=num    
    while n !=1:
        try:
            return (seq + seq_dict[n])
        except:
            n= get_next_seq_num(n)
            seq.append(n)     
    return seq
 


# In[141]:


gen_seq(13)


# In[142]:


for i in range(2,1000_000):
    seq_dict[i]=gen_seq(i)
   


# In[143]:


max_len =0 
max_key = 0
for key, val in seq_dict.items():    
    if len(val) > max_len:        
        max_len = len(val)
        max_key = key
           


# In[144]:


max_len, max_key


# #### Problem number 15

# In[ ]:


2, 6, 2 + (6+6*2)


# #### Problem # 16

# In[639]:


def get_sum_sq(n):    
    num = 2**n    
    sm=0    
    for d in str(num):
        sm+=int(d)
    return sm
        
    


# In[641]:


get_sum_sq(15)


# In[642]:


get_sum_sq(1000)


# #### Problem # 17

# In[645]:


len("three hundred and forty-two".replace(' ','').replace('-',''))


# In[646]:


2+18+24


# #### Problem # 15

# In[16]:


size =20
arr = np.ones([size+1, size+1])


# In[27]:


for i in range(19,-1,-1):
    for j in range(19,-1,-1):
        arr[i][j] = arr[i+1][j] + arr[i][j+1]


# In[28]:


arr[0][0]


# #### Problem # 17

# In[87]:





# In[878]:


d_nbr = {}
words = ['one','two','three','four','five','six','seven','eight','nine','ten',         'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen',         'nineteen','twenty']

for idx,word in enumerate(words):
    d_nbr[idx+1]=word
    
d_nbr[30]='thirty'
d_nbr[40]='forty'
d_nbr[50]='fifty'
d_nbr[60]='sixty'
d_nbr[70]='seventy'
d_nbr[80]='eighty'
d_nbr[90]='ninety'
d_nbr[100]='hundred'
d_nbr[1000]='one thousand'  
d_nbr[0]=''


# In[877]:


def get_words_from_nbr(num):
    st=''  
    d2 = num//100
    num=num%100
    d1 = num//10
    d0=num%10
    if d2!=0:
        st+=d_nbr[d2]+'hundred'        
        if d1!=0 or d0!=0:
            st+=' and ' 
    if d1==1:
        st+=d_nbr[num]
    else:
        st+=d_nbr[d1*10]
        st+=d_nbr[d0]
    return st
    


# In[879]:


get_words_from_nbr(14)


# In[881]:


s=0
for i in range(1,1000):
    
    word = get_words_from_nbr(i)

    
    s+=len(word.replace(' ',''))
    


# In[883]:


s


# In[29]:


s_tran = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


# In[30]:


lines = s_tran.split('\n')
sm=0
for line in lines:
    mx_line = max(map(int,line.split()))
    sm+=mx_line


# In[31]:


sm


# In[26]:



(map(int,lines[9].split()))


# #### Problem# 18

# In[891]:


st_num = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


# In[894]:


data = []

for line in st_num.split('\n'):
    data.append(line.split())
    
    


# In[977]:


l=15
paths = [[0]]
for i in range(1,l): ## Position of total Depth
    new_path = []    
    for j in range(l):        
        for path  in paths: # Paths contain path upto level i           
            if path[-1]==j: ## Parent Position is j
                 new_path.append((path+[j])) ## add j as child
            if path[-1]==j-1: ### Parent Position is j-1 ## add j as child
                new_path.append((path+[j]))
                
    paths=new_path
    print(f'Total no of path up to level {i} = {len(paths)}')
    

len(paths)


# In[969]:


2**14


# In[ ]:





# In[898]:


mx = 0
for path in paths:
    sm=0
    for idx, pos in enumerate(path):
        sm+=int(data[idx][pos])
        
    if sm>mx:
        mx=sm
    


# In[899]:


mx


# In[57]:


# 0  L0
# 00 01 L1
# 000 001 011 012 L2

# 0000 0001 0011 0012 0111 0112 0122 0123 L3



# f_path = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]


# #### Project Euler Problem # 19

# In[378]:


# start_dt = "1 Jan 1900"
# end_dt = "31 Dec 2000"
# def get_num_date(str_date):
    
#     day, mon, year = str_date.split()
#     day = int(day)
#     mon = mon_idx_dict[mon.capitalize()]
#     year = int(year)
    
#     return day, mon, year
# st_day, st_mon, st_year = start_dt.split()

# st_day = int(st_day)
# st_mon = mon_idx_dict[st_mon]
# st_year = int(st_year)

# def get_no_of_days_year(year):
#     n_days = 0    
#     for i in range(1,13):        
#         n_days+=get_no_days_mon(i,year)
#     return n_days

# day_diff = 0
# mon_diff = 0
# yr_diff = 0

# if end_day < st_day:   
#     day_diff = (get_no_days_mon(st_mon, st_year)- st_day) + end_day + 1
#     st_mon+=1
# else:
#     day_diff = end_day - st_day + 1
    
# if end_mon < st_mon:
#     mon_diff = 12 - st_mon + end_mon
#     st_year+=1
# else:
#     mon_diff = end_mon - st_mon
    
# yr_diff = end_year - st_year


# In[905]:


mon_day_dict = {1:31, 2:28, 3:31,4:30, 5:31, 6:30,7:31,8:31,9:30,10:31,11:30,12:31}


def get_no_days_mon(mon, year):
    
    if (mon!=2) :
        return mon_day_dict[mon]
    elif year%4==0 and (year%100 !=0 or year%400==0):
        return 29
    else:
        return 28


# In[906]:



curr_day = 2 # First jan 1900 was Monday Hence First jan 1901 was Tuesday (sun-0, mon-1, tue-2)
cnt=0
for num in range(1,1200):    
    mon = num%12+1
    prev_mon = mon-1
    if prev_mon==0:
        prev_mon=12
    year = 1901 + num//12
    curr_day = curr_day + get_no_days_mon(prev_mon,yr) 
    
    if curr_day%7==0:
        cnt+=1
 
print(cnt)


# #### Problem # 20

# In[393]:


def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)


# In[396]:


fact_num = fact(100)


# In[398]:


sm=0
for s in str(fact_num):
    sm+=int(s)


# In[399]:


sm


# #### Problem # 21

# In[416]:


def get_divs(num):        
    divs = [1]
    for i in range(2,num//2+1):        
        if num%i==0:
            divs.append(i)            
    return divs


# In[419]:


ls1 = get_divs(220)


# In[418]:


sum_div_dict = {}


# In[444]:


for i in range(1,10000):
    sum_div_dict[i] = sum(get_divs(i))


# In[476]:


am_lst = []

for i in range(1,10000):
    try:
        if sum_div_dict[sum_div_dict[i]]==i and sum_div_dict[i]!=i:
            
            am_lst.append(i)
    except:
        pass


# In[479]:


(am_lst)


# #### Problem # 22

# In[481]:


with open('p022_names.txt') as f:
    data = f.read()


# In[490]:


data = data[0]
data = data.replace('"','')
names = data.split(',')
sorted_names = sorted(names)


# In[520]:


alpha_dict = {}

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
for idx, alpha in enumerate(alphabets):
    alpha_dict[alpha]=idx+1


# In[529]:


def get_score_by_name(name):
    sm = 0    
    for l in name:
        sm+=alpha_dict[l]
    return sm


# In[534]:


tot_sum = 0
for idx, name in enumerate(sorted_names):
    tot_sum = tot_sum + (idx+1)*get_score_by_name(name)


# In[535]:


tot_sum


# #### Problem# 23

# In[1764]:


def get_all_div(num):
    
    try:
        return div_dict[num]
    except:
        divs = [1]
        for div in range(2,num//2+1):
            if num%div ==0:
                divs.append(div)            
                return (list_mult(divs,get_all_div(num//div)))

        divs.append(num)
    return divs


# In[1766]:


get_all_div(24)


# In[1765]:





# In[1745]:


div_dict = {}
for i in range(2,28123):
    div_dict[i] = (sorted(get_all_div(i)))


# In[ ]:





# In[1746]:


def list_mult(list1, list2):
    lst = []
    for num1 in list1:
        for num2 in list2:
            lst.append(num1*num2)
            
    return (list(set(lst)))


# In[1748]:


abd_nums = []

for i in range(2,28123):
    if sum(div_dict[i][:-1]) > i:
        abd_nums.append(i)


# In[1749]:


len(abd_nums)


# In[1750]:


abd_nums[-1]


# In[630]:


abd_nums[-2]


# In[633]:


u_lim = 28123


# In[1751]:


abd_sum = set()
for num1 in (abd_nums):
    for num2 in (abd_nums):
        if num1+num2 <u_lim:
            abd_sum.add(num1+num2)
            


# In[1758]:


all_nums = list(range(28123))


# In[1754]:


# abd_sum


# In[650]:


# abd_sum


# In[1759]:


all_nums = set(all_nums)


# In[1760]:


diff = all_nums - abd_sum


# In[1761]:


len(diff)


# In[1762]:


sum(diff)


# In[1763]:


sum(all_nums) - sum(abd_sum)


# #### Problem # 24

# In[653]:


lst = [0,1,2,3,4,5,6,7,8,9]


# In[786]:


def get_list_without_num(num,lst):
    return [n for n in lst if n!=num]


# In[1770]:


def gen_perm(lst):
    perm_lst_out = []    
    if len(lst)==2:
        return [[lst[0],lst[1]],[lst[1],lst[0]]]
    elif len(lst)==1:
        return lst
    else:        
        for num in lst:           
            lst2 = [n for n in lst if n!=num]
            for perm_lst in gen_perm(lst2):        
                perm_lst.insert(0,num)
                perm_lst_out.append(perm_lst)                
    return perm_lst_out


# In[1771]:


perm_list = gen_perm([0,1,2,3,4,5,6,7,8,9])


# In[842]:


lst2 = perm_list[999999]


# In[848]:


''.join(map(str,lst2))


# In[1767]:


def gen_perm2(lst):
    perm_lst_out = []    
    if len(lst)>=3:        
        for num in lst:           
            lst2 = get_list_without_num(num,lst)
            for perm_lst in gen_perm(lst2):        
                perm_lst.insert(0,num)
                perm_lst_out.append(perm_lst)
    else:
        return [[lst[0],lst[1]],[lst[1],lst[0]]]                
    return perm_lst_out


# In[ ]:


def get_list_without_num(num,lst):
    return [n for n in lst if n!=num]


# In[1768]:


perm_lis2 = gen_perm2([0,1,2,3,4,5,6,7,8,9])


# In[ ]:





# In[1769]:


perm_lis2[999999]


# In[ ]:


lst=[2,3,4,5,6,7]


# #### Problem # 25

# In[1772]:


fib_dict={}


# In[ ]:





# In[1773]:


fib_dict[1]=1
fib_dict[2]=1


# In[1774]:


def get_fib_seq(num):
    
    return fib_dict[num-1]+fib_dict[num-2]
    


# In[1782]:


curr_fib=1
i=3
while len(str(curr_fib))<1000:
    curr_fib=get_fib_seq(i)
    fib_dict[i] = curr_fib    
    i+=1
    


# In[1781]:


i


# #### Problem # 26

# In[1791]:


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
        


# In[1800]:


(get_list_den(7))


# In[1796]:


mx=0
mx_idx = 0
for i in range(2,1000):
    val = len(get_list_den(i))
    if val>mx:
        mx=val
        mx_idx=i 
    


# In[1798]:


mx


# In[1799]:


mx_idx


# #### Problem # 27

# In[1432]:


def is_prime(num):
    if num==2:
        return True    
    if num%2 ==0 :
        return False    
    for i in range(3,int(num**.5)+1,2): 
        if num%i==0:
            return False        
    return True


# In[1509]:


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


# In[1510]:


get_quadric_prime_cnt(1,41)


# In[1567]:


get_quadric_prime_cnt(-79,1601)


# In[1560]:


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
            


# In[1568]:


mx_a, mx_b


# In[1569]:


get_quadric_prime_cnt(-61,971)


# In[ ]:


21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13


# #### Problem # 28

# In[1582]:


import numpy as np


# In[1721]:


def get_sprial_mat(n):
    
    if n==1:
        return np.ones((1,1))
    
    mat = np.ones((n,n))    
    mat[1:n-1,1:n-1] = get_sprial_mat(n-2)    
    mat[1:n,n-1]=list(range((n-2)**2 + 1 , (n-2)**2 + n))        
    mat[n-1,0:n-1] = list(range( (n-2)**2 + 2*n-2, (n-2)**2 + n-1,-1))    
    mat[0:n-1,0] = list(range((n-2)**2 + 3*n-3, (n-2)**2 + 2*n-2, -1))    
    mat[0,1:n] = list(range((n-2)**2 + 3*n-2, (n-2)**2 + 4*n-3))
    
    return mat
    
    


# In[1735]:


mat = get_sprial_mat(5)
sum (mat.diagonal()) + sum(np.fliplr(mat).diagonal()) -1


# In[1736]:


mat = get_sprial_mat(1001)
sum (mat.diagonal()) + sum(np.fliplr(mat).diagonal()) -1


# #### Problem # 29

# In[1737]:


all_nums = set()
for a in range(2,101):
    for b in range(2,101):
        all_nums.add(a**b)


# In[1738]:


len(all_nums)


# Problem # 30

# In[1802]:


max_num = 6*9**5
max_num


# In[1740]:


def get_dgt_sm(p):
    lst = []
    for i in range(2,max_num):
        if i==get_dgt_pow_sm(i,p):
            lst.append(i)
    return sum(lst)


# In[1741]:


def get_dgt_pow_sm(num, p):
    s=0
    for d in str(num):
        s+=(int(d))**p
    return s
        


# In[1742]:


get_dgt_sm(4)


# In[1743]:


get_dgt_sm(5)


# In[ ]:




