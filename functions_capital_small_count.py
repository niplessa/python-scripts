'''12.3 Να κατασκευάσετε πρόγραμμα που καλεί συνάρτηση που
μετράει τα κεφαλαία και μικρά γράμματα σε μια φράση.'''

def letter_count(phrase) :
    #arxikopoihsh metrhtwn
    capital = 0;
    small = 0;
    
    for char in phrase : #gia ka8e xarakthra sto string
        if char.isalpha() :  #mono ta grammata
            if char.lower() == char : #h lower() mas epistrefei pisw ton xarakthra pezo, opote an taytizetai me ton xarakthra, aytos einai pezos!
                small += 1;
            elif char.upper() == char :#paromoia h upper()
                capital += 1
    return(capital,small)

frash = input("Dwse mia frash me peza & kefalaia grammata: ")
print("Ta peza grammata einai: {} enw ta kefalaia einai: {}".format(letter_count(frash)[1],letter_count(frash)[0]))

                