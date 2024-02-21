##1
#from string import *

#vokaali=["a","e","o","u","i","j"]
#konsonanti=["q","w","r","t","p","s","d","f","g","h","k","l","z","x","c","v","b","n","m"]
#markid=punctuation
#v=k=m=t=0
#tekst=input("Sisesta sona voi lause: ").lower() #"ABCD"->"abcd!"
#tekst_list=list(tekst) #["a","w","s","c","!"]
#for sümbol in text_list:
#    if sümbol in vokaali:
#        v+=1
#    elif sümbol in konsonanti:
#        k+=1
#    elif sümbol in markid:
#        m+=1
#    elif sümbol==" ":
#        t+=1
#print("Vokaali:",v,"\nKonsonanti:",k) #print("Vokaali:",v)
#print("Konsonanti:",k)
#print("Kirjuvahemärgid:",m)
#print("Tuhikud:",t)

##2
#nimed=[]
#for i in range(5):
#    nimi=input("Sisesta nimi: ").capitalize()
#    nimed.append(nimi)

#print("loetelu oli: ",nimed)
#nimed.sort()
#print("Loetelu sorteeritud: ",nimed)
#for n in range(len(nimed)):
#    print(n+1,".",nimed[n],sep="")
#print("Vimasena oli lisatud: ",nimi)
##dublikatid 2
#uued_nimed=[]
#for nimi in nimed: 
#    if nimi not in uued_nimed:
#        uued_nimed.aapend(nimi)
#print(uued_nimed)
##uued_nimed=list(set(nimed))

##2.3
#vanused=[]
#for i in range(5):
#    vanus=int(input("Sisesta vanus: "))
#    vanused.append(vanus) #
#maksimum=max(vanused)
#minimum=min(vanused)
#summa=sum(vanused)
#keskmine=summa/len(vanused)
#print(vanused)
##Kuva ekraqanile nimi koos vanusega
#for i in range(5):
#    print(nimed[i],"on" , vanused[i],"aastat vana")

##3
#from random import *
#arvud=[]
#N=int(input("Mitu rida joonostame? "))
#S=input("Sisesta sümbol: ")
#for p in range(N):
#    arvud.append(randint(1,100))
#for p in range(N):
#    print(arvud[p]*S)

##4
#Indeksid=["Tallinn","Narva,Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa,Lääne-Virumaa,Jõgevamaa","Tartu linn","Tartumaa,Põlvamaa,Võrumaa,Valgamaa","ViljandimaA, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#while True:
#    while True:
#        try:
#            indeks=int(input("Sisesta viienumbriline indels: "))
#        #1000,1567,959568
#        #if 1000<=indeks<=99999:
#            indeks_elemendide_arv=len(str(indeks))
#            if indeks_elemendide_arv==5:
#                pass
#            else:
#                print("on vaja 5 numbriline arv(indeks)")
#        except:
#            print("Vale andmetüüp")
#        arv1=indeks//10000
#        print(arv1)
#        #symbolid=list(str(indeks))
#        #sym1=symbolid[0]
#        #print(sym1)
#        print(f"Sa elad piirkonnas {Indeksid[int(symbolid[0])-1]}")

##5
#from random import *
#from re import A 
#from string import *
#rida=[]
#N=randint(2,25)
#for i in range(N):
#    rada.append(choice(ascii_uppercase))
#print(rida)
#kogus=int(input("Mitu elemendi vahetame oma vahel "))
#if len(rida)//2>=kogus:
#    for i in range(kogus):
#        a=rida[i]
#        rida[i]=rida[len(rida)-i-1]
#        rida[len(rida)-1-i]=a
#print(rida)

#6
#nimekirja1=[]
#nimekirja=[]
#n=int(input("Nimekirja suurus: "))
#for i in ramge(n):
#    arv=randint(10,100)
#    nimekirja1.append(arv)
#    nimekirja.append(arv)
#maksimum=nimekirja[0]
#for arv in nimekirja:
#    if arv>maksimum:
#        maksimum=arv
#        vajavarv=maksimum/len(nimekirja)
#for i in range(len(nimekirja)):
#    if nimekirja[i]==maksimum:
#        nimekirja[i]=vajavarv 
#print(nimekirja1)
#print(nimekirja)

##6
#nimekirja=[] 
#n=int(input("Nimekirja suurus: "))
#for i in range(n):
#    arv=randint(10,100)


##9
#nimi=input("Mis su nimi on?")
#if nimi.isalpha():
#    print("Tere,"+ nimi.capitalize())
#    print("Nimes on",len(nimi),"tähte")
#vokaali=0
#konsonanti=0
#for i in nimi.lower():
#    if i in "aouiüõöjeä":
#        vokaali +=1
#    else:
#        konsonanti +=1
#print("Nimes on", vokaali,"vokaali ja",konsonanti,"konsonanti")
#soorteerimine_nimi=sorted(set(nimi.lower()))
#soorteerimine_i=(sorteerimine_nimi)
#print("Tähed nimes tähestiku järjekorras: ")

#16
#from random import *

#jada=["Jah, kindlasti!", "Jah!", "Võib-olla!", "Ei!"] 
#while True:
#    küsimus=input("Küsi küsimus: ")
#    if küsimus.lower()=="jah/ei":
#        vastus=choice(jada)
#        print(vastus)
#    else:
#        print("küsimus pole selge. Proovige esitada küsimus 'jah/ei' ")

#11
#kirju=["a","b","c","d", "f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#indeks = 0
#for j in kirju:
#   indeks += 1
#   kirju[indeks] = j*(indeks + 1) 
#print("tähestiku järjekord:", kirju)

#12
from random import*
arv=[]
for i in range(10):
    arv.append(randint(1,100))
minarv=min(arv)
maxarv=max(arv) 
minindex=arv.index(minarv)
maxindex=arv.index(maxarv)
arv[minindex],arv[maxindex]=arv[minindex],arv[minindex]
print(arv)
