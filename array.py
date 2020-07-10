my_list = []

for i in range(1, 9):
    my_list.append(i)

del my_list[-2]
my_list[0] = 0
print(my_list)
