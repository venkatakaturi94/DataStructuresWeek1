"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import Counter

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    list_from_call =[]
    list_to_call =[]
    from_dict = {}
    to_dict = {}
    final_list = []

    """ Placing values into lists"""

    for to1 in calls:
      list_from_call.append((to1[0],int(to1[3])))
      list_to_call.append((to1[1],int(to1[3])))

    """ getting sum of durations of each phone number called to other number """

    for t in list_from_call:
        if t[0] in from_dict:
            from_dict[t[0]] = from_dict[t[0]]+t[1]
        else:
            from_dict[t[0]] = t[1]

    """ getting sum of durations of each of receiving phone numbers """

    for u in list_to_call:
        if u[0] in to_dict:
            to_dict[u[0]] = to_dict[u[0]]+u[1]
        else:
            to_dict[u[0]] = u[1]

    """ Appending from list and to list """

    final_list.append(from_dict)
    final_list.append(to_dict)
    c = Counter()

    """ using counter for increased performance, below code adds the durations """

    for d in final_list:
        c.update(d)
    """ converting counter to dictionary """
    
    final_dict = dict(c)

    """ converting key and value to list as indexing is not supported by Python 3 """

    phone_num = list(final_dict.keys())[0]
    duration_time = list(final_dict.values())[0]

    """ Printing the Result """
    
    print(phone_num + " spent the longest time, " + str(duration_time) + " seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

