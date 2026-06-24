# myList=["apple","paron","cherry","watermelon","melon","apple","paron"]
# myList=list(dict.fromkeys(myList))
# print(myList)
# print(type(myList))
# #burda bizim listde tekrarlama olur deye ve bunu qaldirmaq ucun dictionarya cevirdik sonra ise liste cevirdik
# #buna gorede listimizdeki tekrarlananlari sildi,cunki dict tekrara icaze vermir

# number=list((1,2,3,4,5,6,1,2,3))
# number=list(dict.fromkeys(number))
# print(number)    #[1, 2, 3, 4, 5, 6]

# fruits=["apple","paron","watermelon","melon"]
# fruits[2]="grape"
# print(fruits)  #2ci indexdeki watermelonun yerine grape qoyduq

# fruits=["apple","paron","watermelon","melon"]
# print(len(fruits))  #4
# fruits[1:2]=["grape","banana"]
# print(len(fruits))     #5 burda 1:2 dediyimize gore yalniz birinci indexi grape eledi ve banana verdiyimiz ucunde onun sagina yeni veri girdi
# print(fruits)


# fruits=["apple","paron","watermelon","melon"]
# fruits[:3]=["banana"]
# print(fruits)   #['banana', 'melon'] burdada 0,1,2 ci indexleri silib yerine banana yazdiq


# fruits=["apple","paron","melon"]
# fruits.append("watermelon")
# print(fruits)   #['apple', 'paron', 'melon', 'watermelon']  sonuna elave edir 

# fruits=["apple","paron","melon"]
# fruits.insert(1,"cherry")
# print(fruits)    #['apple', 'cherry', 'paron', 'melon']  buda isdediyimiz indexe elave edir ve hemin yerdeki saga gedir

# fruits=["apple","paron","melon"]
# fruits2=["watermelon","grape","strawberry"]
# fruits.extend(fruits2)
# print(fruits)    #['apple', 'paron', 'melon', 'watermelon', 'grape', 'strawberry'] iki listi birlesdirir
#                  # ama liste tek list yox tupple,set,dictionary de elave etmek olar netice yene listdi

# fruits=["apple","paron","melon"]
# fruits2=("watermelon","grape","strawberry")
# fruits.extend(fruits2)
# print(fruits)    #['apple', 'paron', 'melon', 'watermelon', 'grape', 'strawberry']

#DUZGUN LIST KOPYALAMA

# fruit=["apple","paron","melon"]
# new_fruit=fruit      #bu cur kopyalama olmaz bu iki eyni seyi yaradir be elaveleri her ikisine edir 

# new_fruit.append("cherry")
# print(fruit)
# print(new_fruit)  #NETICE CHERRYINI HER IKISINE ELAVE EDIR CUNKI KOPYALANMADI EYNI YARATDI

      ##BIRINCI DUZGUN KOPYALAMA

# fruit=["apple","paron","melon"]
# new_fruit=fruit.copy()

# new_fruit.append("cherry")   #['apple', 'paron', 'melon']
#                             #['apple', 'paron', 'melon', 'cherry'] burda ama duzgun kopyaladiq deye yalniz new fruite elave etdi
# print(fruit)
# print(new_fruit)

    ###IKINCI DUZGUN KOPYALAMA
# fruit=["apple","paron","melon"]
# new_fruit=list(fruit)

   ###UCUNCU DUZGUN KOPYALAMA
# fruit=["apple","paron","melon"] 
# new_fruit=fruit[:]

#AMMA LISTIN ICINDE IKI LIST VARSA YENI IKI LISTLI BIR LISTI KOPYALAMAQ UCUN DERIN KOPYALAMA LAZIMDI

# import copy

# list=[[1,2],[2,3]]  #bu iki listli 1 listdi,1 listin icinde 2 list var
# new_list=copy.deepcopy(list)  
#  #YOXLAMAQ UCUN DEYISEN ELAVE EDEK

# new_list[0][0]=16  #0ci setir 0ci sutuna   
# new_list[0][1]=67  #0ci setir 1ci sutuna
# new_list[1][1]=25  #1ci setir 1ci sutuna   [[1, 2], [2, 3]]
#                                           #[[16, 67], [2, 25]]  netice bu cur oldu

# print(list)
# print(new_list) 

# mylist=["apple","paron","melon","watermelon"]
# mylist.remove("paron")   #['apple', 'melon', 'watermelon'] isdediyimizi silir
# print(mylist)

# mylist=["apple","paron","melon","watermelon"]
# mylist.pop()  # ['apple', 'paron', 'melon'] burdada pop en sondakini silir
# print(mylist)

# mylist=["apple","paron","melon","watermelon"]
# del mylist[2]    # ['apple', 'paron', 'watermelon'] ikinci indexdeki melonu silir
# print(mylist)

# mylist=["apple","paron","melon","watermelon"]
# mylist.clear()
# print(mylist)   #[] burda icindekileri bosaldir amma list qalir

# mylist=["apple","paron","melon","watermelon","paron","paron"]
# result=mylist.index("paron")  #1 burda yalniz ilk yerde olanin indexini getirir
# print(result)

# mylist=["apple","paron","melon","watermelon","paron","paron"]
# result=mylist.count("paron")
# print(result)    #3 nece paron oldugunu getirir,gormek ucun hansisa deyisene atiram bele vermir sade

# mylist=["apple","paron","Melon","Watermelon"]
# mylist.sort()   #bu sort a-z ye ve ya 1,2,3... duzgun siralayir amma icerisinde boyuk kicik herflerden ilk once boyuye baxir
                 # ['Melon', 'Watermelon', 'apple', 'paron']               
                 # #ona gorede asagidaki kimi daha duzgundu
# print(mylist)

# mylist=["apple","paron","Melon","Watermelon"]
# mylist.sort(key=str.lower)   #['apple', 'Melon', 'paron', 'Watermelon'] burda boyuk herflerde olsa hamisini kicikle oxudu
# print(mylist)

# myList=[18,4,87,16,55]
# myList.sort()
# print(myList)    #[4, 16, 18, 55, 87]

#    ## AMMA BOYUKDEN KICIYE DOGRU ETMEK UCUN
# myList=[18,4,87,16,55]
# myList.sort(reverse=True)   #burdada reverse true deyerek yeni eksine dondur demis oluruq
# print(myList)               #[87, 55, 18, 16, 4]

# mylist=["Apple","Paron","Melon","Watermelon"] #hamisini boyuk elemeliyik key kodunu siliriy deye
# mylist.sort(reverse=True)   #['Watermelon', 'Paron', 'Melon', 'Apple']
# print(mylist)


  ##ISDEDIYIMIZ SAYIN EN YAXININNAN EN UZAGINA DOGRU SIRALAMA
def mySort(x):
    return abs(x-20)  #isdeyimiz 20-e en yaxin olannan en uzaga siralasin 

    
myNumbers=[70,19,34,23,7,34]
myNumbers.sort(key=mySort)  #mySort yeni verdiyimz functiona gore siralamasini deyirik 
                            #yeni ededleri aparib xin yerine qoyacaq ve 20e yaxinlardan duzecey
print(myNumbers)                            
