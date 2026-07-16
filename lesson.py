# user_input=int(input("Enter an integer:"))
# isPrime=True

# if user_input <= 0:
#     print("Please enter a positive number greater than 0!")

# elif(user_input>0 and user_input<2):
#     print("The smallest prime number is 2.")

# else:
#     for i in range(2,int(user_input**0.5)+1):  #**0.5 kokde user_input demeydi,+1 ona gore yazdiqki girilen ededden oncesini hesablamasin
#         if(user_input %i ==0):                 # int ona gore deyirikki hesablamada vergulleri silsin
#             isPrime=False
#             break
#     if(isPrime):
#         print(f"{user_input} is prime number.")
#     else:
#         print(f"{user_input} is not prime number.")   #praktika hissesinde ozum daha basa busulen yazmisam bax!

#İstifadəçinin daxil etdiyi ədədi (user_input), dövrdən gələn anlıq i rəqəminə böl.
# Əgər qalıq tam olaraq sıfıra bərabərdirsə (== 0), deməli bu ədəd həmin i rəqəminə tam bölünür!





##EBOB EKOB tapma

# number1=int(input("Enter the first number:"))
# number2=int(input("Enter the second number:"))
# smaller=min(number1,number2)    #min verilenlerden kiciyini getirir

# for i in range(smaller,0,-1):   #yeni balaca ededden sifira qeder 1-1 azalda azalda ged,niye cunki 6,18 olsa 6 7,8,9...a bolunmur menasi yoxdu boyuyun
#     if(number1 %i ==0 and number2 %i ==0):   #1-ci 2-ci ededin i ye bolunmesinnen qalan qalig sifir olsa ebobu tapir atir gcd-ya 
#         gcd=i
#         break

# lcm=(number1*number2)//gcd  #ekob, bu dusturdu ekob beraberdi x*y bolunsun ebob(x,y) 
# print(f"The GCD of {number1} and {number2} is {gcd}")  #greatest common divisor   
# print(f"The LCM of {number1} and {number2} is {lcm}")  #least common multiple  




## Fibonacci 

fib_element=int(input("Enter the number of fibonacci elements:"))

if(fib_element <=0):
    print("Please,enter the number greater than 0!")
else:
    fibonacci_series=[]
    first=0
    second=1
    for _ in range(fib_element):
        fibonacci_series.append(first)
        temp=first+second
        first=second
        second=temp
    print(f"The first {fib_element} elements of the Fibonacci series:{fibonacci_series}")    