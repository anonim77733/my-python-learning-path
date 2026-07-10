# while(True):
#     name=input("Enter Your Name:")
#     if(name==""):
#         continue
#     else:
#         print(f"Your name is {name}")
#         break

# result=1
# i=1
# user_input=int(input("Enter The Number:"))
# while(i<=user_input):
#     result*=i
#     i+=1
# print(f"{user_input}!={result}")  

# odd_numbers=[]
# even_numbers=[]

# i=0

# while(i<10):
#     input_number=int(input("Enter an integer:"))
#     if input_number %2 ==0:
#         even_numbers.append(input_number)
#     else:
#         odd_numbers.append(input_number)    
    
#     i+=1
    



# odd_numbers.sort()    
# even_numbers.sort()

# print('Odd Numbers:',*odd_numbers)
# print('Even Numbers:',*even_numbers)


# myList=["Mercedes","Bmw","Audi","Porsche","Ferrari","Aston Martin"]


# myList.extend(["Hyundai","Toyota","Nissan"])

# myList.insert(2,"Volvo")


# print(myList)

# text="I love to practice in python\tAnd i'm training every day."
# print(text.index("practice"))  #10 yeni 10 cu indexden





##Streaming Data
# data_stream=[]
# i=0

# while(i<5):
#     user_input=input("Enter a data:")
#     data_stream.append(user_input)
#     i+=1

# data_stream.sort()
# print("Entered Datas:",*data_stream)   #Entered Datas: AI Engineer CyberSecurity Engineer Data Engineer Programming Developer Software Engineer


##Managing Loss
# loss=1.0
# while(loss>0.1):
#     print(f"Current error value:{loss:.1f}")
#     learning_rate=float(input("Enter a float:"))
#     loss-=learning_rate
# print("The model was successfully trained!")  

# #netice Current error value:1.0
# # Enter a float:0.1
# # Current error value:0.9
# # Enter a float:0.3
# # Current error value:0.6
# # Enter a float:0.5
# # Current error value:0.1
# # Enter a float:0.2
# # The model was successfully trained!


##Data temprature

# while True:
#     user_input=int(input("Enter the temperature:"))
#     if(user_input<=0):
#         print("System is stopped.")
#         break
#     elif(user_input>=50):
#         print("Danger! An anomaly has been detected!")
#         break
#     else:
#          print("Data is normal; the next sensor is being checked...")
#          continue
        

##number guessing game

# print("Hello! Welcome to the Number Guessing Game.Let's start")

# low_number=int(input("Enter a low number:"))
# high_number=int(input("Enter a high number:"))
# print(f"Okey,now you have 7 chances to find number between {low_number} and {high_number}.Let's start.")

# ch=7
# gc=0

# import random
# num=random.randint(low_number,high_number)

# while(gc<ch):
#     gc+=1
#     guess=int(input("Enter your guess:"))
#     if(guess==num):
#         print(f"Correct,the number is {num}.You found the number {gc} attempts.")
#         break    
#     elif(gc>=ch and guess !=num):
#         print(f"Sorry,the number was {num}.Better luck nect time.")
#         break
#     elif(guess>num):
#         print("Too high,try a lower number.")
#     elif(guess<num):
#         print("Too low,try a higher number.") 


##sade eded tapma pragrami
# print("Hello,Welcome to the finding prime number program!")
# user_input=int(input("Enter an integer:"))
# number="is prime"

# if(user_input<=0):
#     print("Please,enter a positive number greater than 0!")
# elif(user_input>0 and user_input<2):
#     print("The smallest prime number is 2.")
# else:
#     for i in range(2,int(user_input**0.5)+1):
#         if(user_input %i ==0):
#            number="is not prime"
#            break
    
    
#     if(number=="is prime"):
#         print(f"{user_input} is prime number.")
#     else:
#         print(f"{user_input} is not prime number.") 
# 







# print("Hello,Welcome to the finding prime number program!")
# i=0
# prime=[]
# is_not_prime=[]


# while(i<10):
#     number="is prime"
#     user_input=int(input("Enter an integer:"))
#     if(user_input<=0):
#         print("Please,enter a positive number greater than 0!")
#         continue
#     elif(user_input>0 and user_input<2):
#         print("The smallest prime number is 2.")
#         continue
#     else:
#         for item in range(2,int(user_input**0.5)+1):
#             if(user_input %item ==0):
#                 number="is not prime"        
#                 break
            
        
#         if(number=="is prime"):
#             prime.append(user_input)
#         else:
#             is_not_prime.append(user_input)
#     i+=1        

# prime.sort()
# is_not_prime.sort() 

# print("Prime Numbers:",*prime)
# print("Is not Prime Numbers:",*is_not_prime)







user_input=int(input("Enter an integer:"))
prime_numbers=[]


    
if(user_input<=0):
    print("Please,enter an integer greater than 0!")
    
elif(user_input>0 and user_input<2):
    print("The smallest prime number is 2.")
    
else:
    prime_numbers.append(2)
    for i in range(3,user_input+1,2):
        for j in range(3,int(i**0.5)+1):
            if( i % j ==0):
                break
        else:
            prime_numbers.append(i)

print(f"{prime_numbers}")                