from math import pi

def Planet_massa (r, T):
    G=6.67*10**-11
    return (4*(pi**2)*(r**3))/(G*((T*60*60)**2))

def main():
    r=float(input("Skriv avståndet mellan satelliten och planeten i m:"))
    T=float(input("Skriv satellitens omloppstid i timmar: "))

    print("Massa av planeten blir: ", Planet_massa(r, T), "kg.")
    
main()