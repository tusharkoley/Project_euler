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

def list_mult(list1, list2):
    lst = []
    for num1 in list1:
        for num2 in list2:
            lst.append(num1*num2)
            
    return (list(set(lst)))


abd_nums = []

div_dict = {}
for i in range(2,28123):
    div_dict[i] = (sorted(get_all_div(i)))

for i in range(2,28123):
    if sum(div_dict[i][:-1]) > i:
        abd_nums.append(i)



u_lim = 28123
abd_sum = set()
for num1 in (abd_nums):
    for num2 in (abd_nums):
        if num1+num2 <u_lim:
            abd_sum.add(num1+num2)


all_nums = list(range(28123))


print(sum(all_nums) - sum(abd_sum))