def slutvärde(räntesats,belopp,år):
    return ((räntesats/100)+1)**år*belopp

def main():
    
    belopp = float(input("Ange beloppet i kr "))
    räntesats = float(input( "Ange räntesatsen i procent "))
    år = float(input("Ange antal år som beloppet ska förräntas "))
    värde = round(slutvärde(räntesats,belopp,år))

    print("Slutvärdet är", värde, "kr")
    
main()
