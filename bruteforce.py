dogru_sifre = "admin"
users_txt = ["admin123", "1234","1234567890","admin"]

for tahmin in users_txt:
    if tahmin == dogru_sifre:
        print("şifre bulundu" , tahmin)
        break
    else:
        print("Şifre bulunamadı!")




