#queston 1
def product_or_sum(a, b):
    product = a * b
    if product > 1000:
        return a + b
    else:
        return product
    
product_or_sum(20, 30)
product_or_sum(50, 30)


#Question 2
previous = 0

for current in range(10):
    total = current + previous
    print('Current:', current, 'Previous')
    previous = current
    
#question 3
text = input('enter a string')

for i in range(len(text)):
    if i % 2 ==0:
        print(text[i])


#question 4
text = input('enter a string')
n = int(input('enter a number'))

new_string = text[n==1:]
print('New String:', new_string)

#question 5
numbers =[10, 20, 30 ,40, 10]

if numbers[0] == numbers[-1]:
    print('true')
else:
    print('false')
    
#question 6
numbers =[10, 20, 33, 46, 55]

for num in numbers:
    if num % 5 == 0:
        print(num)

#question 6
text = 'emma is a good developer. emma is a good writer'

count = text.count('emma')
print("total count of 'emma':", count)

#question 7
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
        print()

#question 8
num = int(input('enter a number: '))
original_num = num

reversed_num= 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
    
if original_num ++ reversed_num:
    print('true')
else:
    print('false')
    

#question 9

list1 =[1, 2, 3, 4,5 ,6]
list2 =[10, 15, 20, 25, 30]

new_list =[]

for num in list1:
    if num % 2 !=0:
        new_list.append(num)
        

for num in list2:
    if num % 2 == 0:
        new_list.append(num)
        
print('new list:', new_list)
