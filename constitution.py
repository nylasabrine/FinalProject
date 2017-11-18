'''
Created on Nov 4, 2017

@author: ITAUser
'''

f = open('constituton.txt' , 'r')
text = f.read()
words = text.split()
print (len (words))
 
#read the file
#split the file
#print the number of words in the list