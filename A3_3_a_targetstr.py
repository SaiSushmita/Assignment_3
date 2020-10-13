
S = input("Enter the string\n")

lst1 = S.split(' ')
tar = input("Enter the target word\n")
count=0
lst2=[]
for i in range(len(lst1)):
    if lst1[i]==tar:
        lst2.append(i)
        count+=1

if count==0:
    print(False)
else:
    print(*lst2)

