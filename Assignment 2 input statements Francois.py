print('This is a formula for when you get stuck in Canada\n and want to know what temperature it is outside')
print('What is the temperature in Celcius?')
C=int(input())#C is for Celcius, this is pointless comment one
F=((C*9/5)+32)#F is for Farenheit, this is pointless comment two
if F>70:
    print('This is Tshirt weather')
    print(F,'Degrees')
elif F>40:
    print('This is hoody(sweatshirt weather)')
    print(F,'Degrees')
elif F<40:
    print('This is put a coat on or catch hypothermia weather')
    print(F,'Degrees')
