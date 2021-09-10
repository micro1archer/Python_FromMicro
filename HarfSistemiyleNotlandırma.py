sinav_not = int(input("Bir not giriniz: "))

if sinav_not>=90 and  sinav_not<=100:
    print("AA-" + "-Katsayınız:4.0 ")

elif sinav_not>=85  and  sinav_not<=89:
    print("BA-" + "-Katsayınız:3.5 ")


elif sinav_not>=80  and  sinav_not<=84:
    print("BB-" + "-Katsayınız:3.0 " )

elif sinav_not>=75  and  sinav_not<=79:
    print("CB-" + "-Katsayınız:2.5 " )

elif sinav_not>=65 and sinav_not<=74 :
    print("CC-" + "-Katsayınız:2.0 ")

elif sinav_not>=60 and sinav_not<=64:
    print("DC-" + "-Katsayınız:1.5 " )

elif sinav_not>=55 and sinav_not<=59:
    print("DD-" + "-Katsayınız:1.0 ")

elif sinav_not>=50 and sinav_not<=54:
    print("FD-" + "-Katsayınız:0.5 ")

elif sinav_not>=00 and sinav_not<=49:
    print("FF-" + "-Katsayınız:0 ")

else :
    print("Geçersiz Not")
