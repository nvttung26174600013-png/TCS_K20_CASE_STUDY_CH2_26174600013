ma_phien=input("Nhap ma phien: ")
ma_may=input("Nhap ma may: ")
cong_suat_w=float(input("Nhap cong suat (W): "))
so_phut=int(input("Nhap so phut su dung: "))
don_gia_kwh=float(input("Nhap don gia (VND/kWh): "))

dien_nang_kwh=cong_suat_w*so_phut/60/1000
chi_phi =dien_nang_kwh*don_gia_kwh

print("Ma phien:",ma_phien)
print("May:",ma_may)
print("Dien nang:",dien_nang_kwh)
print("Chi phi:",chi_phi)