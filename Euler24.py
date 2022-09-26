def get_list_without_num(num,lst):
    return [n for n in lst if n!=num]


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


perm_list = gen_perm([0,1,2,3,4,5,6,7,8,9])

lst2 = perm_list[999999]

print(''.join(map(str,lst2)))