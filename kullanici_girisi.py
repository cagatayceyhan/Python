print (""" 
************************************
Kullanıcı Girişi Programı
************************************
""")
sys_kullanici_adi = "Cagatay"
sys_parola = "123456789"

giris_hakki = 3

while True:
    kullanici_adi = input("Kullanıcı Adını Giriniz: ")
    parola = input("Parolanızı Giriniz: ")

    if ( kullanici_adi != sys_kullanici_adi and parola == sys_parola ):
        print("Kullanici Adı Hatalı...")
        giris_hakki -= 1
        print("Kalan Giriş Hakkınız : {}".format(giris_hakki))
    elif(kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Parola Hatalı....")
        giris_hakki -= 1
        print("Kalan Giriş Hakkınız: {} ".format(giris_hakki))
    elif(kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanıcı adı ve Parola yanlış....")
        giris_hakki -= 1
        print("Kalan Giriş Hakkınız: {} ".format(giris_hakki))
    else:
       print ("Giriş Başarılı")
       break
    if (giris_hakki == 0):
        print("Giriş Hakkınız Bitmiştir.")
        break


