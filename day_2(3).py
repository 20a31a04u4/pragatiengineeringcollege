email="siva@gmail.com"
pwd=123456
cemail=input("enter the email:")
cpwd=input("enter the pwd:")

if(email==cemail and pwd==cpwd):
    print("login succesfully")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")
elif(email==cemail and pwd!=cpwd):
    print("login failed due to pwd")
elif(email!=cemail and pwd!=cpwd):
    print("login failed due to mail and pwd")

