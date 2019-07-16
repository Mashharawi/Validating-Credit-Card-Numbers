""" hackerrank.com
 valid credit card from ABCD Bank has the following characteristics: 

► It must start with a ,  or . 
► It must contain exactly  digits. 
► It must only consist of digits (-). 
► It may have digits in groups of , separated by one hyphen "-". 
► It must NOT use any other separator like ' ' , '_', etc. 
► It must NOT have  or more consecutive repeated digits.

Examples:

Valid Credit Card Numbers

4253625879615786
4424424424442444
5122-2368-7954-3214
Invalid Credit Card Numbers

42536258796157867       #17 digits in card number → Invalid 
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid


Sample Input

6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
Sample Output

Valid
Valid
Invalid
Valid
Invalid
Invalid

"""

#contineu enter no.s tell you enter # to stop

import re

PATTERN=r"^(?!.*([0-9])(?:-?\1){3})[456][0-9]{3}(-?)[0-9]{4}\2[0-9]{4}\2[0-9]{4}$"

def is_valid_card(sequence):
    x=re.search(PATTERN, sequence)
    #print(x)
    if x != None:
        return True
    return False
#result = is_valid_card('5122-2368-7954-3214')
#print(result)


while True:
    n = input("Enter number or enter # to END!     :")
    if n != '#':
        result = is_valid_card(n)
        print(result)
    else:
        print("Bye")
        break