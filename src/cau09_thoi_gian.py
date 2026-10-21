from datetime import datetime

thoi_diem =datetime.now()
thoi_diem_text =thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau =datetime(2026, 10, 14, 13, 15)
ket_thuc =datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))

# Giai thich su khac nhau:
# - datetime: Doi tuong luu moc thoi gian cu the (nam, thang, ngay, gio, phut, giay).
# - str: Chuoi ky tu van ban da dinh dang de hien thi, khong dung de tinh toan truc tiep.
# - timedelta: Doi tuong bieu dien khoang thoi gian chenh lech giua hai moc datetime.