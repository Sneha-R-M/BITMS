# Reads two numbers from input and typecasts them to int using 
# list comprehension
'''x, y = [int(x) for x in input().split()]
print(x)
print(y)

# Reads two numbers from input and typecasts them to int using 
# map function
x, y = map(int, input().split())
print(x)
print(y)'''
#slicing mtd
'''names="Sneha"
print(names)
print(names[:])
print(names[2:])
print(names[-1:])
print(names[-5:1])
print(names[::-1])'''
#finding vowels in word using list comprehension
'''word='sneha'
vowels='aeiou'
result=[char for char in word if char in vowels]

print(result)'''
#to print
'''x='sneha'
print(a[::-3])'''

'''name="sneha"
print(name)
print(name[:])
print(name[2:])
print(name[-1:])
print(name[-5:-1])
print(name[::-1])
print(name[::-3])
sep='-'.join(name[::2])
print(sep)
for i in range(0,len(name)):
    if(i%3==0 and i!=0):
        print('-',end='')
    else:
         print(names[i],end='')'''

'''name="sneha"
print(name)
a=name[0:8:2]
print(a,end='-')'''

#opening file
'''fileptr=open("second.txt","r")
if fileptr:
    print("file is opened successfully")'''
#Inbuilt methods in list
'''list=['a','b',23,45]
list.append(c)
print(list)'''
'''list1=[1,2,3]
list2=[2,3,4,5]
List1.extend(List2)
List2.extend(List1)
print(List2)'''
'''list=[1,2,3,4,5]
print(sum[list])'''

'''print(dir(locals()['_builtins_']))'''

'''try:
    num=10
    deno=0
    
    result=num/deno
    
    print(result)
except:
    print("Error: Denominator cannot be 0.")'''
try:
    num=10
    deno=0
    result=num/deno
    print(result)
except:
    print('error:denominator cannot be 0')'''

'''try:
    even_numbers=[2,4,6,8]
    print(even_numbers[5])
except ZeroDivisionError:
    print('denominaator cannot be 0')
except IndexError:
    print('indext out of bound')'''

'''try:
    num=int(input('enter a number:'))
    assert num%2==0
except:
    print('not an even number!')
else:
    reciprocal=1/num
    print(reciprocal)'''
    
file_path="second.txt"
try:
    with open(file_path, "r")as file:
        content = file.read()
        print(content)
    except Exception as e:
        print(f"An error occured: {e}")
        finally:
            print("Closing the file.")
        


