'''
Ξεκινώντας από τη σελίδα καθηγητών του πανεπιστημιακού
τμήματος : http://www.ece.upatras.gr/index.php/el/faculty.html
να αναζητήσετε τα τηλέφωνα των μελών του Τμήματος
'''

import urllib.request,urllib.error
import re

#synarthsh poy epistrefei to onoma kai to thlefwno ka8e ka8hghth
def find_phone(adr) :
    url = urllib.request.Request(adr)

    try:
        with urllib.request.urlopen(url) as my_page :
            encoding = my_page.headers.get_content_charset()
            html = my_page.read().decode(encoding) 
                    
    except urllib.error.HTTPError as e:
        print("HTTP error")
        print(e)
        return(False)
        
    except urllib.error.URLError as e:
        print("Url error")
        print(e)
        return(False)
        
    else :
        #evresi toy onomatos poy vrisketai sto <title>
        phone=""
        name=""
        
        name = re.findall(r'<title\b[^>]*>(.*?)</title>',html,re.I)
        name[0]=name[0].strip()
        #return(name)
        
        td = re.findall(r'<td\b[^>]*>(.*?)</td>',html) #vres ola ta tags <td> -> ekei mesa einai ta tilefwna
        for t in td:
            if "τηλ" in t : #otan vris to "τηλ", το τηλεφωνο ειναι 2 γραμμες παρακατω
                tel=td[td.index(t)+2]
                tel=re.findall(r'[ 0-9+-/]*',tel)
                for i in tel :
                   if len(i)>5 : phone = i
                    
        return(name[0],phone)
                
        




#main
prof_url = "http://www.ece.upatras.gr"
pattern = "/index.php/el/faculty/"

url = urllib.request.Request("http://www.ece.upatras.gr/index.php/el/faculty.html")

try:
    with urllib.request.urlopen(url) as my_page :
        encoding = my_page.headers.get_content_charset()
        html = my_page.read().decode(encoding) 
        with open("examples/ece-upatras.html","w",encoding=encoding) as f :
            f.write(html)

        
except urllib.error.HTTPError as e:
    print("HTTP error")
    print(e)
    
except urllib.error.URLError as e:
    print("Url error")
    print(e)
    
else :
    katalogos_str =""
    katalogos_dir ={}
    faculty_url=[]
    #evresi olwn twn links twn proswpikwn selidwn ka8hghtwn
    anchors = re.findall(r'<a href=(.*?)\s', html) #<a href=/index.php/el/faculty/navouris 
    for a in anchors :
        if pattern in a :
            faculty_url.append(prof_url+a)
    faculty_url=set(faculty_url) #monadika apotelesmata
    for f in faculty_url :
        tel = find_phone(f)
        if tel :
            katalogos_dir.update({tel[0]:tel[1]})
            print("Όνομα καθηγητή: {} Τηλέφωνο: {}".format(tel[0],tel[1]))
            katalogos_str += "Όνομα καθηγητή: {} Τηλέφωνο: {}\n".format(tel[0],tel[1])

    with open ("katalogos.txt","w",encoding="utf-8") as f :
        f.write(katalogos_str)
                      


        