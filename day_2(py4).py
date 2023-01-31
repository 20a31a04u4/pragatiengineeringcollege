a=int(input("enter no of days:"))
if(a>84):
      print("your plan is expired ,kindly recharge")
else:
      print("you have ",84-a, "days of your plan left")
      b=int(input("enter  no of calls:"))
      c=int(input("enter  no of msgs:"))
      d=float(input("enter data:"))
      if b<3000 and c<100 and d<2:
            print("you have",3000-b,"calls left in your plan")
            print("you have",100-c," msgs limit left today")
            print("you have",2-d,"gb left today")
      elif b>3000 and c<100 and d<2:
            print("you have exceded your montly limit")
      elif b<3000 and c>100 and d<2:
            print("message not sent")
      elif b<3000 and c<100 and d>2:
            print("you have",2-d,"gb left today")
          
           
        
            
            
              
      
