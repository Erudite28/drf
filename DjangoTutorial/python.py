def my_function(name, age):
    print('Hi ' + name + ', you are ', age, 'years old')

name=input('Enter your name: ')
age=input('Enter your age: ')
my_function(name, age) 


def my_function(num1, num2):
    return num1 + num2

num1=int(input('Enter a number: '))
num2=int(input('Enter another number: '))
print(my_function(num1, num2))

#IF Statements
value=input('Enter a sentence: ')
if len(value)>10:
    print('The length of (' + value + ') is greater than 10')
elif len(value)<10:
    print('The length of (' + value + ') is lesser than 10')
else:
    print('None of them are true')

a=2
b=5

if a==2 or a==5:
    print('The statements are true')

elif a==b and b==5:
    print('The statements are false')

else:
    print('none of the two')

x=int(input('Enter a number: '))

if x%5==0:
    print('The number is divisible by 5')
else:
    print('The number is not divisible by 5')

for x in 'mangoes':
    print(x)

my_list=[
    ['apple', 'banana', 'cherry'],
    ['grapes', 'kiwi', 'mangoes'],
    ['orange', 'pear', 'watermelon']
]

for lists in my_list:
    for items in lists:
        for letters in items:
            print(letters)