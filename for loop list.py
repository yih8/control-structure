my_list=[1,2,"ele","umlaut",[1,2]]

for i in range (1,5):
    print(my_list[i])
    if my_list[i]==1:
        break
    else:
        i+=1
