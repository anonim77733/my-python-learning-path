# text = "   Mən Python\'u çox sevdim! Bu dil superdir.   "
# text=text.strip()
# text=text.replace("superdir","mukemmeldir")
# print(text)


# username = "mUhAnDiS_2026"

# username=username.upper()
# print(username)

# username=username.lower()
# print(username)

# print(len(username))

# sentence = "Python,AI,Machine,Learning"
# sentence=sentence.split(",")
# print(sentence)

# text="Suni\nIntellekt"
# print(text)

# new_word="Hel"
# new_word="Hel\bllo"
# print(new_word)

# new_word_2="male\rp"
# print(new_word_2)

# user_email=input("Username Email:")

# correct_type=user_email.strip()
# correct_type=user_email.replace(" ","").lower()

# print(correct_type)

# name="Eli"
# role="AI Engineer"
# sentence=f'Hello {name} {role} you are welcome'
# print(sentence)

# accuracy=0.98765
# print(f"accuracy is {accuracy:.2f}")

# user_midterm_score=float(input("Your Midterm Score:"))
# user_final_score=float(input("Your Final Score:"))

# average_scor=((user_midterm_score+user_final_score)/2)
# user_average_score=f"{average_scor:.2f}"

# percent_score=((user_midterm_score*0.40)+(user_final_score*0.60))
# user_percent_score=f"{percent_score:.2f}"

# print("Your midterm score is:",user_midterm_score)
# print("Your final score is:",user_final_score)
# print("Your average score is:",user_average_score)
# print("Your percent Score is:",user_percent_score)


# text="Sağlam"
# test1=text.encode(encoding="ascii",errors="backslashreplace")
# print(test1)


# user_input=input("Add your text:")

# #broken_data=user_input.encode("ascii")

# fixed_data=user_input.encode(encoding="ascii",errors="replace")

# print(fixed_data)


# user_password=input("New password(only words and numbers):")
# if user_password.isalnum():
#     print("The password is accepted.")
# else:
#     print("The password isn't correct.")    

# text="Learning Python is very interesting.Everthing we can do in python." 
# print(text.count("Python"))
# print(text.find("interesting"))   

text="Learning Python is very interesting.Everthing we can do in python."
print(text.find("Java"))
print(text.index("Java"))


# text="280920"
# x="\u0030" #0
# y="\u00B2" #x kvadrati

# print(x.isdigit())
# print(y.isdigit()) #true
# print(int(x))

# a="AnonimUnknown"    #true
# b="3anonim"          #false
# c="anonim3"          #true
# d="anonim unknown"   #false
# e="anonim-unknown"   #false
# f="anonim_unknown"   #true

# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())
# print(e.isidentifier())
# print(f.isidentifier())


# x="\u0033"
# y="\u00B2"
# print(x.isnumeric())  #true
# print(y.isnumeric())  #true only numbers,and kvadratik x-kvadrati


# text="anonim unknown \u0032 12 ?@.!*"
# print(text.isprintable())   #true yalniz ekrana gorunmeyen karakterlerde false meselen \n \r amma \u0032 2 reqemini ifade elediyine gore true

# names=("anonim","unknown","anonymous")
# result=",".join(names)
# print(result)   #anonim,unknown,anonymous sadece birlesdirir hansisa bir ayirici ile meselen- olsa - ile birlesdirir

# myDict={"name":"anonim","country":"france"}
# print("-".join(myDict))    #name-country
# print("-".join(myDict["country"])) #f-r-a-n-c-e

# text="Hello, Python"
# myDict={80:84,108:65}
# result=str.maketrans(myDict)
# print(text.translate(result))  #HeAAo, Tython
# 
  
# text="Hello, Python"
# x="PH"  #P H ile H m ile evezlenir
# y="Hm"
# z="l"  #z yeni ucuncu deyisen isdediyimizi silir
# result=str.maketrans(x,y,z)  
# print(text.translate(result))  #meo, Hython

#print(str.maketrans(x,y,z)) #dictionary seklinde gorsenir


# text="i can eat apple all day"
# print(text.partition("apple"))  #3 hisseye bolur tupple

# text="I can eat cherry,cherry,cherry every day"
# result=text.replace("cherry","apple",2)
# print(result)  #apple apple cherry 2 defe deyisdi

# text="i can eat strawberry all day.strawberry is my favorit fruit."
# result=text.rpartition("strawberry")  #sag teref yeni en sondaki strawberry olan yerden bolur
# print(result)  #('i can eat strawberry all day.', 'strawberry', ' is my favorit fruit.')

text="i could eat apple all day,\n apple is \n my favorite fruit"
result=text.splitlines(True)
print(result)
