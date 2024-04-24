'''o='mangoes
city-use
single qts
inside double qts'
print(o)'''



'''list=[str(x) for x in input().split()]
list1=[]
for i in list:
    for j in range(len(i)):
        if(i[j]=='s'):
            list1.append(i)
print(list1)'''

userinput = input("Enter a string: ")
print([word for word in userinput.split() if 's' in word])
