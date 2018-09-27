from random import *
x = randint(1, 10)    # Pick a random number between 1 and 10.
y = randint(1, 10)
z = x*y
print('You have two numbers')
print(z,' ',x)
print('What type of arthmatic would you like to practice?')
operator=input()
if operator == '+' or operator == 'addition':
    ad=x+z
    print('Answer')
    ans=float(input())
    print(z,'+',x,'=',ad)
    if ad == ans:
        print('your answer is correct!!!')
    else:
        print('try again for more practice')
elif operator == '-' or operator == 'subtraction':
    su=z-x
    print('Answer')
    ans=float(input())
    print(z,'-',x,'=',su)
    if su == ans:
        print('your answer is correct!!!')
    else:
        print('try again for more practice')
elif operator == '*' or operator == 'multiplication':
    mu=x*y
    print('Answer')
    ans=float(input())
    print(z,'*',x,'=',mu)
    if mu == ans:
        print('your answer is correct!!!')
    else:
        print('try again for more practice')
elif operator == '/' or operator == 'division':
    di=z/x
    print('Answer')
    ans=float(input())
    print(z,'/',x,'=',di)
    if di == ans:
        print('your answer is correct!!!')
    else:
        print('try again for more practice')
elif operator != '+':
    print('please type +,-,*,/ as the arthmatic you would like to practice')
