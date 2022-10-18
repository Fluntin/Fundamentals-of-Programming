import os

class Aminosyror:
    def __init__(self, kod, namn, grupp, molekylvikt):
        self.kod=kod
        self.namn=namn
        self.grupp=grupp
        self.molekylvikt=float(molekylvikt)
        
    def __str__(self):
        return f"{self.kod} {self.namn}  {self.grupp}  {self.molekylvikt}"
    
def get_data ():
    print('\n')
    print("Getting data -> reading aminoacids...")
    txt=open("aminosyror.txt", "r", encoding="utf8")
    content=txt.read()
    content_list=content.split()
    txt.close()
    print("...done.")
    print('\n')

    return(content_list)

def create_aminosyror (text):
    aminosyror=[]
    for i in range (0, len(text), 4):
        aminosyror.append(Aminosyror(text[i],text[i+1],text[i+2],text[i+3],))
    
    return(aminosyror)

def show_menu ():
    
    print("1 -> Print table of aminoacids sorted by code")
    print("2 -> Print table of aminoacids sorted by name")
    print("3 -> Print table of aminoacids sorted by group")
    print("4 -> Print table of aminoacids sorted by mm")
    print("5 -> End program ")
    print('\n')
    
def sort_aminosyror (val, aminosyror):
    
    if val==1:
        switch="on"
        aminosyror.sort(key = lambda Aminosyror: Aminosyror.kod)
        os.system('cls')
        print("Amino acids sorted by code.")
        print('\n')
                
    elif val==2:
        switch="on"
        aminosyror.sort(key = lambda Aminosyror: Aminosyror.namn)
        os.system('cls')
        print("Amino acids sorted by name.")
        print('\n')
                
    elif val==3:
        switch="on"
        aminosyror.sort(key = lambda Aminosyror: Aminosyror.grupp)
        os.system('cls')
        print("Amino acids sorted by group.")
        print('\n')
                
    elif val==4:
        switch="on"
        aminosyror.sort(key = lambda Aminosyror: Aminosyror.molekylvikt)
        os.system('cls')
        print("Amino acids sorted by molecular weight.")
        print('\n')
          
    elif val==5:
        switch="off"
        os.system('cls')
    else:
        switch="unspecified"
        os.system('cls')
        
    return ({"sorted_list":aminosyror, "switch":switch})
    
def main ():
    
    aminosyror=create_aminosyror(get_data ())
         
    while True:
        
        show_menu()
        
        results=sort_aminosyror(int(input("Val av alternativet: ")), aminosyror)
        
        if results["switch"]=="on":
            for i in range (len(results["sorted_list"])):
                print(results["sorted_list"][i])
            print('\n')
                
        elif results["switch"]=="off":
            print('\n')
            print("Välkomolekylvikten åter!")
            print('\n')
            break
        
        elif results["switch"]=="unspecified":
            print('\n')
            print("Välj ett giltigt alternativ.")
            print('\n')
            
main()