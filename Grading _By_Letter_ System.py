while True:
    user_input = input("Please Enter Your Exam Grade :  ")
    try:
        sinav_not = int(user_input)
        # do something
        break
    except ValueError:
        print("!!Please Enter Your Grade In Numbers!!")


if sinav_not>=90 and  sinav_not<=100:
    print("AA-" + "-Coefficient:4.0 ")

elif sinav_not>=85  and  sinav_not<=89:
    print("BA-" + "-Coefficient:3.5 ")


elif sinav_not>=80  and  sinav_not<=84:
    print("BB-" + "-Coefficient:3.0 " )

elif sinav_not>=75  and  sinav_not<=79:
    print("CB-" + "-Coefficient:2.5 " )

elif sinav_not>=65 and sinav_not<=74 :
    print("CC-" + "-Coefficient:2.0 ")

elif sinav_not>=60 and sinav_not<=64:
    print("DC-" + "-Coefficient:1.5 " )

elif sinav_not>=55 and sinav_not<=59:
    print("DD-" + "-Coefficient:1.0 ")

elif sinav_not>=50 and sinav_not<=54:
    print("FD-" + "-Coefficient:0.5 ")

elif sinav_not>=00 and sinav_not<=49:
    print("FF-" + "-Coefficient:0 ")

else :
    print("Invalid Note")






