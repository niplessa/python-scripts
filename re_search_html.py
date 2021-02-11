'''19. Regular Expressions : Παραδείγματα
(1)Να βρείτε αν υπάρχει email στη σελίδα.
(2)Να βρείτε το περιεχόμενο της ετικέτας <title>
(3) .. και των ετικετών <h2> της σελίδας αυτής.'''

import re

with open("upatras.html","r",encoding='utf-8') as f :
    site = f.read()

#αναζήτηση email
print("Αναζήτηση email:")
email_pattern = r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"
emails = re.findall(email_pattern,site,re.I)
for e in set(emails) : #set -> mas dinei monadika apotelesmata
    print(e)
    
#αναζήτηση περιεχομένου <tag>
while True :
    tag=input("\nDwse to tag poy se endiaferei: ")
    if tag == "" : break
    tag_pattern = r'<'+tag+r'\b[^>]*>(.*?)</'+tag+r'>'
    tags = re.findall(tag_pattern,site,re.I)
    print("Αναζήτηση tag: {}: ".format(tag))
    for t in set(tags) :
        print(t)
    