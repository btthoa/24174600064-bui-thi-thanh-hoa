import math
#Kiểm tra kí tự trong bảng chữ cái tiếng anh là nguyên âm hay phụ âm
ki_tu =str(input("Nhập một kí tự bất kì trong bảng chữ cái tiếng anh :"))
nguyen_am = "ueoai"
if ki_tu == nguyen_am:
    print(f'Kí tự {ki_tu} là nguyên âm')
else:
    print(f'Kí tự {ki_tu} là phụ âm')