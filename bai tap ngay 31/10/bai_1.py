import math
#Tính năm nhuận
n = int(input("Nhâp năm cần kiểm tra: "))
if n > 0:
    nam_nhuan = n % 4 == 0 and n % 400 == 0
    print(f"Năm {n} là năm nhuận")
else:
    print("Năm không phải là năm nhuận")