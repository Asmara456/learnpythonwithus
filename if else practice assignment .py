#if else practice assignment 
# make airlines system including tickets price according to ages with me 

ticketsprice=int(input("enter price of ticket:"))
age=int(input("enter your age :"))
if age<=13:
     if ticketsprice<30000:
           print("you are a child")
     else:
           print("you are not a child   ")
elif age <=18:
      if ticketsprice<50000:
            print(" you are a teenager") 
      else :
            print( "you are not a teenager")  
elif age<=90 :
      if ticketsprice<100000:
            print("you are an adult ")    
      else: 
            print("you are not an adult ") 
else:
      if age<=100:
            print("for you we have special offer in our systems you can travel free of cost ")

print(" have a nice and safe journey with us ")

                            