def get_data (filnamn):
    txt=open(filnamn, "r", encoding="utf8")
    content=txt.read()
    content_list=content.split()
    txt.close()
    
    return(content_list)

def differensen (text_list):
    dif=list(set(text_list)-set(get_data("vanligaord.txt")))
    
    return(dif)

def clean (text_list):
    
    
    for i in range (0, len(text_list)):

        text_list[i]=text_list[i].replace(",","")
        text_list[i]=text_list[i].replace(".","")
        text_list[i]=text_list[i].replace(":","")
        text_list[i]=text_list[i].replace("-","")
        text_list[i]=text_list[i].replace("/","")
        text_list[i]=text_list[i].replace("”","")
        text_list[i]=text_list[i].replace("–","")
       
    for n in range (len(text_list)):
        text_list[n]=text_list[n].lower()
        
    return (text_list)
 
def clean_digits (text_list):
    text_clean=[]
    for i in range (0, len(text_list)):
        if text_list[i].isdigit()==False:
            text_clean.append(text_list[i])
            
    return text_clean

def main():

    text_list=get_data(input("Vilken fil vill du läsa in?: "))
    
    text_list_clean= clean_digits(clean(text_list))
   
    print("Texten innehåller", len(text_list), "ord.") #numbers included
    print("Funnit", len(differensen(text_list_clean)), "ovanliga ord.")
    print(*differensen(text_list_clean), sep = "\n")

main()