import re
def sdt(document):
  pattern = r"\+84\d+|\b\d{10}\b"
  phone = re.findall(pattern, document)
  for phone in phone:
    document = document.replace(phone, "[REDACTED]")
  return document
check = "số dth 1233445566."
print(sdt(check))
