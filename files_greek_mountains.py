with open('files/mountains.txt','r',encoding='utf-8') as mountains:
  
    vouna=[]
    max_ypsos=0
    
    #to arxeio keimenou einai iterable antikeimeno ws pros tis grammes toy. Edw h for diaperna mia mia tis grammes toy.
    for vouno in mountains : 
        vouno = vouno.rstrip().split('\t') #dhmioyrgia listas vouna[] me diaxwristiko to tab gia ka8e stoixeio toy voynoy (onoma,ypsos,topo8esia)
        onoma=vouno[0].strip()
        ypsos=vouno[1].strip().replace(".","")
        topos=vouno[2].strip()
        vouna.append((onoma,ypsos,topos))
        
        #evresi megistoy ypsoys
        if max_ypsos<int(ypsos) :
            max_ypsos=int(ypsos)
        

#eksodos apo to arxeio (aytomath me to with - den xreiazetai kleisimo) efoson exoyme apo8hkeysei tis plhrofories se lista
keimeno=""

for i in vouna :
    ypsos=int(i[1])
    keimeno= keimeno+"Το όρος {} έχει ύψος {} μέτρα και βρισκεται στην τοποθεσία: {}.".format(i[0],i[1],i[2])
    if ypsos == max_ypsos :
        keimeno += "Είναι το ψηλότερο Ελληνικό Βουνό\n."
    else :
        keimeno += "Είναι χαμηλότερο κατά {} μέτρα από το ψηλότερο βουνό.\n".format(max_ypsos-ypsos)
print(keimeno)

with open("vouna2.txt","w",encoding="utf-8") as f:
    f.write(keimeno)
