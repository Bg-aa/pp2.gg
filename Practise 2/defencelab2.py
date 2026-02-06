mdict = {"Aidar":'m', "Arai":'f'}
male = []
female = []
for x in mdict:
    if mdict[x]=='m':
        male.append(x)
    else:
        female.append(x)
print(male)
print(female)