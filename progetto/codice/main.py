import json
from variabiliGlobali import*


def analisi(count,numeri,gestore,x):
   
    for elem in oggetto_python:
        if(elem[gestore[x]]== None):

            continue
        else:
            count+= 1
            numerosss=float(elem[gestore[x]])
            numeri= numeri+numerosss
            inquinanti.update({str(gestore[x]):numeri})
    if(inquinanti.get(str(gestore[x]))==None):
        print("la media del",gestore[x],"è nulla")
    else:
        media.update({gestore[x]:(inquinanti.get(gestore[x]) / count)})
        print("la media del",gestore[x],"è ",media.get(gestore[x]))

#lista

def classifica():
    print("******************************\n"+"lista di inquinanti:\n" \
    "PM10\n","PM2.5\n","NO2\n","O3\n","SO2\n","CO\n","H2S\n","BENZENE\n","BC\n","BB\n","******************************\n")
    print("quale vuoi analizzare di dato?")



#per la stampa
def selezione(scelta,count):

    classifica()
    scelta=input().upper()
    count=0
    if(scelta in gestore):
        for elem in oggetto_python:
            count+= 1
            if elem[scelta]==None:
                print("il "+ scelta + " di "+ str(count)+" è nullo")
            else:
                print("il "+ scelta + " della "+ str(count) + "° centralina è:"+ elem[scelta])
    else:
        print("errato")
        selezione(scelta,count)
        
         
        

# inizio main vero prima è funzione
nome_file = "file/centralineFirenze.json"
with open(nome_file, "r") as file:
    stringa_json = file.read()
oggetto_python = json.loads(stringa_json)
    
for  elem in oggetto_python:
    analisi(count,numeri,gestore,x)
    x=x+1
    if(x<10):
        continue
    else:
        break
selezione(scelta,count)

