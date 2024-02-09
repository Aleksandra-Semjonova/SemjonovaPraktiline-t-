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

#2
nimed=[]
for i in range(5):
    nimi=input("Sisesta nimi: ").capitalize()
    nimed.append(nimi)

print("loetelu oli: ",nimed)
nimed.sort()
print("Loetelu sorteeritud: ",nimed)
for n in range(len(nimed)):
    print(n+1,".",nimed[n],sep="")
print("Vimasena oli lisatud: ",nimi)

uued_nimed=[]
for nimi in nimed: 
    if nimi not in uued_nimed:
        uued_nimed.aapend(nimi)
print(uued_nimed)
#uued_nimed=list(set(nimed))


