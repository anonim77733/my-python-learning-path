#  # Store Company
# user_product_cost=float(input("Product Price:"))
# user_coupon_code=input("Coupon Code:")

# #correct coupon code=YAY2026 20% discount
# #if product final cost >100 delivery 0AZN,else 5AZN delivery

# coupon_code=user_coupon_code.upper().replace(" ","").strip()
# discount=(user_product_cost-(user_product_cost*0.20))
# final_cost_nodiscount=user_product_cost

# #eger kupon duz olarsa 
# if coupon_code =="YAY2026":
#     print("Congratulations, you won 20% discount.")
#     print("Discounted Price:",discount)

#     if discount >=100:
#         print("Your delivery price is free.")
#         print("Amount to be paid:",discount)
#     else:
#         print("Your delivery price is 5AZN.")
#         print("Amount to be paid:",(discount+5)) 
# else:
#     print("The product is registered no discount.")
#     print("Normal Price:",final_cost_nodiscount)

#     if final_cost_nodiscount >=100:
#         print("Your delivery price is free.")
#         print("Amount to be paid:",final_cost_nodiscount)
#     else:
#         print("Your delivery price is 5AZN:")
#         print("Amount to be paid:",(final_cost_nodiscount+5))             


# #SECURITY CORRECT PASSWORD
#  #correct type only words and numbers.
# user_password=input("Your New Password:").strip().replace(" ","")

# if user_password.isalnum() and not user_password.isalpha() and not user_password.isdigit():

#     if len(user_password) >=8:
#         print("Password is accepted.")
#     else:
#         print("Password isn't accepted,please use a minimum of 8 characters.")    

# else:
#     print("Password isn't correct,please don't use symbols.Only numbers and letter.")

# print(user_password)        




# user_name=input("Your Name:")

# if user_name.isalpha() and len(user_name) >=3:
#     print("Name is accepted.")
# else:
#     print("Name isn't correct!")

# # AI ANALYSIS PROGRAM
# objects=["cat","dog","cat","car","tree","cat"]

# number_of_cats=objects.count("cat")
# print(number_of_cats)

# index_car=objects.index("car")
# print(index_car)

# objects.reverse()
# print(objects)

# #DATA CLEANING
# users_old=[23, 45, 12, 19]
# users_old.append(30)
# users_old.insert(2,25)
# print(users_old)

# users_old.sort()

# deleted_user=users_old.pop()
# print(users_old)
# print(deleted_user)

# #DATA WORKS
# sensor_A = [22.5, 23.0, 21.8]
# sensor_B = [24.1, 23.5]

# sensor_A_backup=sensor_A.copy()
# sensor_A.extend(sensor_B)
# sensor_B.clear()

# print(sensor_A_backup)
# print(sensor_A)
# print(sensor_B)


# #DATA PREPROCESSING
# user_comment="   THIS PRODUCT  VERY AMAZING!  I fainted with just one word.  "
# correct_type=user_comment.lstrip().rstrip().casefold()
# search_result=correct_type.count("amazing")
# print(correct_type)
# print(search_result)


# #VALIDATION (mesajin dogrulanmasi)
# code_1 = "AI_2026"
# code_2="987321"
# code_3 = "   "

# if code_1.isalnum():
#     print("code_1 is true and accepted.")    
 
# else:
#     print("False,code_1 isn't accepted.")    

# if code_2.isdigit():
#     print("code_2 is true and accepted")
# else:
#     print("False,code2 isn't correct")   

# if code_3.isspace():
#     print("True,code_3 is only whitespace")
# else:
#     print("False,code_3 is not only whitespace")   

   
#Data Structuring
# workers=["Aydan", "Emin", "Lale"]
# external=","
# sentence=external.join(workers)

# sms="Customer ID: 4592_AZ"
# search_result=sms.index("_AZ")

# if sms.startswith("Customer"):
#     print("Sentence begin with 'customer'.")

# print(sentence)
# print(search_result)

##area of circle
# pi=3.14159
# radius_of_circle=float(input("Enter Radius:")) 
# area_of_circle=pi*radius_of_circle**2
# circumference_of_circle=2*pi*radius_of_circle


# print(f"Area of circle={area_of_circle:.2f} \nCircumference of circle={circumference_of_circle:.2f}")


##Bitwise AND & Shift
# pixel = 182
# pixel &=15
# print(pixel)
# pixel <<=2
# print(pixel)

# Membership & Logical Operators
# text="The AI model performance was amazing, not bad at all!"

# if "amazing" in text and "error" not in text:
#     print("Data is relevant for model.")
# else:
#     print("Data is not relevant for model.") 

 ##Assignment Operators)
# w= 0.5
# w**=2
# print(w)
# learning_rate=0.1
# w -=learning_rate
# print(w)

# text="sağlam"
# test=text.encode(encoding="ascii",errors="replace")
# print(test)

# text1=input("Add your text:").encode(encoding="ascii",errors="replace")
# print(text1)

##YUVARLAQLASDIRMA

# my_int_1=4.798
# my_int_2=4.253
# rounded_int_1=round(my_int_1)
# rounded_int_2=round(my_int_2)
# print(rounded_int_1)  #5
# print(rounded_int_2)  #4

# rounded_int_2=round(my_int_2,1) #burdada ikinci hisseni, netice 4.3

# num=-15
# absolute_value=abs(num)
# print(absolute_value)   #15 menfini musbet,musbete deymir

# result_1=pow(2,3)
# print(result_1)  # 2usdu 3 netice 8

# result_2=pow(2,3,5)
# print(result_2)   # (2 ** 3) % 5 netice 3

bits=35
bits %=2
print(bits)