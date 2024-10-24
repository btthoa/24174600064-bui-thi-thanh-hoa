import math

def thoi_gian_xe_dung_theo_van_toc(a):
    log4_5 = math.log(5, 4)  # Tính log4(5)
    thoi_gian_dung = a**4 / log4_5  # Tính thời gian dừng
    return round(thoi_gian_dung, 2)

# Nhập vận tốc a từ người dùng
a = float(input("Nhập vào vận tốc a của xe ô tô: "))
result = thoi_gian_xe_dung_theo_van_toc(a)

print(f"Thời gian ô tô đi được cho đến lúc dừng là: {result} giây")
