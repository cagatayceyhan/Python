print("""
********************************************************
Atm Makinesine Hoşgeldiniz.
İşlemler;
1 - Bakiye Sorgulama
2 - Para Yatırma
3 - Para Çekme
Programdan çıkmak için 'c' tuşuna basınız. 
********************************************************
""")

bakiye = 1000
while True:
    islem = input ("İşlemi Seçiniz: ")

    if(islem == "c"):
        print("İşlem İptal Ediliyor...")
        break

    elif (islem == "1"):
        print("Mevcut Bakiyeniz: {} TL .".format(bakiye))

    elif(islem == "2"):
        miktar = int(input("Yatırmak İstediğiniz Miktarı Giriniz: "))
        bakiye += miktar

    elif(islem=="3"):
        miktar = int(input("Çekmek İstediğiniz Miktarı Yazınız: "))
        if(bakiye - miktar <0):
            print("Yetersiz Bakiye")
            continue
        bakiye -= miktar

    else:
        print("Geçersiz İşlem Yaptınız!")