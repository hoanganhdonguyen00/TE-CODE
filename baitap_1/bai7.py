import random
def tao_ma_khoa():
  c3so = ""
  for i in range(3):
    so = random.randint(0, 9)
    c3so = c3so + str(so)
    c4so = ""
  for i in range(4):
    so = random.randint(1, 6)
    c4so = c4so + str(so)
  print("3 chữ số :", c3so)
  print("4 chữ số :", c4so)
tao_ma_khoa()