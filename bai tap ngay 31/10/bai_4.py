import math
a = float(input("Nhâp số a :"))
b = float(input("Nhập số b :"))
c = float(input("Nhập số c :"))
#Kiếm tra xem có phải là tam giác không
if a + b > c or a + c > b or b + c > a:
    print("Ba cạnh a, b, c tạo thành một tam giác")
#Phân loại tam giác    
if a == b == c:
    print("Tam giác là tam giác đều")
elif a == b or a == c or b == c:
    print("Tam giác là tam giác cân")
elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
    print("Tam giác là tam giác vuông")
else:
    print("Tam giác là tam giác thường")