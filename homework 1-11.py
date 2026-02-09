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
numbers =(10, 20, 30 ,40 10)

if numbers(0) == numbers[-1]:
    print('true')
else:
    print('false')