x=int(input('Enter a number in the range of 1-10: '))
'''
if(x==1):
    print('one')
elif(x==2):
    print('two')
elif(x==3):
    print('three')
elif(x==4):
    print('four')
elif(x==5):
    print('five')
elif(x==6):
    print('six')
elif(x==7):
    print('seven')
elif(x==8):
    print('eight')
elif(x==9):
    print('nine')
else:
    print('ten')
'''
num_word={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
if x in [1,2,3,4,5,6,7,8,9,10]:
    print(num_word.get(x))
else:
    print('Enter a number in valid range')

