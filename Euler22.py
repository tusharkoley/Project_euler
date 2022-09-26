


def get_score_by_name(name):
	sm = 0    
	for l in name:
	    sm+=alpha_dict[l]
	return sm




with open('p022_names.txt') as f:
    data = f.read()

data = data.replace('"','')
names = data.split(',')
sorted_names = sorted(names)

alpha_dict = {}

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
for idx, alpha in enumerate(alphabets):
    alpha_dict[alpha]=idx+1


tot_sum = 0
for idx, name in enumerate(sorted_names):
    tot_sum = tot_sum + (idx+1)*get_score_by_name(name)

print(tot_sum)