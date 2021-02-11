import random

months = '''    Ιανουάριος (31 ημέρες)
    Φεβρουάριος (28 ή 29 ημέρες)
    Μάρτιος (31 ημέρες)
    Απρίλιος (30 ημέρες)
    Μάιος (31 ημέρες)
    Ιούνιος (30 ημέρες)
    Ιούλιος (31 ημέρες)
    Αύγουστος (31 ημέρες)
    Σεπτέμβριος (30 ημέρες)
    Οκτώβριος (31 ημέρες)
    Νοέμβριος (30 ημέρες)
    Δεκέμβριος (31 ημέρες)'''

#xwrise ton string me vash ta newlines prwta kai meta me vash ta kena kai pare to 1o stoixeio gia ta onomata twn mhnwn
months_names = [x.split()[0] for x in months.split("\n")] 
print(months_names)

#xwrise to string me vash ta newlines prwta kai meta me vash to "(" kai pare ta 2 prwta stoixeia gia ton
#ari8mo hmerwn
month_days = [int((x.split("(")[1][0:2])) for x in months.split("\n")]
print(month_days)

while True :
    year = input("Etos: ").strip() #.strip()->ka8arizei apo kena ktl
    if  not year.isdigit() :
        print("Den edwses xronologia!")
        break
    else :
        year = int(year) #entopismos disektoy etoys
    if year % 4 != 0 :
        disekto = False
        print("To etos {} DEN einai disekto" .format(year))
    elif year % 100 != 0 :
        disekto  = True
        print("To etos {} EINAI disekto" .format(year))
    elif year % 400 != 0 :
        disekto = False
        print("To etos {} DEN einai disekto".format(year))
    else :
        disekto = True
        print("To etos {} EINAI disekto".format(year))
        
    if disekto == True :
        month_days[1]=29
        
    random_days=input("Poses tyxaies meres 8eleis? ")
    if not random_days.isdigit() :
        break
    else :
        random_days=int(random_days)
        for i in range(random_days) :
            m = random.randint(0,11)
            d = random.randint(1,month_days[m])
            print("{:02d}-{:02d}-{}".format(d,m,year))
            print("{:02d}-{}-{}".format(d,months_names[m],year))
                              
    
