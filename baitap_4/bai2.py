import re
def s(color):
  pattern = r"^#[0-9a-fA-F]{6}$"
  if re.fullmatch(pattern, color):
    return True  
  else:
    return False  
print(s("#FF5734"))
print(s("123456")) 