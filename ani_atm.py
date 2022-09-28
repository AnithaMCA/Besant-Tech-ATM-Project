
import mysql.connector

anidb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ani@67890",
    database="atmproject_db"
)
mycursor=anidb.cursor()

#*******************************
#mycursor.execute("create table transfer(acctype varchar(255),transferaccno int,ammount int)")
#print("transfer table created")
#mycursor.execute("create table pin(accountno int,mobilenumber int,otpnumber int,newpin_no int)")
#print("pin table created")
#mycursor.execute("create table deposit(name varchar(255),account_no int,account_type varchar(255),phone_no int,beneficiary_accname varchar(255),beneficiary_accno int,deposit_cash int)")
#print("deposit table created")


print("Welcome To ATM") 
print("Please insert your card")
print("please do not remove your chip card while processing")
print("Leave your card when your entire process complete!")
n=input("Please Select  Tamil or English Lanuage:")
n=int(input("Enter Your PIN:"))
print("*****************************************")
print("Press 1: WITHDRAWL")
print("Press 2: DEPOSIT")
print("Press 3: DISPLAY WITHDRAWL ACCOUNT DETAILS") 
print("Press 4: DISPLAY DEPOSIT ACCOUNT DETAILS")
print("Press 5: TRANSFER")
print("Press 6: MINI STATEMENT=>Display Transfer Details")
print("Press 7: PIN CHANGE")
print("press 8: DISPLAY PIN CHANGE CUSTOMERS DETAILS")


def insert_data(name,account_no,account_type,withdrawl_amount):
  sql="insert into users_data (name,account_no,account_type,withdrawl_amount) values (%s,%s,%s,%s)"
  val=(name,account_no,account_type,withdrawl_amount)
  mycursor.execute(sql,val)
  anidb.commit()
  print("Your transaction is being processed please wait....")
  print("Transaction Complete")
  print("Thank You!")

def deposit(name,account_no,account_type,phone_no,beneficiary_accname,beneficiary_accno,deposit_cash):
  sql="insert into deposit(name,account_no,account_type,phone_no,beneficiary_accname,beneficiary_accno,deposit_cash) values (%s,%s,%s,%s,%s,%s,%s)"
  val=(name,account_no,account_type,phone_no,beneficiary_accname,beneficiary_accno,deposit_cash)
  mycursor.execute(sql,val)
  anidb.commit()
  print("Your transaction is being processed")
  print("please wait....validating cash")
  print("Deposit transaction Complete")
  print("Thank You!")

def view_data():
    print("view the cash withdrawl account")
    mycursor.execute("select*from deposit")
    result=mycursor.fetchall()
    for i in result:
       print(i)

def depo_data():
    print("view the deposit account details")
    mycursor.execute("select*from users_data")
    result=mycursor.fetchall()
    for i in result:
       print(i)  

def transfer_data(acctype,transferaccno,ammount):
    sql="insert into transfer(acctype,transferaccno,ammount) values (%s,%s,%s)"
    val=(acctype,transferaccno,ammount)
    mycursor.execute(sql,val)
    anidb.commit()
    print("Your transaction is being processed")
    print("please wait....")
    print("Transfer Successfully")
    print("Thank You!") 

def mini_stmt():
    print("view the Mini Statement of Transfer Account Details")
    mycursor.execute("select*from transfer")
    result=mycursor.fetchall()
    for i in result:
       print(i)          


def pin_data(accountno,mobilenumber,otpnumber,newpin_no):
    sql="insert into pin(accountno,mobilenumber,otpnumber,newpin_no) values (%s,%s,%s,%s)"
    val=(accountno,mobilenumber,otpnumber,newpin_no)
    mycursor.execute(sql,val)
    anidb.commit()
    print("Your  is being processed")
    print("please wait....")
    print("PIN CHANGE Successfully")
    print("Thank You!") 


def show_pin():
    print("view the PIN CHANGE Details")
    mycursor.execute("select*from pin")
    result=mycursor.fetchall()
    for i in result:
       print(i)   



user=int(input("Press the key to view the particular details:"))
if user==1:
    name=input("Enter Your Name:")
    account_no=int(input("Enter Your Account Number:"))
    account_type=input("Enter Your Account Type(Kcc,Current,Saving):")
    withdrawl_amount=int(input("Enter Your Withdrawl Ammount:"))
    insert_data(name,account_no,account_type,withdrawl_amount)

elif user==2:
    name=input("Enter Your Name:")
    account_no=int(input("Enter Your Account Number:"))
    account_type=input("Enter Your Account Type(Kcc,Current,Saving):")
    phone_no=int(input("Enter Your Phone No:"))
    beneficiary_accname=input("Enter Beneficiary AccountName:")
    beneficiary_accno=int(input("Enter Beneficiary AccountNo:"))
    deposit_cash=int(input("Enter Your Deposit Ammount:"))
    deposit(name,account_no,account_type,phone_no,beneficiary_accname,beneficiary_accno,deposit_cash)

elif user==3:
    view_data()

elif user==4:
    depo_data() 
        
elif user==5:
    acctype=input("Enter your Account type:")
    transferaccno=int(input("Enter your Account Number:"))  
    ammount=int(input("Enter your Ammount to Transfer:"))
    transfer_data(acctype,transferaccno,ammount) 

elif user==6:
    mini_stmt()


elif user==7:
    accountno=int(input("Enter Your Account Number:")) 
    mobilenumber=int(input("Enter Your Mobile Number:")) 
    otpnumber=int(input("Enter Your OTP Number:")) 
    newpin_no=int(input("Enter Your New PIN  Number:")) 
    pin_data(accountno,mobilenumber,otpnumber,newpin_no)  

elif user==8:
    show_pin() 
            
else:
    print("Please...Enter 1 to 8 numbers only to view the details!") 
    print("Thank You.....")           