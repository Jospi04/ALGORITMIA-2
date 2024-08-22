#break 
for i in range(1,11):
    print(i)
    if i ==5:
        break #Solo imprime hasta el 5 

#continue
for i in range(1,11):
    if i % 2==0:
        continue #Saltar números pares
    print(i)