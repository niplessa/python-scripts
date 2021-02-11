import math as m

"""12.2 Να κατασκευάσετε πρόγραμμα που ζητάει διαδοχικά από
τον χρήστη την ακτίνα σφαίρας και υπολογίζει, καλώντας
σχετικές συναρτήσεις την επιφάνεια και τον όγκο της. Τερματίζει
με stop."""

#synarthseis:

def emv(r) : #emvadon
    emv = 4*m.pi*r**2
    return(emv)

def vol(r) : #ogkos
    vol =  4/3*m.pi*r**3
    return(vol)

#voh8htikh synarthsh isnum()

def isnum(n) :
    if not type(n) is str :
        return(False)
    n = n.strip() #ka8arisma kenwn
    if n.isdigit() : return(True) 
    elif (n[0] == "+" or n[0]== "-") and (n[1:].isdigit()) :
        return(True) 
    elif "." in n :
        if n.count(".")==1 and isnum(n.replace(".","")) : return(True)
        else : return(False)
    else : return(False)
                                   

while True :
    r = input("Dwse thn aktina ths sfairas - stop gia eksodo: ")
    if isnum(r) :
        r=float(r)
        print("To emvadon einai:\t{:1.4f} ".format(emv(r)))
        print("O ogkos einai:\t{:1.4f} " .format(vol(r)))
    else :        
        if r=="stop" :
            print("Eksodos")
            break
        print("Den edwses ari8mo!");
