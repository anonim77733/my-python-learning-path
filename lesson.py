# i=0
# while(i<11):   
#     print(i," ")
#     i +=1
# print("\nDone") #netice alt alta 0 1 2 3 4 5 6 7 8 9 10

# i=0
# while(i<11):
#     i+=1
#     print(i,end=" ")
# print("\nDone")    #netice 1 2 3 4 5 6 7 8 9 10 11

# i=1
# while(i<=7):
#     print(i,end=" ")
#     i+=1
#     if(i==4):
#         break
# print("\nDone")    #1 2 3 done 

 ##ENDLESSS!!!!
# i=1
# while(i<=7):
  
#     print(i,end=" ")
#     if(i==4):
#         continue
#     i+=1        #burda ini asagida artiririg deye 1 2 3 4 4 4 4 .....sonsuz olur cunki if den sora ancag 4 e baxir ve 4 de kicikdi deye sonsuza girir
#                 #bunu duzeltmek ucun ini yuxariya yazaciq
# print("\nDone")    


# i=1
# while(i<=7):
#     i+=1
#     print(i,end=" ")
#     if(i==4):
#         continue 
# print("\nDone")      #netice 2 3 4 5 6 7 8 amma printi if sertinnen sora yazsa idik 4 olmuyacagdi meselen onuda eliyek

# i=1
# while(i<=7):
#     i+=1
#     if(i==4):
#         continue
#     print(i,end=" ")  #netice 2 3 5 6 7 8 burda uje 4 den sora davam edir yazdirmadan cunki sertimiz continue-dir
# print("\nDone")       #8 de ona gore yazilirki 7 beraberdi sora onu artirir 8 yazir 8 ama boyukdu deye dovreye gire bilmir

##ELSE ILE WHILE

# i=1
# while(i<=7):
#     print(i,end=" ")
#     i+=1
# else:
#     print(f"\n i({i}) variable is no longer than 7") 
# print("While loop is over")         #1 2 3 4 5 6 7 
#                                       #i(8) variable is no longer than 7
#                                     #While loop is over

# ##LISTLERDE WHILE
# myNumbers=[34,19,45,78,4,66]
# i=0                            #0 deyirik cunki 0ci indexden baslasin
# while(i<len(myNumbers)):       #burdada uzunlugu 6 olduguna gore i<6 olmus olur eslinde
#     print(myNumbers[i])
#     i+=1                        #netice alt alta 34 19 45 78 4 66

# i=70
# while(i>=0):
#     print(i,end=" ")
#     i-=5               #70 65 60 55 50 45 40 35 30 25 20 15 10 5 0 





#{

# myNumbers=[]
# i=0                                    
# while(i<7):
#     input_number=int(input("Enter an integer:"))
#     myNumbers.append(input_number)
#     i+=1

# myNumbers.sort()  
# print(myNumbers)    #netice [11, 33, 44, 55, 66, 77, 99]  #isdifadecinin elave elediyi

#burda ne elemisik olduq bos list yaratdig sora yene indexe gore 0dan basladiq isdifadecinin yazdigi reqemleri aldiq ve listimize elave eledik
#i her defesinde 1 artdigi ucun isdifadeci 7 olana kimi davam edecek ve 7 uzunlugda list yaratmis olacaq

#eger neticeni list seklinde gorsetmek isdemesek bunu bele etmek lazimdi(esl is muhiti):

# myNumbers=[]
# i=0                                    
# while(i<7):
#     input_number=int(input("Enter an integer:"))
#     myNumbers.append(input_number)
#     i+=1
# myNumbers.sort()  
# x=0
# while(x<7):
#     print(myNumbers[x],end=" ")
#     x+=1                             #netice uje 11 33 44 55 66 77 99
    
#}



#{
# ##tek ve cut reqem yazdirma 

# start_number=int(input("Enter The Start Number:"))   #ferz eliyekki 0 dedik
# end_number=int(input("Enter The End Number:"))       #ferz eliyekki 10 dedik
# while(start_number<end_number):
#     if(start_number %2 ==0 or start_number %2 !=0):
#         print(start_number,end=" ")
#         start_number+=1                              #netice 0 1 2 3 4 5 6 7 8 9

# #burda isdifadeciden aldigimiz baslama bitme saylarini donguye saldiq ve ededlerin 2 ye bolunmesinnen qaligina gore 0 olsa cut olmasa tek olur        

#}


# while(True):
#     name=input("Enter Your Name:")
#     if(name==""):
#         continue
#     else:
#         break
# print(f"Your name is {name}")     #isdifadeci hecne yazmadigca dongu davam edir ad yazana kimi


##faktoryal hesablayan pragram

result=1
i=1
number=int(input("Enter an integer:")) #ferz eliyekki 5 girdik
while(i<=number):
    result*=i
    i+=1
print(f"{number}!={result}")    #netice 5!=120
