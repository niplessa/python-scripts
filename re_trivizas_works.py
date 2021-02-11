import re

tw='trivizas_works.txt'
tonoi = ["αά","εέ","ηή","ιί","οό","υύ","ωώ"] #λίστα που κρατάει κάθε γράμμα τονούμενο/άτονο

#anoigma arxeioy me try
try :
    with open (tw,'r',encoding='utf-8') as f :
        triv = f.read()
        print(triv)
        #for line in triv.strip().split('\n') :
            #print(line)
except IOError as e :
    print(e)
    
#to arxeio exei perastei sto triv, vgainoyme apo to perivallon arxeioy
while True :
    phrase = input("\nΔώσε λέξη-κλειδί -κενό για έξοδο-: ")
    if phrase == "" : break
    
    #παράλειψη τονων α->α/ά
    n_phrase = ""
    for c in phrase : #διαπεραση καθε χαρακτήρα της φράσης
        char = c
        for i in tonoi :
            if c in i : char ='['+i+']' #αν ο χαρακτήρας ειναι ενας απο τα φωνήεντα πχ α αντικατέστησε τον με [αά]
        n_phrase+=char
    print("Regular Expression:",n_phrase)
    
    
    pattern = r'.*'+n_phrase+'.*' #_οποιοσδηποτε χαρακτηρας _ + φράση + _οποισδήποτε χαρακτήρας_
    print("\nΠαραμύθια που περιέχουν την λέξη {} :\n".format(phrase))
    w= re.findall(pattern,triv,re.I)
    for work in w :
        print(work)