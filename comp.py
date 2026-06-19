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
