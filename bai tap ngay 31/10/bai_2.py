import math
#Kiểm tra điểm M(x,y) đối với hình tròn tâm I(a,b) bán kính R
x = float(input("Nhập tọa độ điểm x :"))
y = float(input("Nhập tọa độ điểm y :"))
a = float(input("Nhập tọa độ điểm a :"))
b = float(input("Nhập tọa độ điểm b :"))
ban_kinh = float(input("Nhập bán kính R :"))
d = ((x - a)**2 + (y - b)**2)**1/2
if  d <= ban_kinh and ban_kinh > 0:
    print(True)
    print("Điểm M thuộc đường tròn tâm I")
else: 
    print(False)