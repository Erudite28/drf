num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))
op=input('Enter an operator(+,-,*,/); ')

if op=="+":
    print('The addition of', num1, 'and', num2, 'is:', num1+num2)

elif op=='-':
    print('The subtraction of', num1, 'and', num2, 'is:', num1-num2)

elif op=='*':
    print('The multiplication of', num1, 'and', num2, 'is:', num1*num2) 

elif op=='/':
    print('The division of', num1, 'and', num2, 'is:', num1/num2)

else:
    print('Please choose a valid operator')