''' parse the titles.txt file into a json file'''

'''
escape all characters

preserve all inner parenthesis
preserve all - characters
store it as it is  , in raw format .


for each line , split the line into single characters and insert
 to dictionary if unique
export dictionary to json

clear characters at start and end of line

'''
# file1 = open("titles.txt","r")
# print(file1.readlines())
import io
with io.open("titles.txt", "r", encoding="utf-8") as my_file:
     my_unicode_string = my_file.read()
     print(my_unicode_string)
