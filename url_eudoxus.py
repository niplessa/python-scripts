'''
20.1 Ξεκινώντας από τη σελίδα
https://service.eudoxus.gr/public/departments διαλέξτε ένα
Πανεπιστημιακό Τμήμα και να αναζητήσετε τα μαθήματα του και
τους κωδικούς τους
'''

import urllib.request , urllib.error
import re

#katevasma istoselidas se arxeio .txt
url = urllib.request.Request("https://service.eudoxus.gr/public/departments/courses/1303/2019")

try:
    with urllib.request.urlopen(url) as my_page :
    #evresi kwdikopoihshs:
        encoding = my_page.headers.get_content_charset()
        eudoxus = my_page.read().decode(encoding) #an afhsw to decode() keno -> utf-8
        with open("eudoxus\eudoxus.txt","w",encoding=encoding) as f :
            f.write(eudoxus)
        
except urllib.error.HTTPError as e:
    print("HTTP error")
    print(e)
    
except urllib.error.URLError as e:
    print("Url error")
    print(e)

else :
    #evresi olwn twn <h2> tags (me gnwsto pattern)
    h2_tags = re.findall(r'<h2\b[^>]*>(.*?)</h2>',eudoxus,re.I)

    h1_tags = re.findall(r'<h1\b[^>]*>(.*?)</h1>',eudoxus,re.I)


    count = 0

    print("{}\n{}\n{}\n".format(h2_tags[0],h2_tags[1],h1_tags[0]))

    for t in h2_tags :
        #anaktisi kwdikoy ma8hmatos
        code = re.findall(r"\[(.*)\]",t,re.I) # r"\[.*\]" -> otidhpote periexetai mesa se []
        if len(code)>0 : code=code[0].strip()
        #anaktisi onomatos ma8hmatos
        name=re.findall(r'\:(.*)',t,re.I)
        if len(name)>0 : name = name[0].strip()
        count += 1    
        print("{} Κωδικός μαθήματος: {} Όνομα μαθήματος: {}".format(count,code,name))

