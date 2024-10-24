def tinh_tien_dien(dien_ap, dong_dien, thoi_gian, gia_tien_kwh):
    cong_suat = dien_ap * dong_dien  # Công suất (W)
    tieu_thu_nang_luong_kwh = ( cong_suat* thoi_gian) / 3600000  # Chuyển đổi sang kWh
    chi_phi = tieu_thu_nang_luong_kwh * gia_tien_kwh # Tính tiền điện
    return round(chi_phi, 2)

# Thông tin đã cho
dien_ap = 220  # V
dong_dien = 2.7  # A
gia_tien_kwh = 7000  # đ/kWh

# Nhập thời gian sử dụng bóng đèn từ người dùng
thoi_gian = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))

# Tính toán tiền điện
result = tinh_tien_dien(dien_ap, dong_dien, thoi_gian, gia_tien_kwh)
print(f"Tiền điện phải trả là: {result} đ")
