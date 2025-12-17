def brute_force_kontrol(hedef_sifre, deneme_listesi):
    print("--- İşlem Başlatıldı ---")
    
    for sira, tahmin in enumerate(deneme_listesi, 1):
        if tahmin == hedef_sifre:
            print(f"✅ Başarılı! {sira}. denemede şifre bulundu: {tahmin}")
            return True # Fonksiyondan çıkış yapar
        else:
            print(f"❌ Deneme {sira}: '{tahmin}' yanlış.")
            
    print("⚠️ Liste bitti, şifre bulunamadı.")
    return False

# Ayarlar
DOGRU_SIFRE = "admin"
USERS_TXT = ["admin123", "1234", "1234567890", "admin"]

# Çalıştır
brute_force_kontrol(DOGRU_SIFRE, USERS_TXT)

# bu kod parçası genel olarak bruteforce mantık yapısını anlamaktan geçer. belirli bir atak vektörü , hedef {target} içermez. 
# bruteforce (eğitim amaçlı ) yapmak için linux sistemlerine default olarak gelen passwords.txt dosyasını kullanabilirsiniz.
