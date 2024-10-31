import math
#Tìm số lớn nhất trong ba số a, b, c
a = float(input("Nhập số a :"))
b = float(input("Nhập số b :"))
c = float(input("Nhập số c :"))
if a > b and a > c:
    print("a là số lớn nhất")
elif b > a and b > c:
    print("b là số lớn nhất")
else:
    print("c là số lớn nhất")