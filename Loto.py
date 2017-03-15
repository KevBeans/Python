from random import randint
check = randint(0,9)
 
def loto():
    number = input("Sisesta üks täisarv 0-9: ")
    if number.isdigit():
        print (check)
        number = int(number)
        if int(number) < check:
            print("Sisestatud number on kontrollarvust väiksem.")
            loto()
        elif int(number) > check:
            print("Sisestatud number on kontrollarvust suurem.")
            loto()
        else:
            print ("We wuz kangs n shit")
    else:
        print("Gibsmedat juissi number b0ss")
        loto()
loto()