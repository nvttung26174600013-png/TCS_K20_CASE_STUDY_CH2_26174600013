tong_phut =135 
cong_suat_w =250 
so_gio=tong_phut//60
so_phut_du=tong_phut%60
print("So gio:",so_gio)
print("So phut du:",so_phut_du)

su_dung_lau=tong_phut>60
print("Su dung lau (>60 Phut):",su_dung_lau)
du_lieu_hop_le=(cong_suat_w > 0) and (tong_phut > 0)
print("Du lieu hop le:", du_lieu_hop_le)

ket_qua_1 =100+20*3
ket_qua_2 =(100+20)*3
print("100+20*3 =", ket_qua_1)
print("(100+ 0)*3 =", ket_qua_2)