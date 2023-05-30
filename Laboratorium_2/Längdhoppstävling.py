import statistics as stat
import os

def inmatning(Resultat):
    Antal = int(input("Hur många tävlande:"))
    
    for i in range (Antal):
        Resultat.append(float(input("Ange för deltagare " + str(len(Resultat)+1) + ": ")))
    os.system('cls')
    print("Tack för input.\n")
    return Resultat
        
def statistik(Resultat):
    print("Medelvärdet är", sum(Resultat)/len(Resultat),"m med standardavvikelse", stat.stdev(Resultat), "m. Högsta värde var", max(Resultat), "m och det lägsta " ,min(Resultat), "m.")
    print('\n')

def main():
    
    Resultat=[]
    
    while True:
        print("1. Mata in de tävlandes resultat.")
        print("2. Se statistik för tidigare inmatade")
        print("3. Avsluta")
        
        val=int(input())
        os.system('cls')
    
        if val==1:
            Resultat=inmatning(Resultat)
            
        elif val==2:
            if len(Resultat)>=2:
                statistik(Resultat)
            else:
                print("Ingen data att arbeta med. Välj först 1 och skriv resultaten för deltagarna.")
                print('\n')
            
        elif val==3:
            print("Välkommen åter!")
            break
        
        else:
            print("Välj ett giltigt alternativ.")
            print('\n')
        
main()