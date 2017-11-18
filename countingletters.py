'''
Created on Nov 18, 2017

@author: ITAUser
'''
def characterappearances(filename, mychar):
    f = open(filename , 'r')
    count = 0;
    run = True
    while run:
        text = f.read(1)
        text = text.lower()
        if text == mychar:
            count = count +1; 
        if text == '': 
            break 
        print(count)
characterappearances('constituton.txt' , 'a')
#read the file
#split the file
#count the letters
#print result 