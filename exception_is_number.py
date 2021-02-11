num = ''

while type(num) is str:
    num = input("Dwse arithmo: ")
    
    try :
        num = float(num) #an einai ari8mos ola kala
    except ValueError : #ValuError einai to sfalma poy 8a dwsei an pame na kanoyme metatroph px string se dekadiko
        print("Den edwses ari8mo! - Ksanaprospa8hse!") #typwnei sfalma kai efoson to num einai akoma string mas ksanazhtaei 
        
        
print("O ari8mos einai:{:1.2f}".format(num))