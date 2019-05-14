"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    list_from_call =[]
    list_blr_out =[]
    list_area_codes=[]
    blr_to_blr=[]

    """ Placing values into lists"""

    for to1 in calls:
      list_from_call.append((to1[0],to1[1]))
    list_blr_out = [i for i in list_from_call if "(080)" in i[0]]
    blr_to_blr = [i for i in list_from_call if "(080)" in i[0] and "(080)" in i[1]]

    for x in list_blr_out:
        s = x[1]
        if x[1][0] == '(' :
            start = '(;'
            end = ')'
            list_area_codes.append(s[s.find(start)+len(start):s.rfind(end)])
        elif x[1][0] == '7' or x[1][0] == '8' or x[1][0] == '9' or (' ' in x[1]):
            list_area_codes.append(x[1][:4])
    
        list_area_codes.append('140')
    final_list = sorted(set(list_area_codes))
    print("The numbers called by people in Bangalore have codes:")
    for j in final_list:
        print(j)

    """ PART B SOLUTION """
    percent = (len(blr_to_blr)*100)/(len(list_from_call))
    print(str(round(percent,2))+" percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

    
    
    

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
