from random import *
x = randint(1, 10)    # Pick a random number between 1 and 10.
y = randint(1, 10)
z = x*y
print('You have two numbers')
print(z,' ',x)
print('What type of arthmatic would you like to practice?')
print('please type +,-,*,/ as the arthmatic you would like to practice')
operator=input()
while operator != '+' or '-' or '*' or '/':#forces user to put in an operator
        if operator == 'q':#loops so user does not have to keep rerunning program
                break
        elif operator == '+':
            ad=x+z
            print('Please answer the following scenario')
            print(z,'+',x,'= ?')
            print('Answer')
            ans=float(input())
            while ad != ans:
                print('try again for more practice')#user gets a second try
                ans=float(input())
                if ad != ans:
                    print('Would you like the answer?\n type (yes or no)')#allows user a way out of problem
                    giveup=input()
                    if giveup == 'yes':
                        print(z,'+',x,'=',ad)
            if ad == ans:
                print('your answer is correct!!!')
                print(z,'+',x,'=',ad)
        if operator == '-':
            su=z-x
            print('Please answer the following scenario')
            print(z,'-',x,'= ?')
            print('Answer')
            ans=float(input())
            while su != ans:
                print('try again for more practice')
                ans=float(input())
                if su != ans:
                    print('Would you like the answer?\n type (yes or no)')
                    giveup=input()
                    if giveup == 'yes':
                        print(z,'-',x,'=',su)
            if su == ans:
                print('your answer is correct!!!')
                print(z,'-',x,'=',su)
        if operator == '*':
            mu=x*z
            print('Please answer the following scenario')
            print(z,'*',x,'= ?')
            print('Answer')
            ans=float(input())
            while mu != ans:
                print('try again for more practice')
                ans=float(input())
                if mu != ans:
                    print('Would you like the answer?\n type (yes or no)')
                    giveup=input()
                    if giveup == 'yes':
                        print(z,'*',x,'=',mu)
            if mu == ans:
                print('your answer is correct!!!')
                print(z,'*',x,'=',mu)
        if operator == '/':
            di=z/x
            print('Please answer the following scenario')
            print(z,'/',x,'= ?')
            print('Answer')
            ans=float(input())
            while di != ans:
                print('try again for more practice')
                ans=float(input())
                if di != ans:
                    print('Would you like the answer?\n type (yes or no)')
                    giveup=input()
                    if giveup == 'yes':
                        print(z,'/',x,'=',di)
            if di == ans:
                print('your answer is correct!!!')
                print(z,'/',x,'=',di)
        print('please type +,-,*,/ as the arthmatic you would like to practice\nor q to quit studying')
        operator=input()#forces user to put in an operator
