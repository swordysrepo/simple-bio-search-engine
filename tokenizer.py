# Import necessary modules
import nltk
#nltk.download()

from nltk.tokenize import sent_tokenize, word_tokenize
my_list=[]
s=set()
f = open("titles.txt", "r")
for line in f:
   my_list = word_tokenize(line)
   for word in my_list:
       s.add(word)
print(s)
