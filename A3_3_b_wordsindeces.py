
S = input("Enter the string\n")

lst = S.split(' ')
lst1 = set(lst)
print(lst1)
lst1 = list(lst1)
print(lst1)

     
for i in lst1:
    count=0
    for j in lst:
        if i == j:
            count+=1
    print(i,':',count)
    