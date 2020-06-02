num_list = list()
i=2000
while i in range(2000, 3200):
    print(i)
    if i % 7 == 0:
        if i% 5 != 0:
            num_list.append(i)
    i=i+1
    
print(num_list)