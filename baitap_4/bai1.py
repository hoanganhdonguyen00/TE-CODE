# import re

# a= input("type your course: ")
# if a=="[tTeEcC][0-9][0-9][0-9]":
#     return (s.match(a))  

import re
a = input("type code: ")
def s(code):
    if re.search(r"^[A-Z][A-z][A-Z][0-9][0-9][0-9]$", code):
        return True
    else:
        return False
print(s(a))    