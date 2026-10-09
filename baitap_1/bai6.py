def Doidonvi(t, p, l):
  gram = (t * 20 * 32 * 13.3) + (p * 32 * 13.3) + (l * 13.3)
  kg = int(gram // 1000)
  gram = gram % 1000
  print("dap an", kg, "kg", gram, "g")
t = int(input("talents: "))
p = int(input("pounds: "))
l = int(input("lots: "))
Doidonvi(t, p, l)
