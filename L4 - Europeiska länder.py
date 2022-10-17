class eu:
    def __init__(self, namn, befolkning, yta):
        self.namn = namn
        self.befolkning = int(befolkning)
        self.yta = float(yta)
        self.täthet = self.befolkning_täthet ()
        
    def __str__(self):
        return f"{self.namn} {self.befolkning}  {self.yta}  {round(self.täthet, 1)}"
    
    def befolkning_täthet (self):
        return (self.befolkning/self.yta)

def inläsning():
    fil = open("europa.txt", "r",encoding="utf-8")
    li = list()
    rad = fil.readline()
    rad = rad.rstrip("\t")
    rad = rad.rstrip("\n")
    while rad != "":
        raddelar = rad.split(",")
        li.append(raddelar)
        rad = fil.readline()
        rad = rad.rstrip("\t")
        rad = rad.rstrip("\n")
    fil.close()
    return li

def main():
    
    li = inläsning()

    länderna = list()
    for i in range(len(li)):
        länderna.append(eu(li[i][0], li[i][2], li[i][1]))

  
    länderna.sort(key = lambda eu: eu.täthet)
    länderna.reverse()

    for i in range (len(li)):
        print(länderna[i])

main()
