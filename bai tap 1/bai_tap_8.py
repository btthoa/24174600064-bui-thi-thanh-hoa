import math

def tinh_gia_tri_f(x):
    if x <= 0:
        return "x phải lớn hơn 0."
    
    log4_x = math.log(x, 4)  # log_4(x)
    logx_2 = math.log(2, x)  # log_x(2)
    
    f_x = log4_x + logx_2
    return round(f_x, 1)

# Nhập giá trị x từ người dùng
x = float(input("Nhập vào giá trị x (x > 0): "))
result = tinh_gia_tri_f(x)

print(f"Giá trị của f(x) là: {result}")