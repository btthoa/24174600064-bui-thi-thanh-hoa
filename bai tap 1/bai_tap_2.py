import math

def tinh_gia_tri_f(x):
    tu_so = -x + math.sqrt(x**2 + 4)
    mau_so = (x**4 + 1)**(1/7)
    f_x = tu_so / mau_so
    return round(f_x, 2)

# Nhập giá trị x từ người dùng
x = float(input("Nhập vào giá trị x: "))
result = tinh_gia_tri_f(x)
print(f"Giá trị của f(x) là: {result}")
