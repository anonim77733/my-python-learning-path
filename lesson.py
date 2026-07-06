##FOR LOOP

# fruits=["grape","orange","strawbery","cherry","melon"]

# for item in fruits:
#     print(item,end=" ")   #grape orange strawbery cherry melon

#demeli burda coxlu melumatlar olsa olari tek tek cagirmiyaq deye for dongusunnen isdifade eliyiriy
# item burda bizim verdiyim her hansisa variable ola biler icine atdigi ucun
    
# fruits=["grape","orange","strawbery","cherry","melon"]
# i=0
# for item in fruits:
#     print(i,".index=",item)
#     i+=1     #netice  # 0 .index= grape
#                       # 1 .index= orange
#                       # 2 .index= strawbery
#                       # 3 .index= cherry
#                       # 4 .index= melon


#burda tek list yox hemcinin tuple dictionary string ve s hamisinda for olar
# text="Python"
# for item in text:
#     print(item,end=" ")   #P y t h o n



# fruits=["grape","orange","strawbery","cherry","melon"]
# for item in fruits:
#     print(item,end=" ")
#     if(item=="orange"):
#         break                # netice grape orange


# fruits=["grape","orange","strawbery","cherry","melon"]
# for item in fruits:
#     if(item=="orange"):
#         break
#     print(item,end=" ")      #netice grape cunki orangeden sora qirdi dongunu


# fruits=["grape","orange","strawbery","cherry","melon"]
# for item in fruits:
#     if(item=="orange"):
#         continue
#     print(item,end=" ")        #  grape strawbery cherry melon

<<<<<<< HEAD

##RANGE IN FOR

# for numbers in range(8):
#     print(numbers,end=" ")     #0 1 2 3 4 5 6 7 

# for numbers in range(1,19,2):
#     print(numbers,end=" ")       #1 3 5 7 9 11 13 15 17

# for numbers in range(8):
#     print(numbers,end=" ")
# else:
#     print("\nFor loop finished!")    #0 1 2 3 4 5 6 7 
#                                      #For loop finished!

# number=int(input("Enter an integer:"))
# for item in  range(number):
#     if(item %2 !=0):
#         continue
#     print(item,end=" ")
    
# else:
#     print("\nFor Loop is finished!")

    
# for item in range(11):
#     if(item==5):
#         pass                  #burda pass ve ya ... deyerek kecdire bilirik ona gorede netice 0 1 2 3 4 6 7 8 9 10 olur 5 i yazmir
#     else:
#         print(item,end=" ")

# else:
#     print("\nFor Loop is finished.")


##DONGU ICINDE DONGU 

# adjectives=["red","big","tasty"]
# fruits=["grape","strawbery","cherry"]
# for outer in adjectives:     #outer col demeydi inner ic demeydi
#     for inner in fruits:
#         print(outer,inner)  #burda ne eledik demeli adjectivdeki red outer icine girdi ve donguye daxil oldu yazildi sora
                            #fruitsdeki grape redin yanina yazildi sora fruitsdekiler bitmediyi ucun red tekrar yazilir ve strawberry yazilir
                            #ve bu qaydada fruitsin ici bitennen sora dongu bigi alir eyni qaydada yene yazir

# red grape
# red strawbery
# red cherry
# big grape
# big strawbery
# big cherry
# tasty grape
# tasty strawbery
# tasty cherry    


##LIST ICINDEKI LISTLERIN DONGUSU

# myNumbers=[        #bu eyni seydi myNumbers=[[20,15],[35,40],[5,19]] 
#     [20,15],
#     [35,40],
#     [5,19]
#     ]

# for item1,item2 in myNumbers:              #eger 20,15,6 yeni uc sira olsa idi for item1,item2,item3 yazmaliyiq       
#     print(f"{item1},{item2}")    #netice 20,15
#                                  #       35,40
#                                 #        5,19

# myNumbers=[
#     [20,15,6],
#     [35,40,17],
#     [5,19,31]
#     ]



# for item1,item2,item3 in myNumbers:
#     print(f"{item1},{item2},{item3}")



##ENUMERATE

# fruits=["grape","orange","strawbery","cherry","melon","pineapple","watermelon","apple"]

# for index,item in enumerate(fruits):    #indexle birlikde enumerate siradakilarin indexini yapisdirir yanina
#     print(f"{index}-{item}")            #netice 0-grape
# #                                               1-orange
# #                                               2-strawbery
# #                                               3-cherry
# #                                               4-melon
# #                                               5-pineapple
# #                                               6-watermelon
# #                                               7-apple

# fruits=["grape","orange","strawbery","cherry","melon","pineapple","watermelon","apple"]
# print(list(enumerate(fruits)))
##[(0, 'grape'), (1, 'orange'), (2, 'strawbery'), (3, 'cherry'), (4, 'melon'), (5, 'pineapple'), (6, 'watermelon'), (7, 'apple')]

# names=["Rustem","Eli"]
# ages=[25,30]
# print(list(zip(names,ages)))
#[('Rustem', 25), ('Eli', 30)]  iki ayri listi birlesdirir zip. 2 listi birlesdirib tuple edir 


# names=["Rustem","Eli"]
# ages=[25,30]
# for name,age in zip(names,ages):
#     print(f"{name} is {age} years old")
#Rustem is 25 years old
#Eli is 30 years old    
 


##NUMBER GUESSING GAME
import random
random_number=random.randint(1,100)

chance=5         #tapma sansi
score=100        #baslangic skoru
attempt_count=0  #yoxlama sayi

print("Guess a number between 1 and 100.")
print(f"Your starting score is {score}.")

while(chance>0):
    guess=int(input("Enter your guess:"))
    attempt_count+=1
    if(guess<1 or guess>100):
        print("Please! Enter a number between 1 and 100")
        continue  #continue basa qaytarir dovru
    if(guess==random_number):
        print(f"Correct the number is {random_number} and yo found a number {attempt_count} attempts.")
        print(f"Your total score is {score}")
        break
    elif(guess<random_number):
        print("Try a higher number.")
    else:
        print("Try a lower number.")
    chance-=1
    score-=20
    if(chance>0):
        print(f"Your remaining attempts:{chance}")
        print(f"Your current score:{score}") 
    else:
        print("Sorry,you ran out of attempts!")
        print(f"Your total score:{score}")           
=======
result=1
i=1
number=int(input("Enter an integer:")) #ferz eliyekki 5 girdik
while(i<=number):
    result*=i
    i+=1
print(f"{number}!={result}")    #netice 5!=120
>>>>>>> a3161d9603f320cd9fe668ba469851fd586ccc00
