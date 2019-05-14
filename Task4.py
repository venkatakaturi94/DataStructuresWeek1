"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

list_tele_marketers=[]
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    list_from =[]
    list_to =[]
    for to in texts:
      list_from.append(to[0])
      list_to.append(to[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    list_from_call =[]
    list_to_call =[]
    for to1 in calls:
      list_from_call.append(to1[0])
      list_to_call.append(to1[1])

for x in list_from_call:
    if ((x not in list_to_call) and (x not in list_from) and (x not in list_to)):
        list_tele_marketers.append(x)

print("These numbers could be telemarketers:")
no_duplicates = sorted(set(list_tele_marketers))
for j in no_duplicates:
    print(j)
        
        

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

