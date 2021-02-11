''' Εκφώνηση:

η κλάση Point
Να ορίσετε μια κλάση Point που περιγράφει σημεία (x,y) στο καρτεσιανό επίπεδο.
Ο δημιουργός αντικειμένων της κλάσης δέχεται ως όρισμα τη θέση του σημείου (x,y), όπου x,y ακέραιοι.
Τα αντικείμενα της κλάσης θα πρέπει να έχουν μια μέθοδο distance(p) που λαμβάνει ως όρισμα
ένα άλλο σημείο p και υπολογίζει την απόσταση του σημείου από το p.
Η κλάση Point περιλαμβάνει ως γνώρισμα κλάσης μια λίστα που περιέχει τα σημεία που έχουν δημιουργηθεί.

η εφαρμογή Point

Να κατασκευάσετε πρόγραμμα που επιτρέπει στον χρήστη να ορίσει διαδοχικά σημεία.
Για κάθε νέο σημείο που εισάγεται να εμφανίζει τις αποστάσεις των ήδη υφιστάμενων σημείων από το νέο σημείο.
Με <enter> τερματίζει το πρόγραμμα.
Σημείωση: οι συντεταγμένες να δίνονται ως 2 ακέραιοι χωρισμένοι με κόμμα:
100,50 (δεν απαιτείται αμυντικός προγραμματισμός, για έλεγχο της εισόδου του χρήστη).

****MODIFICATION*****

Άσκηση: να τροποποιήσετε τον κώδικα της κλάσης Point ώστε ο χρήστης να μπορεί να διαγράψει ένα σημείο με βάση τις
συντεταγμένες του.

Ο χρήστης θα πρέπει να δίνει ένα νέο σημείο με την εντολή insert x,y
και να διαγράφει ένα σημείο με την εντολή delete x,y'''

#2 points distance (Euclidean):
#p1 = (x1,y1)
#p2 = (x2,y2)
#dist = sqrt( (x2-x1)^ 2 + (y2-y1)^2)

'''class definition'''
import math

class Point():
    the_points = [] #list of points in the class
    
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)
        Point.the_points.append(self) #pass the list as class attribute
        
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    
    def distance(self, p):
        return math.sqrt((self.x -p.x)**2 + (self.y - p.y)**2)
    
    
#main program

while True:
    command  = input("Insert a point with (insert x,y) or Delete a point with (delete x,y): ")
    if command == "": break
    if len(command.split()) < 2:
        print("Wrong syntax")
        continue
    
    coords = command.split(' ')[1] #split with space between the insert/delete and (x,y)
    if coords.count(',') != 1 :
        print("Wrong syntax")
        continue
    x,y = coords.split(',')
    if x.isdigit() and y.isdigit():
        if command.split()[0] == 'insert' :
            #create object
            new_point = Point(x,y)
            
            print("There are {} points in total".format(len(Point.the_points))) #print total points in list
        
            for p in Point.the_points:
                if p != new_point:
                    print("The distance between {} and  new point {} is {:.2f}"\
                          .format(p, new_point, p.distance(new_point)))
            print('\n')
        elif command.split()[0] == 'delete' :
            deleted = False
            new_points = []
            for p in Point.the_points:
                if int(x)==p.x and int(y)==p.y:
                    print("Point {} deleted".format(p))
                    Point.the_points.remove(p)
                    del p
                    print("There are {} points after the deletion".format(len(Point.the_points)))
                    deleted = True
                
            if deleted==False:
                print("point ({},{}) not found!".format(x,y))
        else:
            print("Wrong syntax")
            continue
        
                    
            
