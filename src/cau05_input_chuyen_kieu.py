ma_may =input("Nhap ma may: ")
cong_suat_raw =input("Nhap cong suat (W): ")
so_phut_raw =input("Nhap so phut su dung: ")
don_gia_raw =input("Nhap don gia dien/kWh: ")

print("--- Kieu du lieu ngay sau khi nhap ---")
print("ma_may:",type(ma_may))
print("cong_suat_raw:",type(cong_suat_raw))
print("so_phut_raw:",type(so_phut_raw))
print("don_gia_raw:",type(don_gia_raw))

cong_suat_w =float(cong_suat_raw)
so_phut =int(so_phut_raw)
don_gia_kwh =float(don_gia_raw)

print("--- Kieu du lieu sau khi chuyen kieu ---")
print("cong_suat_w:",cong_suat_w,"| Kieu:",type(cong_suat_w))
print("so_phut:",so_phut,"| Kieu:",type(so_phut))
print("don_gia_kwh:",don_gia_kwh,"| Kieu:",type(don_gia_kwh))

dien_nang_kwh =cong_suat_w*so_phut/60/1000
chi_phi =dien_nang_kwh*don_gia_kwh

print("--- Ket qua tinh toan ---")
print("Ma may:",ma_may)
print("Dien nang tieu thu (kWh):",dien_nang_kwh)
print("Chi phi dien (VND):",chi_phi)