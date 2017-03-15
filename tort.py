from math import ceil,floor

pikkus = input("Sisesta pikkus tükkides: ")
laius = input("Sisesta laius tükkides: ")
korgus = input("Sisesta kõrgus: ")
tk_pakk = input("Mitu tükki on ühes pakis: ")

def pakke():
    tk_arv = int(pikkus)*int(laius)*int(korgus)
    pakk_arv = tk_arv/int(tk_pakk)
    #print ("Sul on vaja "+str(round(pakk_arv+0.49))+" pakki:")
    print ("Sul on vaja "+str(floor(pakk_arv))+" pakki.")

pakke()