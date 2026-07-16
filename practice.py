# user_input=int(input("Enter an integer:"))
# prime_numbers=[]

# if(user_input<=0):
#     print("Please,enter an integer greater than 0!")
# elif(user_input<2):
#     print("The smallest prime number is 2.")
# else:
#     prime_numbers.append(2)
#     for i in range(3,user_input+1,2):
#         for j in range(3,int(i**0.5)+1):
#             if(i%j==0):
#                 break
#         else:
#             prime_numbers.append(i)
#     print(f"{prime_numbers}")    



# colors=["black","white","brown"]
# cars=["mercedes","bmw","audi"]

# for outer in colors:
#     for inner in cars:
#         print(outer,inner)



## GCD and LCM

# number1=int(input("Enter the first number:"))
# number2=int(input("Enter the second number:"))
# smaller=min(number1,number2)

# for i in range(smaller,0,-1):
#     if(number1 %i ==0 and number2 %i ==0):
#         gcd=i
#         break
# lcm=(number1*number2)//gcd
# print(f"The GCD of {number1} and {number2} is {gcd}")  #ebob
# print(f"The LCM of {number1} is {number2} is {lcm}")   #ekob



## GCD and LCM 
# input_numbers = []
# i = 0

# # 1. İstifadəçidən 10 dənə düzgün ədəd alıb siyahıya yığırıq
# while(i < 10):
#     user_input = int(input("Enter an integer: "))
#     if user_input <= 0:
#         print("Please, enter an integer greater than 0!")
#         continue
#     else:
#         input_numbers.append(user_input)
#     i += 1

# # --- BİLDİYİMİZ METODLA ZƏNCİRVARİ HESABLAMA ---

# # Siyahının ilk elementini başlanğıc EBOB və EKOB qəbul edirik
# current_gcd = input_numbers[0]
# current_lcm = input_numbers[0]

# # 1-ci indeksdən başlayaraq digər ədədləri növbə ilə yoxlayırıq
# for item in input_numbers[1:]:
    
#     # --- 1. EBOB (GCD) Tapılması ---
#     # current_gcd ilə növbəti ədədin (item) ortaq bölənini tapırıq
#     smaller = min(current_gcd, item)
#     gcd_found = 1 
    
#     for j in range(smaller, 0, -1):
#         if (current_gcd % j == 0) and (item % j == 0):
#             gcd_found = j
#             break # Ən böyüyünü tapan kimi dövrü qırırıq
            
#     # --- 2. EKOB (LCM) Tapılması ---
#     # Düstur: (a * b) // EBOB. 
#     # Buradakı EBOB elə yenicə yuxarıda tapdığımız 'gcd_found' ədədidir!
#     lcm_found = (current_lcm * item) // gcd_found
    
#     # Yekun yaddaşı yeniləyirik ki, növbəti dövrdəki ədəd bunlarla müqayisə olunsun
#     current_gcd = gcd_found
#     current_lcm = lcm_found

# # --- NƏTİCƏ ---
# print(f"\nDaxil etdiyiniz siyahi: {input_numbers}")
# print(f"Bütün siyahinin EBOB-u: {current_gcd}")
# print(f"Bütün siyahinin EKOB-u: {current_lcm}")  
    



                
        
