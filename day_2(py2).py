email="siva@gmail.com"
pwd=123456
otp=5678
cemail=input("enter the email:")
cpwd=int(input("enter the pwd:"))

if(email==cemail and pwd==cpwd):
    print("login succesfully")
    cotp=int(input("enter the otp:"))
    if(otp==cotp):
        print("your order is placed")
    else:
        print("your otp is incorrect")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")
elif(email==cemail and pwd!=cpwd ):
    print("login failed due to pwd")
elif(email!=cemail and pwd!=cpwd):
    print("login failed due to mail and pwd")
