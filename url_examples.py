import urllib.request
import urllib.error
import socket

#1 katevasma toy https://www.e-ce.uth.gr/ -> an pesei to diktyo/server 8a xtyphsei o interpreter!!!

'''url = urllib.request.Request("https://www.e-ce.uth.gr/")

with urllib.request.urlopen(url) as my_page :
    #evresi kwdikopoihshs:
    encoding = my_page.headers.get_content_charset()
    html = my_page.read().decode(encoding) #an afhsw to decode() keno -> utf-8
    #print(html)'''
    

#2 try/except :

url = urllib.request.Request("https://www.e-ce.uth.gr/")

try:
    with urllib.request.urlopen(url) as my_page :
    #evresi kwdikopoihshs:
        encoding = my_page.headers.get_content_charset()
        html = my_page.read().decode(encoding) #an afhsw to decode() keno -> utf-8
        with open("examples/ece_html1.txt","w",encoding=encoding) as f :
            f.write(html)
        
except urllib.error.HTTPError as e:
    print("HTTP error")
    print(e)
    
except urllib.error.URLError as e:
    print("Url error")
    print(e)
    
#3 timeout
    
url = urllib.request.Request("https://www.e-ce.uth.gr/")

#timeout: xronos anamonhs se second
timeout = 10

socket.setdefaulttimeout(timeout) #para8yro 10sec gia epityxh syndesh, alliws retry

try:
    with urllib.request.urlopen(url) as my_page :
    #evresi kwdikopoihshs:
        encoding = my_page.headers.get_content_charset()
        html = my_page.read().decode(encoding) #an afhsw to decode() keno -> utf-8
        with open("examples/ece_html2.txt","w",encoding=encoding) as f :
            f.write(html)
        
except urllib.error.HTTPError as e:
    print("HTTP error")
    print(e)
    
except urllib.error.URLError as e:
    print("Url error")
    print(e)

#4 user agent 
    
#orismos User Agent -> gia apofygh mplokarismatos scrapping / deikse oti to request to kanei browser kai oxi programma
#xwris UA to google epistrefei -> HTTP Error 403: Forbidden
    
my_UA ="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"

url="https://www.google.com/search?client=firefox-b-d&q=corona+virus"

try:
    #dhmioyrgia lex headers -> sto pedio User-Agent -> timh my_UA (to user agent to firefox edw)
    headers = {}
    headers['User-Agent'] = my_UA
    req = urllib.request.Request(url,headers=headers)
    with urllib.request.urlopen(req) as my_page :
    #evresi kwdikopoihshs:
        encoding = my_page.headers.get_content_charset()
        html = my_page.read().decode(encoding) #an afhsw to decode() keno -> utf-8
        with open("examples/google.txt","w",encoding=encoding) as f :
            f.write(html)
        
except urllib.error.HTTPError as e:
    print("HTTP error #4")
    print(e)
    
except urllib.error.URLError as e:
    print("Url error")
    print(e)

    

    