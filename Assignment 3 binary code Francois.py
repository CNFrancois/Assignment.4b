print('This is an equation to convert to or from binary and decimal')
print('Are you entering a binary or decimal number?')
a=input('')#allows for formula choice in line 5 if formula
print('What is your',a,'number?')
if a == 'binary':
      b=int(input(),2)
      print(b,' is your number in decimal')
else:
      c=bin(int(input()))[2:]#[_:]nifty little formula to remove begining characters
      print(c,' is your number in binary')
