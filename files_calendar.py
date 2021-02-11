# i vivliothiki calendar mas dhmioyrgei ena hmerologio toy  etoys poy 8a zhth8ei
import calendar as cal

#δημιουργία λίστας απο το αρχειο months με ελληνικους & αγγλικους μηνες
with open("months.csv","r",encoding="utf-8") as f :
    months=[]
    for i in f :
        months.append(i.strip().split(","))
    #print(months)


#εισαγωγη ετους με try/except σε περιπτωση που δεν δωθει ακεραιος
year=input("Dwse to etos: ")
while type(year) is str :
    try :
        year=int(year)
        calendar_en=cal.calendar(year)
    except ValueError :
        print("Den edwses ari8mo")
        year=input("Dwse to etos: ")

calendar_gr=calendar_en
#αντικατασταση αγγλικων μηνων με ελληνικους
for m in months :
    calendar_gr=calendar_gr.replace(m[0],m[1])

#αντικατασταση αγγλικων ημερων με ελληνικες
calendar_gr= calendar_gr.replace("Mo Tu We Th Fr Sa Su","Δε Τρ Τε Πε Πα Σα Κυ")



#write calendar to file
with open("files\calendar_en.txt","w",encoding="utf-8") as f :
    f.write(calendar_en)
with open("files\calendar_gr.txt","w",encoding="utf-8") as f :
   f.write(calendar_gr)
