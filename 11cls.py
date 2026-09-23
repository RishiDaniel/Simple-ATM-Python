#SIMPLE ATM NON GUI
#data base

d={"RISHI":8585,"UDHAY":5858,"RAMU":5656,"DEEPAK KALAL":9944,"HEAMANTH":6969}
B={"RISHI":2000,"UDHAY":2559,"RAMU":2595,"DEEPAK KALAL":9944,"HEAMANTH":3083}
#FUNCTIONS

def MENU():
    print("________________________")
    print("\t\t\t MENU")
    print("1.BALANCE INQUIRY\t\t\t\t\t2.WITHDRAW")
    print("3.PIN CHANGE         \t\t\t\t\t 4.FUNDS TRANSFER")
    print("5.cash deposit           \t\t\t\t\t 6.EXIT")
    print("________________________")

def BALANCE():
    q=int(input("ENTER CORRECT PASSWORD"))
    if pas==q:
        print("YOUR BANK BALANCE :",B[username])
    else:
        print("INCORRECT PASSWORD")
def withdraw():
    q=int(input("ENTER CORRECT PASSWORD"))
    if pas==q:
        w=int(input("ENTER AMOUNT TO WITHDRAW"))
        if B[username]<w:
            print("INSUFFICENT BALANCE TO WITHDRAW")
        else:
            B[username] -= w
            print("CURRENT BALANCE :",B.get(username))
    else:
        print("PLEASE ENTER CORRECT USERNAME")    

def pinchange():
    q=int(input("ENTER CORRECT PASSWORD"))
    if pas==q:
        w=int(input("ENTER OLD PIN"))
        if w ==d[username]:
            S=int(input("ENTER NEW PIN"))
            d[username]=S
            print("PASS CHANGED SUCCESFUL TO ",S)
    else:
        print("PLEASE ENTER CORRECT USERNAME")
def funds():
    q=int(input("ENTER CORRECT PASSWORD"))
    if pas==q:
        x=input("ENTER SENDER ACC NAME :").upper()
        if username==x:
            s=input("ENTER RECIEVER ACC USERNAME :").upper()
            d=int(input("ENTER AMOUNT TO TRANSFER :"))
            B[x] -= d
            B[s] +=d
            print("AMOUNT SUCESSFULLY TRANSFERED TO",s)
        else:
            print("PLEASE ENTER CORRECT USERNAEM")

def back():
    exit()

def deposit ():
    q=int(input("ENTER CORRECT PASSWORD"))
    if pas==q:
        s=int(input("ENTER CASH TO  DEPOSIT"))
        B[username] +=s
    else:
        print("ENTER CORRECT USERNAME ")
        
def SIGNUP():
    q=input("CREATE USERNAME :").upper()
    if q not in d and q not in B:
        while True:
            p1=int(input("ENTER PIN"))
            s=len(str(abs(p1)))
            if s==4:
                d[q]=p1
                B[q]=0
                print("ACCOUNT SUCCESFULLY CREATED !!")
                break
            elif s>4 or s<4:
                print("PLEASE CHOOSE 4 DIGIT PIN")
                continue 
    else:
        print("USER ALREADY EXIST")
 #LOGIN  PAGE
while True:
    print("\t\tWELCOME TO UR BANK")

#taking choice from user    
    print("1.SIGN UP : \t\t\t\t 2.LOGIN :")
    Q=int(input("ENTER YOUR CHOICE :"))
    if Q==1:
        SIGNUP()
    elif Q==2:
        username=input("ENTER CORRECT USERNAME :").upper()
        if username in d:
            pas=int(input("ENTER CORRECT PASSWORD :"))
            if d[username]==pas:
                MENU()
                x=int(input("ENTER YOUR CHOICE :"))
                if x==1:
                    BALANCE()
                elif x==2:
                    withdraw()
                elif x==3:
                    pinchange()
                elif x==4:
                    funds()
                elif x==5:
                    deposit()
                elif x==6:
                    back()
             
else:
    print("\nPLEASE ENTER THE CORRECT USERNAME")
