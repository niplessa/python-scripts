'''18. Άσκηση 1
Να παρουσιάστε με κατάλληλη στοίχιση την
ιεραρχία του συστήματος αρχείων του
υπολογιστή σας.'''

import os
import os.path

#ζητάμε απο τον χρήστη το όνομα του φακέλου
while True :
    folder = input("Dwse to onoma toy fakeloy(Enter gia eksodo): ")
    if folder =="" : break
    #os.chdir(folder)
    if os.path.isdir(folder) :
        for r,d,f in os.walk(folder) :
            print(r)
            #level 
            for fi in f :
                print("Files:")
                print("\t\t",fi)
    