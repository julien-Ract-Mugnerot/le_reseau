with open(inventory.txt, r) as file:
    txt = file.read()


with open(current_inventory.txt, r) as file:
    current_txt = file.read()    
    
grp=[]
grp=[elem.split(',') for elem in txt.split('\n')]

grp_t_p = []
grp_t_p= [line[:-1] for line in grp[1:]][:-1]



current_grp = [elem.split(',') for elem in current_txt.split('')][:-2]
current_grp

current_txt_titles = [line[0] for line in current_grp[2:][:-1]]


txt_titles = [i[0] for i in grp_t_p]

titles_in_stock=[]
titles_not_in_stock=[]
for title in txt_titles :
    if title in current_txt_titles :
         titles_in_stock.append(title)
    else :
        titles_not_in_stock.append(title)

