import re

with open('greece.txt','r',encoding='utf-8') as f :
    greece = f.read()
    #print(greece)
    #αντικατασταση του "Ελλάδα" με "ΕΛΛΑΔΑ"
    print(re.sub(r'\bΕλλάδα\b','ΕΛΛΑΔΑ',greece)) #r prin to string ypodhlwnei reg-ex
    
    #ευρεση ολων των λεξεων που αρχιζουν με κεφαλαιο γραμμα
    print("\nΛέξεις που αρχίζουν με κεφαλαίο γράμμα: ")
    pattern =r'\b[Α-Ω]+[\w]*'
    print(re.findall(pattern,greece))
    print("\nΛέξεις που αρχίζουν με φωνήεν: ")
    pattern =r'\b[αάΑεέΕηήΗιίΙοόΟωώΩ]+[\w]*' 
    print(re.findall(pattern,greece)) #αν δεν θελω διαχωρισμο πεζων-κεφαλαιων βαζω 3ο παραμετρο στην findall re.I (ι κεφαλαιο) που αγνοει κεφαλαια-πεζα
    print("\nΛέξεις που αρχίζουν με σύμφωνο: ")
    pattern =r'\b[^αάΑεέΕηήΗιίΙοόΟωώΩ][\w]*' 
    print(re.findall(pattern,greece)) #αν δεν θελω διαχωρισμο πεζων-κεφαλαιων βαζω 3ο παραμετρο στην findall re.I (ι κεφαλαιο) που αγνοει κεφαλαια-πεζα




    