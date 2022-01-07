from datetime import date
import pickle
from datetime import datetime
import calendar
import random
import os
d1=0
e=0
def get_days(b,a = None):
    from datetime import date, datetime, timedelta
    d={"Monday":0,"Tuesday":1,"Wednesday":2,"Thrusday":3,"Friday":4,"Saturday":5,"Sunday":6}
    days = []
    current = datetime.now()
    if isinstance(a, date): 
        current = a 
    date = date(current.year, current.month, 1)    
    date += timedelta(days = (d[b] - date.weekday()+7)%7)      
    while date.month == current.month: 
        days.append(date.day)  
        date += timedelta(days = 7)  
    return days
user=open("User.dat","wb+")
passen=open("Passenger.dat","wb+")
train=open("Train.dat","wb+")
l=[]
ac=[7,7,7,7,7]
g=[7,7,7,7,7]
y=[1,1,1,1,1]
p2=[]
c=0
print("===========================================================")
print("****************WELCOME TO INDIAN RAILWAYS*****************")
print("===========================================================")
while True:
    print("Choose any one option from the list")
    print('''   1. ADMINISTRATIVE MODE
       2. USER MODE
       3. EXIT''')
    print("===========================================================")
    n=int(input("Enter your choice: "))
    if n == 1:
        while True:
            print("===========================================================")
            print("~~~~~~~~~ADMINISTRATIVE MODE~~~~~~~~~")
            print("===========================================================")
            print('''   1. Create detail database
           2. Add Details
           3. Display Details
           4. User Managament 
           5. Back to Main Menu''')
            print("===========================================================")
            ch=int(input("Enter your choice: "))
            if ch == 1:
                ans='y'
                while ans=='y' or ans=='Y':
                    t=[]
                    train=open("Train.dat","ab")
                    train_no=int(input("Enter Train Number:"))
                    t.append(train_no)
                    train_name=input("Enter Train Name:")
                    t.append(train_name)
                    start=input("Enter Starting Point:")
                    t.append(start)
                    desti=input("Enter Destination:")
                    t.append(desti)
                    days=input("Days available:")
                    t.append(days)
                    dept=input("Departure time:")
                    t.append(dept)
                    arrt=input("Arrival Time:")
                    t.append(arrt)
                    FMT = '%H:%M'
                    tdelta = datetime.strptime(arrt, FMT) - datetime.strptime(dept, FMT)
                    l.append(t)
                    c+=1
                    ans=input("Enter y to continue:")
            
            elif ch == 2:
                ans='y'
                train=open("Train.dat","ab")
                while ans=='y' or ans=='Y':
                    t=[]
                    train_no=int(input("Enter Train Number:"))
                    t.append(train_no)
                    train_name=input("Enter Train Name:")
                    t.append(train_name)
                    start=input("Enter Starting Point:")
                    t.append(start)
                    desti=input("Enter Destination:")
                    t.append(desti)
                    days=input("Days available:")
                    t.append(days)
                    dept=input("Departure time:")
                    t.append(dept)
                    arrt=input("Arrival Time:")
                    t.append(arrt)
                    FMT = '%H:%M'
                    tdelta = datetime.strptime(arrt, FMT) - datetime.strptime(dept, FMT)
                    l.append(t)
                    c+=1
                    ans=input("Enter y to continue:")
                pickle.dump(l,train)
                train.close()
            elif ch == 3:
                train=open("Train.dat","rb+")
                l2=[]
                try:
                    while True:
                        l2=pickle.load(train)
                except EOFError:
                    train.close()
                sr=[]
                for i in range(1,c+1):
                    sr.append(i)
                l1=["Train Number"," SuperFastExpress","Starting Point","Destination","Days Available","Departure Time","Arrival Time"]
                row_format ="{:>25}" * (len(l1) + 1)
                print(row_format.format("", *l1)) 
                for team, row in zip(sr,l2): 
                    print(row_format.format(team, *row))
            elif ch == 4:
               print("===========================================================") 
               print("~~~~~~~~~USER MANAGAMENT~~~~~~~~~")
               print("===========================================================")
               u2=[]
               u3=[]
               c=0
               while True:
                   print('''   1. Create id database
                   2. Add Details
                   3. Display Details
                   4. Back to Administrative Mode.''')
                   ch1=int(input("Enter your choice:"))
                   if ch1 == 1:
                       ans='y'
                       while ans=='y' or ans=='Y':
                           u1=[]
                           user.close()
                           user=open("User.dat","ab+")
                           name=input("Enter the name:")
                           u1.append(name)
                           i=input("His ID Password:")
                           u1.append(i)
                           c+=1
                           ans=input("Enter y to enter more details:")
                           u3.append(u1)
        
                   elif ch1 == 2:
                       ans='y'
                       while ans=='y' or ans=='Y':
                           u1=[]
                           user=open("User.dat","ab+")
                           name=input("Enter the name:")
                           u1.append(name)
                           i=input("His ID Password:")
                           u1.append(i)
                           ans=input("Enter y to enter more details:")
                           u3.append(u1)
                           c+=1
                       pickle.dump(u3,user)
                       user.close()
                   elif ch1 == 3:
                        
                        user=open("User.dat","rb+")
                        try:
                            while True:
                                u2=pickle.load(user)
                        except EOFError:
                            user.close()
                        sr=[]
                        for i in range(1,c+1):
                            sr.append(i)
                        l1=["User Name", "ID Password"]
                        row_format ="{:>25}" * (len(l1) + 1)
                        print(row_format.format("", *l1))
                        for team, row in zip(sr,u2): 
                            print(row_format.format(team, *row))
                   elif ch1 == 4:
                        break
                   print("===========================================================")
            elif ch == 5:
                break
    if n == 2:
        print("===========================================================")
        print("TO ACCESS USER MODE ENTER YOUR ID AND PASSWORD")
        n1=input("Enter Your Name:")
        p1=input("Enter your ID Password")
        print("===========================================================")
        user=open("User.dat","rb")
        try:
            while True:
                u=pickle.load(user)
        except:
            user.close()
        d=dict(u)
        if n1 in d.keys() and d[n1]==p1:
            while True:
                print ("~~~~~~~~~USER MODE~~~~~~~~~")
                print("===========================================================")
                print("1. Book Tickets \n2. Cancellation of Tickets\n3.Train Status\n4. Passanger Details\n5. To Exit")
                ch=int(input("Enter Your Choice:"))
                if ch == 1:
                    train=open("Train.dat","rb")
                    try:
                        while True:
                            t=pickle.load(train)
                    except EOFError:
                        train.close()
                    fro=input("Stating Point:")
                    to=input("Destination:")
                    l1=["Train Number"," SuperFastExpress","Starting Point","Destination","Days Available","Departure Time","Arrival Time"]
                    print("TRAIN DETAILS FOR YOUR GIVEN SOURCE AND DESTINATION")
                    for i in range(0,len(t)):
                        if t[i][1] == (fro+"-"+to) :
                            for j in range(0,len(l1)):
                                print(l1[j]," : ",t[i][j])
                            print("SEATS AVAILABLE IN GENARAL: ",g[i])
                            print("SEATS AVAILABLE IN A/C: ",ac[i])
                            c=i
                        else:
                            continue
                    v=c
                    date2=input("Date in dd/mm/yyyy format:")
                    a=int(date2[0:2])
                    date1=input("Date of Travel in dd/mm/yy format:")
                    mm=int(date1[3:5])
                    yy=int(date1[6:])
                    date_reference = date(yy,mm,1) 
                    days = get_days(t[c][4],date_reference)
                    print(days)
                    print(int(date1[0:2]))
                    print(a+7)
                    print(int(date1[0:2]))
                    if int(date1[0:2]) in days and a+7 == int(date1[0:2]):
                            st=""
                            no=int(input("NUMBER OF TICKETS TO BE BOOKED:"))
                            n=0
                            for i in range(0,no):
                                p1=[]
                                passen.close()
                                passen=open("Passanger.dat","ab+")
                                name=input("Passenger Name")
                                age=input("Age")
                                cat=input("GENERAL(g) or A/C (ac)")
                                if cat == 'g' :
                                    e+=1
                                    n=random.randint(1000000000,9999999999)
                                    print("PNR Number for Passanger ",name," is:",n)
                                    if g[c] > 0:
                                        print("Status of ticket is CONFIRMED")
                                        st="CONFIRMED"
                                        g[c]-=1
                                    if e == 8:
                                        print("Ticket in wating ",y[c])
                                        st="WATING"+"y[c]"
                                        y[c]+=1
                                if cat == 'ac':
                                    d1+=1
                                    n=random.randint(1000000000,9999999999)
                                    print("PNR Number for Passanger ",name," is:",n)
                                    if ac[c] >= 0:
                                        print("Status of ticket is CONFIRMED")
                                        st="CONFIRMED"
                                        ac[c]-=1
                                    if d1 == 8:
                                        print("Ticket in wating ",y[c])
                                        st="WATING"+"y[c]"
                                        y[c]+=1
                                if ac[c] == -1 or g[c] == -1:
                                    ac[c]=0
                                    g[c]=0
                                print(ac)
                                print(g)
                                p1.append(n)
                                p1.append(name)
                                p1.append(age)
                                p1.append(cat)
                                p1.append(st)
                                p1.append(t[c][1])
                                p2.append(p1)
                            pickle.dump(p2,passen)
                            print("ALL TICKETS SUCCESSFULLY BOOKED")
                            passen.close()
                    if a+7 != int(date1[0:2]):
                        print("BOOKING STARTS 7 DAYS PRIOR TO THE DEPARTURE DATE")
                        if a+7 not in days:
                            print("AFTER 7 DAYS FROM TODAY THIS TRAIN IS NOT AVAILABLE")
                        if a+7 in days:
                            print("BOOKING FOR TRAIN ON ",date1," STARTS ON ",int(date1[0:2])-7,"/",int(date1[3:5]),"/",int(date1[6:]))
                if ch == 2:
                    pnr=int(input("The PNR Number of the ticket to be cancelled"))
                    for i in range (0,len(p2)):
                        if pnr == p2[i][0]:
                            print ("DETAILS OF THE TICKET")
                            l1=["PNR NUMBER","NAME","AGE","CATEGORY","STATUS"]
                            for j in range (0,len(l1)):
                                print(l1[j],":",p2[i][j])
                            ans=input("Enter C for confirmation for cancellation")
                        if ans == 'c' or ans == 'C':
                            p2=p2.pop(i)
                            break
                    f=open("Temp.dat","wb")
                    pickle.dump(p)
                    os.remove("Passenger.dat")
                    os.rename("Temp.dat","Passenger.dat")
                    f.close()

                if ch == 3:
                    train=open("Train.dat","rb")
                    try:
                        while True:
                            t=pickle.load(train)
                    except EOFError:
                        train.close()
                    num=input("NUMBER OF THE TRAIN WHOSE STATUS IS TO BE SEEN")
                    c=-1
                    for i in range (0,len(t)):
                        if num == t[i][0]:
                            c=i
                            break
                    
                    if c == -1:
                        print ("INVALID TRAIN NUMBER")
                    l1=["Train Number","Train Name","Seats Available in A/C","Seats Available in General"]
                    for i in l1:
                        print (i,"\t", end="")
                    print(t[v][0],"\t",t[v][1],"\t",ac[v],"\t",g[v])

                if ch == 4:
                    l1=["PNR","Name","Age","Category","Ticket Status","Train Travelling"]
                    for i in range(0,len(p2)):
                        for j in range (0,len(l1)):
                            print(l1[j],":",p2[i][j])
                
                    
                
                
                    
                
                
                            
                    
                    
                
                
                    
                    
                        
                    
                    
                    
                    
                    
                    

