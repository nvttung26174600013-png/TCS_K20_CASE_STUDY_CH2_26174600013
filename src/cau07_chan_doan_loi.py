ma_may = input("Nhập mã máy: ") 
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: ")) 
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000 
print(f"Máy: {ma_may}") 
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# Loi 1 (SyntaxError-dong 7): Thieu dau ngoac don dong ')' o cuoi lenh print().
# Loi 2 (TypeError-dong 4): Chua chuyen cong_suat_w sang float nen lay str chia cho int.
# Loi 3 (NameError-dong 7): Viet sai ten bien 'dien_nang' thay vi 'dien_nang_kwh'.