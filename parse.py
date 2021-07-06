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

import io
import pprint
import json
x = 0
hashmap = {}


with io.open("titles.txt", "r", encoding="utf-8") as my_file:
     #load file in obj
     lines = my_file.readlines()
     #read file line by line
     for line in lines:
          if x > 10:
               break
          # show line parsing
          print(line)     
          x+=1
          # split line to a list
          parse_list = line.split()
          for word in parse_list:
               # add word to dictionary
               hashmap.update({word:[]})
     # show our hashmap
     pprint.pprint(hashmap)
     with open("output.json", "a") as outfile:
          #dump dict to output file
         json.dump(hashmap, outfile)
