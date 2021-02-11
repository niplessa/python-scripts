"""παράδειγμα 1

Να δημιουργήσετε μια κλάση Employee που αφορά τους εργαζόμενους μιας επιχείρησης.
Για κάθε εργαζόμενο γνωρίζουμε το όνομα και το μισθό του.
Να δημιουργήσετε μια εφαρμογή που ζητάει διαδοχικά τα στοιχεία εργαζομένων από το χρήστη
και τα αποθηκεύει σε μια λίστα αντικειμένων τύπου Employee.
Όταν ο χρήστης δώσει <enter> το πρόγραμμα σταματάει να ζητάει στοιχεία
και τυπώνει τα στοιχεία των εργαζομένων που έχουν ήδη δοθεί.

Modification: Η λίστα employees να ειναι προσβασιμη (attribute) από την ιδια της κλάση.

"""


class Employee():
    theEmployees = []
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.theEmployees.append(self) #mod1
#main program
         
while True:
    name = input("Employees name:")
    if name == "":
        print("Exiting...")
        break
    salary = input("Employees salary:")
    
    Employee(name,salary) #create an instance of the class and append it in the list
    
print("\nEmployees List: \n")
count = 0
for e in sorted(Employee.theEmployees, key = lambda x: x.name):
    count += 1
    print("Employee {}".format(count))
    print("Name: {}".format(e.name))
    print("Salary: {}".format(e.salary))
    print("\n")
