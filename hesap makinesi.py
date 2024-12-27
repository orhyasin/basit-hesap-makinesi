def toplama(sayi1, sayi2):
    return sayi1 + sayi2

def cikarma(sayi1, sayi2):
    return sayi1 - sayi2

def carpma(sayi1, sayi2):
    return sayi1 * sayi2

def bolme(sayi1, sayi2):
    if sayi2 == 0:
        return "Hata: Sıfıra bölme yapılamaz!"
    return sayi1 / sayi2

def hesap_makinesi():
    print("HESAP MAKİNESİ!")
    print("İşlemler:")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")

    secim = input("Yapmak istediğiniz işlem ? (1/2/3/4): ")

    if secim not in ["1", "2", "3", "4"]:
        print("Geçersiz seçim yaptınız.")
        return

    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    if secim == "1":
        sonuc = toplama(sayi1, sayi2)
        print(f"Sonuç: {sonuc}")
    elif secim == "2":
        sonuc = cikarma(sayi1, sayi2)
        print(f"Sonuç: {sonuc}")
    elif secim == "3":
        sonuc = carpma(sayi1, sayi2)
        print(f"Sonuç: {sonuc}")
    elif secim == "4":
        sonuc = bolme(sayi1, sayi2)
        print(f"Sonuç: {sonuc}")

# Program başlatılıyor
hesap_makinesi()
