print("""
**********************************************************     
                Faktöriyel Bulma Programı
**********************************************************

|----------------------------------------------------------|
|          Çıkış Yapmak İçin c Tuşuna Basınız.             |
|----------------------------------------------------------|
""")
while True:
    sayı = input("Sayı Giriniz: ")
    if(sayı == "c"):
        print("işlem Sonlandırılıyor...")
        break
    else:
        sayı = int(sayı)
        faktoriyel = 1

        for i in range(2,sayı+1):
            faktoriyel *= i
        print("Faktöriyel: ",faktoriyel)