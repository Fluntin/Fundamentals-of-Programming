import os
import yfinance as yf
import datetime as dt
import tkinter as tk
import pandas_datareader as panda

class Stock:
    def __init__(self, company_name, debt_to_equity, pe, ps, history, omx):
        #An object of type Stock contains all the info that describes a company, both technical and fundamental.
        #Note: history -> {date:price}
        #Note: omx -> {date:price}
        
        self.company_name=company_name
        self.debt_to_equity=debt_to_equity
        self.pe=pe
        self.ps=ps
        self.history=history
        self.omx=omx
        self.course_development=self.calculate_course_development()
        self.course_highest=self.calculate_course_highest()
        self.course_lowest=self.calculate_course_lowest()
        self.betha=self.calculate_betha()
    
    def calculate_course_development(self):
        #Calculate course development for last 30 days.
        #Input: self
        #Output: course development for last 30 days -> float

        value=list()
        for key in self.history:
            value.append(float(self.history[key]))
            
        course_development=((value[-1]-value[0])/value[0])*100
            
        return(round(course_development,2))
    
    def calculate_course_lowest(self):
        #Calculate lowest value for last 30 days.
         #Input: self
         #Output: lowest value for last 30 days -> float
        value=list()
        for key in self.history:
            value.append(float(self.history[key]))
        
        return(min(value))
    
    def calculate_course_highest(self):
        #Calculate highest value for last 30 days.
         #Input: self
         #Output: highest value for last 30 days -> float
        value=list()
        for key in self.history:
            value.append(float(self.history[key]))
        
        return(max(value))
    
    def calculate_betha(self):
        #Calculate beta.
         #Input: self
         #Output: beta value-> float
        value=list()
        for key in self.history:
            value.append(float(self.history[key]))
        
        avkastning_aktie=value[-1]/value[0]
            
        omx=list()
        for key in self.omx:
            omx.append(float(self.omx[key]))
        
        avkastning_omx=omx[-1]/omx[0]
    
        betha=avkastning_aktie/avkastning_omx
        
        return(round(betha,2))
          
    def __repr__(self):
        return f"{self.company_name} {self.debt_to_equity}  {self.pe}  {self.ps}"

def check_day(date):
#Check if a date is a weekday

#Input: date -> datetime object
#Output: if date is weekday True
#        if date is weekend False

    weekno = date.weekday()
    weekday=bool
    
    if weekno < 5:
        weekday=True
        
    else:  
        weekday=False
        
    return (weekday)

       
def get_history_data_offline (company_list):
    #Get data from : kurser.txt -> (Format: datum, böorskurs)
    #Store data as a dictionary
    
    #Input:company_list -> [Company name1,Company name2,Company name3...]
    #Output: dictionary-> {Company name:{Date:Value}}

    txt=open("kurser.txt", "r", encoding="utf8")
    content=txt.read()
    content_list=content.split()
    txt.close()

    #Go through each element in a list and find cotoffpoints
    #Cutoff point = index position of a company name
    #Create a list of positions for cutoff points.
    cut_points=list()
    for i in range(0,len(content_list)):
        if content_list[i] in company_list:
            cut_points.append(i)
    cut_points.append(len(content_list))
    
    #Since the text file has dates in the format yy-mm-dd and I want yyyy-mm-dd -> to use datetime
    list_of_dates=list()
    for j in range (cut_points[0]+1, cut_points[1],2):
        list_of_dates.append("20"+content_list[j])

    #Since we and last 30 days we need a start and an end date.
    end_date=list_of_dates[-1]
    end_date = dt.datetime.strptime(end_date, '%Y-%m-%d').date()
    start_date = end_date - dt.timedelta(days=30)
    
    #Stock exchange is only active during work days so we create a list of dates in range start_date to end_dateout to get.
    dates_to_get=list()
    for i in range (0, 31):
        date=start_date+dt.timedelta(days=i)
        if check_day(date):
            dates_to_get.append(date.strftime('%Y-%m-%d')[2:])
            
    #Use cutoff point and a list of dates to get -> Create a dictionary {Date:Value}   
    #For each company create a separate dictionary -> {Company:{Date:Value}}     
    data=dict()
    for i in range (0,len(cut_points)-1):
        index=dict()
        for j in range (cut_points[i]+1, cut_points[i+1],2):
            if content_list[j] in dates_to_get:
                index[content_list[j]]=content_list[j+1]
        data[content_list[cut_points[i]]]=index
    
    return(data)

def get_history_data_online (companies):
    #Calculate start_date and end_date
    #Use Panda to get data for a specific ticker
    #If the date in the range start_date to end_date is a workday store a date and a closing price in a dictionary -> {Date:Value}

    #Input: companies -> {Company name:Ticker}
    #Output: dictionary-> {Company name:{Date:Value}}
    
    start_date = dt.datetime.now().date() - dt.timedelta(days=31)
    end_date = dt.datetime.now().date()
    
    history_data=dict()
    for key in companies:
        raw_data = panda.DataReader(companies[key],'yahoo',str(start_date),str(end_date))

        index=dict()
        for i in range (0, 31):
            date=start_date+dt.timedelta(days=i)
        
            if check_day(date):
                börskurs=raw_data.loc[date.strftime('%Y-%m-%d'),'Close']
                index[str(date)]=round(börskurs,2)
                        
        history_data[key]=index
    
    return (history_data) 

def get_fundamentals_data_offline (company_list):
    #Get data from : fundamenta.txt -> (Format: Company name, DebtToEquity, Price to Earnings ratio, Price to Sales ratio)
    #Store data as a dictionary
    
    #Input:company_list -> [Company name1,Company name2,Company name3...]
    #Output: dictionary-> {Company name:[DebtToEquity, Price to Earnings ratio, Price to Sales ratio]}
    
    txt=open("fundamenta.txt", "r", encoding="utf8")
    content=txt.read()
    content_list=content.split()
    txt.close()

    #Go through each element in a list and find cotoffpoints
    #Cutoff point = index position of a company name
    #Create a list of positions for cutoff points.
    cut_points=list()
    for i in range(0,len(content_list)):
        if content_list[i] in company_list:
            cut_points.append(i)
    cut_points.append(len(content_list))
    
    
    data=dict()
    for i in range (0,len(cut_points)-1):
        data_list=list()
        
        for j in range (cut_points[i]+1, cut_points[i+1]):
            data_list.append(content_list[j])
        data[content_list[cut_points[i]]]=data_list
    
    return(data)
    
def get_fundamentals_data_online (companies):
    #Use Yahoo finance to get fundamental data
    
    #Input: companies-> {Company name:Ticker}
    #Output: dictionary-> {Company name:[DebtToEquity, Price to Earnings ratio, Price to Sales ratio]}

    
    fundamentals_data=dict()
    
    for key in companies:
        data_list=list()
        company = yf.Ticker(companies[key]).info
        
    #Debt-To-Equity
        try:
            data_list.append(company["debtToEquity"])
            
        except KeyError:
            data_list.append("None")
            
    #Price-to-Earnings
        try:
            data_list.append(company["trailingPE"])
            
        except KeyError:
            data_list.append("None")
    
    #Price-to-Sales
        try:
            data_list.append(company["priceToSalesTrailing12Months"])
            
        except KeyError:
            data_list.append("None")
    
        
        fundamentals_data[key]=data_list
    
    return (fundamentals_data)

def get_omx_offline():
    #Get data from : generalindex.txt -> (Format: Date, Value)
    #Store data as a dictionary 
    
    #Input:None
    #Output: dictionary-> {Date:Value}
    
    txt=open("generalindex.txt", "r", encoding="utf8")
    content=txt.read()
    content_list=content.split()
    txt.close()

    data=dict()
    for i in range (3,len(content_list),2):
        data[content_list[i]]=content_list[i+1]
    
    return(data)

def get_omx_online():
    #Calculate start_date and end_date
    #Use Panda to get data for a specific ticker
    #If the date in the range start_date to end_date is a workday store a date and a closing price in a dictionary -> {Date:Value}
    
    #Input: None
    #Output: dictionary-> {Date:Value}
    
    start_date = dt.datetime.now().date() - dt.timedelta(days=30)
    end_date = dt.datetime.now().date()
    
    raw_data = panda.DataReader('^OMXSPI','yahoo',str(start_date),str(end_date))

    index=dict()
    for i in range (0, 30):
        date=start_date+dt.timedelta(days=i)
        
        if check_day(date):
            date.strftime('%Y-%m-%d')
                
            high=raw_data.loc[str(date),'High']
            low=raw_data.loc[str(date),'Low']
            börskurs=round((high+low)/2,3)
            
            index[str(date)]=börskurs
                        
    return(index)
    

def create_list_object (fundamentals, history, omx):
    #Create a list of objects where the object type is Stock.
    
    #Input : 1. fundamentals = dictionary-> {Company name:[DebtToEquity, Price to Earnings ratio, Price to Sales ratio]}
    #        2. history = dictionary-> {Company name:{Date:Value}}
    #        3. omx = dictionary-> {Date:Value}
    #Output: list -> [Stock1,Stock2,Stock3...]
    stock_list=[]
    for key in fundamentals:
        stock_list.append(Stock(key,fundamentals[key][0],fundamentals[key][1],fundamentals[key][2],history[key], omx))
    
    return(stock_list)


def choose_offline_vs_online ():
    #Allows the user to choose whether to get data online or offline (offline=get it from txt-files)
    
    #Input:None
    #Output: list -> [Stock1,Stock2,Stock3...]
    
    while True:
        try:
            print("Would you like to get data online?")
            print('\n')
    
            val=input("(y/n): ")
    
            if val=='y':
                switch=True
                break
            elif val=='n':
                switch=False
                break
            
        except ValueError:
            os.system('cls')
            print('Try again')
        
    if switch:
        companies={'Ericsson':'ERIC',
                'Electrolux':'ELUX-B.ST',
               'AstraZeneca':'AZN',
               'Moderna':'MRNA'}
        
        history_data=get_history_data_online (companies)
        fundamentals_data=get_fundamentals_data_online(companies)
        omx=get_omx_online()
        
        stock_list=create_list_object(fundamentals_data, history_data,omx)
        
    else:
        company_list=['Ericsson','Electrolux','AstraZeneca']
        
        history_data=get_history_data_offline(company_list)
        fundamentals_data=get_fundamentals_data_offline(company_list)
        omx=get_omx_offline()

        stock_list=create_list_object(fundamentals_data, history_data,omx)
            
    return(stock_list)


def show_main_menu ():
    #Prints out the main menu
    
    #Input:None
    #Output:None
    
    print("1 -> Fundamental analysis")
    print("2 -> Technical analysis")
    print("3 -> Ranking according to beta value")
    print("4 -> Exit")
    print('\n')
    print("Choose: ")

def show_fundamental_menu (stock_list):
    #Displays names of all companies in stock_list.
    #Allows the user to select a specific company.
    #Writes out fundamental data for the selected company.
    
    #Input: list -> [Stock1,Stock2,Stock3...]
    #Output: None
    
    while True:
        print('') 
        print('-----Fundamental menu-----')
        
        try:
            for i in range(0,len(stock_list)):
                print(i+1,'->',stock_list[i].company_name)
            print(len(stock_list)+1, '-> Go to Main menu')
        
            print('')  
            val = int(input("What stock would you like to get the fundamental analysis for?"))
            print('')
        
            if val < len(stock_list)+1:
                print('')  
                print("-----Fundamental analys for ",stock_list[val-1].company_name,"-----" )
                print("Company's Debt to Equity is:", stock_list[val-1].debt_to_equity)
                print("Company's Price to Earnings ratio:", stock_list[val-1].pe)
                print("Company's Price to Sales ratio:",stock_list[val-1].ps)
            elif val==len(stock_list)+1:
                break
            else:
                print('Try again')
                
        except ValueError:
            os.system('cls')
            
        print('')
        print('')

def show_teknisk_menu (stock_list):
    #Displays names of all companies in stock_list.
    #Allows the user to select a specific company.
    #Writes out Technical analysis data for the selected company.
    
    #Input: list -> [Stock1,Stock2,Stock3...]
    #Output: None
    
    while True:
        
        print('') 
        print('-----Technical analysis-----')
        
        try:
            for i in range(0,len(stock_list)):
                print(i+1,'->',stock_list[i].company_name)
            print(len(stock_list)+1, '-> Go to Main menu')
        
            print('')   
            val = int(input("What stock would you like to get the technical analysis for?"))
            print('')
    
            if val <len(stock_list)+1:
                print('')
                print("-----Technical analysis for ",stock_list[val-1].company_name,"-----" )
                print("Course development for last 30 days: ", stock_list[val-1].course_development)
                print("Highest value for last 30 days: ", stock_list[val-1].course_highest)
                print("Lowest value for last 30 days: ",stock_list[val-1].course_lowest)
                print("Beta value: ", stock_list[val-1].betha)
                
            elif val==len(stock_list)+1:
                break
            
            else:
                print('Try again')
                
        except ValueError:
            os.system('cls')    
            
    print('')
    print('')

def sort_betha (stock_list):
    #Sorts companies from stock_list according to the beta value
    
    #Input: list -> [Stock1,Stock2,Stock3...]
    #Output: None
    
    print('')
    print('---Ranking according to Beta value---') 
    betha=dict()
    
    for company in stock_list:
        betha[company.company_name]=round(float(company.betha),3)
    
    sorted_betha = sorted(betha.items(), key=lambda x: x[1], reverse=True)
    
    for i in range(len(sorted_betha)):
        print(i+1,"->", *sorted_betha[i])

def want_gui():
    #Allows the user to choose to use GUI or Terminal
    
    #Input:None
    #Output: switch -> boolean
    
    os.system('cls') 
    while True:
        try:
            print("Would you like to use GUI?")
            print('\n')
    
            val=input("(y/n): ")
    
            if val=='y':
                switch=True
                break
            elif val=='n':
                switch=False
                break
            
        except ValueError:
            os.system('cls')
            print('Try again')
            
    os.system('cls')     
    return(switch)

def gui_menu(stock_list):
    # Dropdown menu options
    companies=list()
    for company in stock_list:
        companies.append(company.company_name)
        
    my_w = tk.Tk()
    my_w.geometry("750x500")  # Size of the window 
    my_w.title("Aktieköp")  # Adding a title

    options = tk.StringVar(my_w)
    options.set("Defult") # default value

    l1 = tk.Label(my_w,  text='Select One', width=10 )  
    l1.grid(row=2,column=1) 

    om1 =tk.OptionMenu(my_w, options, *companies)
    om1.grid(row=2,column=2) 

    b1 = tk.Button(my_w,  text='Show Technical', command=lambda: show_technical() )  
    b1.grid(row=2,column=3) 
    
    b2 = tk.Button(my_w,  text='Show Fundamental', command=lambda: show_fundamental() )  
    b2.grid(row=3,column=3) 
    
    b3 = tk.Button(my_w,  text='Show Betha', command=lambda: show_betha() )  
    b3.grid(row=4,column=3) 

    str_out=tk.StringVar(my_w)
    str_out.set("Output")

    l2 = tk.Label(my_w,  textvariable=str_out, width=10 )  
    l2.grid(row=2,column=4) 
    
    def show_betha ():
        betha=dict()
    
        for company in stock_list:
            betha[company.company_name]=round(float(company.betha),3)
    
        sorted_betha = sorted(betha.items(), key=lambda x: x[1], reverse=True)
        
        txt="----- Betha Ranking -----"
        betha1= tk.Label(my_w, text=txt)
        betha1.grid(row=16,column=4) 
        
        txt=str(sorted_betha[0] [0])+str(sorted_betha[0] [1])
        betha1= tk.Label(my_w, text=txt)
        betha1.grid(row=17,column=4) 
        
        txt=str(sorted_betha[1] [0])+str(sorted_betha[1] [1])
        betha2= tk.Label(my_w, text=txt)
        betha2.grid(row=18,column=4) 
        
        txt=str(sorted_betha[2] [0])+str(sorted_betha[2] [1])
        betha3= tk.Label(my_w, text=txt)
        betha3.grid(row=19,column=4) 
        
        try:
            txt=str(sorted_betha[3] [0])+ str(sorted_betha[3] [1])
            betha4= tk.Label(my_w, text=txt)
            betha4.grid(row=20,column=4)
             
        except IndexError:
            pass
    
    def show_fundamental():
        val=options.get()
                
        for company in stock_list:
            if val==company.company_name:
                txt=str("-------- Fundamental Analys for: " + str(company.company_name) + "-------- ")
                course_development_label = tk.Label(my_w, text=txt)
                course_development_label.grid(row=4,column=4) 
                
                txt=str("   Company's Debt to Equity is: " + str(company.debt_to_equity) + "   ")
                debt_to_equity_label = tk.Label(my_w, text=txt)
                debt_to_equity_label.grid(row=5,column=4) 
                
                txt=str("   Company's Price to Earnings ratio: " + str(company.pe) + "   ")
                pe_label=tk.Label(my_w, text=txt)
                pe_label.grid(row=6,column=4) 
                
                txt=str("   Company's Price to Sales ratio: " + str(company.ps) + "   ")
                ps_label=tk.Label(my_w, text=txt)
                ps_label.grid(row=7,column=4) 

    def show_technical():
        val=options.get()

        for company in stock_list:
            if val==company.company_name:
                
                txt=str("-------- Technical Analysis for:  " + str(company.company_name) + "-------- ")
                course_development_label = tk.Label(my_w, text=txt)
                course_development_label.grid(row=10,column=4) 
                
                txt=str("   Course development for last 30 days: " + str(company.course_development) + "   ")
                course_development_label = tk.Label(my_w, text=txt)
                course_development_label.grid(row=11,column=4) 
                
                txt=str("   Highest value for last 30 days: " + str(company.course_highest) + "   ")
                högsta_label=tk.Label(my_w, text=txt)
                högsta_label.grid(row=12,column=4) 
                
                txt=str("   Lowest value for last 30 days: " + str(company.course_lowest) + "   ")
                lägsta_label=tk.Label(my_w, text=txt)
                lägsta_label.grid(row=13,column=4) 
                
                txt=str("   Beta value: " + str(company.betha) + "   ")
                betha_label=tk.Label(my_w, text=txt)
                betha_label.grid(row=14,column=4) 
                
        
    my_w.mainloop()
                     
def main():
       
    stock_list= choose_offline_vs_online()
    gui=want_gui()
    
    if gui==False:

        while True:
            print('') 
            print('-----Main menu-----')
        
            try:
                show_main_menu()
                val=int(input())
        
                if val==1:
                    os.system('cls')
                    show_fundamental_menu(stock_list) 
           
                elif val==2:
                    os.system('cls')
                    show_teknisk_menu(stock_list)
            
                elif val==3:
                    os.system('cls')
                    sort_betha(stock_list)
        
                elif val==4:
                    os.system('cls')
                    print('Thank you for using the program and have a nice day.')
                    break
        
                else:
                    os.system('cls')
                
            except ValueError:
                os.system('cls')
                
    else:
        gui_menu(stock_list)
            
os.system('cls')   
main()
