class Tiny():
    def __init__(self,name):
        self.name = name

    
t1 = Tiny("Nikos")
print(t1)
del(t1) #del deletes the object

t2 = Tiny("Giwrgos")

print(t2.name)
delattr(t2,'name') #delattr deletes an object's attribute


