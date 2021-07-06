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
# declare dict
# hashmap = {"words":[]}
hashmap = {}


with io.open("titles.txt", "r", encoding="utf-8") as my_file:
     lines = my_file.readlines()
     # print(my_unicode_string)
     for line in lines:
          if x > 10:
               break
          print(line)     
          x+=1
          parse_list = line.split()
          for word in parse_list:
               # print(word)
               # add word to hashmap
               # hashmap["words"].append({"word":word})
               hashmap.update({word:[]})

     pprint.pprint(hashmap)
     with open("output.json", "a") as outfile:
         json.dump(hashmap, outfile)
