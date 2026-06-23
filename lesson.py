
# x=5
# x &=7
# print(x) #5 bu and-di defterde qeydlerde,+sekillerde izahi var

# x=5
# x |=7
# print(x)  #7 bu or-du

# x=5
# x ^=7
# print(x)  #2  bu xor-du 

# x=16
# x >>=2
# print(x)  #4 buda rightshift defterde qeydlere bax, >> verilen say qeder saga surusdurur riyazda x bol 2 usdu n

# x=5
# x <<=2
# print(x)  #20 buda sola surusdurur riyaziyyatda x vurulsun 2 usdu n

# x=5
# print(x:=7) #7 buda sadece verdiyimiz ededi atir x-a yeni 5 idi 7 eledik


# x=7
# y=15
# if x!=y:
#     print(f"{x} is not equal {y}")
# else:
#     print(f"{x} equal with {y}")    


# x=19
# y=18
# if x>y:
#     print(f"{x} is greater than {y}") 

# elif x==y:
#     print(f"{x} is equal {y}")

# else:
#     print(f"{x} is less than {y}")    


#tek ve cut eded tapma praqrami
# number=int(input("Enter a number:"))

# if number<0:
#     print("The entered number cannot be less than zero.")
# elif number%2 ==0:
#     print(f"{number} is an even number.") #cut
# else:
#     print(f"{number} is an odd number")   #tek     

#EXAM SCORE
# user_score=int(input("Your Exam Score: "))
# if user_score<=30:
#     print("You failed the exam.")
# elif user_score>30 and user_score<=85:
#     print("You passed the exam.")
# else:
#     print("Yo're amazing!")


# x=7
# print(not(x>3 and x<10))  #false cunki verdiyimiz sert dogru olsada qarsina not dedik deye trunu false edir 

# y=4
# print(not(y>1 and y<2))  #true, burdada icerisi false idi amma nota gore true oldu

# x=["apple","strawberry","orange"]
# y=["apple","strawberry","orange"]
# z=x

# print(x is z) #true cunki x-i z-ye atdig
# print(x is y) #false cunki iclerindekiler eyni olsada ferqli deyisenlerin icindediler
# print(x==y)  #true cunki icindekiler eynidir
# print(x is not z)  #false
# print(x is not y)  #true
# print(x!=y)       #false

x=~3
print(x)