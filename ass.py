'''a='mango'
print(a*2)
b='city'
print(b)'''

test_string=input("Enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))
