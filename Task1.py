"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    list_from =[]
    list_to =[]
    for to in texts:
      list_from.append(to[0])
      list_to.append(to[1])
    final_texts  = (set(list_from) | set(list_to))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    list_from_call =[]
    list_to_call =[]
    for to1 in calls:
      list_from_call.append(to1[0])
      list_to_call.append(to1[1])
    final_calls  = (set(list_from_call) | set(list_to_call))
    
count = len(set(final_texts)|set(final_calls))
print("There are "+str(count)+" different telephone numbers in the records.")



"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
