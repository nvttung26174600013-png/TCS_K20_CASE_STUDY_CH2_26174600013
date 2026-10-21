cong_suat_w =250
so_phut =90
don_gia_kwh =3000

dien_nang_kwh =cong_suat_w*so_phut/60/1000
chi_phi =dien_nang_kwh*don_gia_kwh

print("--- Khi so_phut = 90 ---")
print("Dien nang (kWh):",dien_nang_kwh,"| Kieu:",type(dien_nang_kwh))
print("Chi phi (VND):",chi_phi,"| Kieu:",type(chi_phi))

so_phut =60
dien_nang_kwh = cong_suat_w*so_phut/ 60/1000
chi_phi =dien_nang_kwh*don_gia_kwh

print("\n--- Khi so_phut = 60 ---")
print("Dien nang (kWh):",dien_nang_kwh, "| Kieu:",type(dien_nang_kwh))
print("Chi phi (VND):",chi_phi,"| Kieu:",type(chi_phi))