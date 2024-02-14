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

#4
Indeksid=["Tallinn","Narva,Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa,Lääne-Virumaa,Jõgevamaa","Tartu linn","Tartumaa,Põlvamaa,Võrumaa,Valgamaa","ViljandimaA, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
while True:
    while True:
        try:
            indeks=int(input("Sisesta viienumbriline indels: "))
        #1000,1567,959568
        #if 1000<=indeks<=99999:
            indeks_elemendide_arv=len(str(indeks))
            if indeks_elemendide_arv==5:
                pass
            else:
                print("on vaja 5 numbriline arv(indeks)")
        except:
            print("Vale andmetüüp")
        arv1=indeks//10000
        print(arv1)
        symbolid=list(str(indeks))
        sym1=symbolid[0]
        print(sym1)


