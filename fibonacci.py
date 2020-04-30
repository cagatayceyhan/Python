a = 1
b = 1
fibonacci = [a,b]

for i in range(20): #İlk 20 İşlemi Ele Alıyoruz.
    a,b = b,a+b
    print("a:",a,"b:",b) #Adımları Yazdırıyoruz
    fibonacci.append(b)
print(fibonacci)