print('This is to figure out your final grade')
print('Enter your grade 0-100')
x=int(input())
if x>100 or x<0:
    print('This does not fall within grading guidelines')
elif x>=90:
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print('C')
elif x>=60:
    print('D')
else:
    print('F')
