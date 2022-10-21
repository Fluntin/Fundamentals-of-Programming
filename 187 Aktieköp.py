# -*- coding: utf-8 -*-

"""
Created on Wed Oct  5 12:45:41 2022
@author: villi
"""
import yfinance as yf
import pandas_datareader as  panda
import datetime as dt
import matplotlib.pyplot as plt
import os

class Aktie:
    def __init__(self, företagsnamn, soliditet, pe, ps, history, omx):
        self.företagsnamn=företagsnamn
        self.soliditet=soliditet
        self.pe=pe
        self.ps=ps
        self.history=history
        self.omx=omx
        self.kursutveckling=self.calculate_kursutveckling()
        self.högsta_kurs=self.calculate_högsta_kurs()
        self.lägsta_kurs=self.calculate_lägsta_kurs()
        self.betha=self.calculate_betha()
    
    def calculate_kursutveckling(self):
        value=list()
        for key in self.history:
            value.append(float(self.history[key]))
            kursutveckling=((value[-1]-value[0])/value[0])*100
            
        return(kursutveckling)
    
    def calculate_lägsta_kurs(self):
        value=list()
        for key in self.history:
            value.append(float(self.history[key]))
        #print(value)
        
        return(min(value))
    
    def calculate_högsta_kurs(self):
        value=list()
        for key in self.history:
            value.append(float(self.history[key]))
        
        return(max(value))
    
    def calculate_betha(self):
        value=list()
        for key in self.history:
            value.append(float(self.history[key]))
        
        avkastning_aktie=value[-1]/value[0]
            
        omx=list()
        for key in self.omx:
            omx.append(float(self.omx[key]))
        
        avkastning_omx=omx[-1]/omx[0]
            
        betha=avkastning_aktie/avkastning_omx
        
        return(betha)
        
         
            
        
        
    def __repr__(self):
        return f"{self.företagsnamn} {self.soliditet}  {self.pe}  {self.ps}"

def check_day(date):
#Input: date
#Output: if date is weekday True
#        if date is weekend False

    weekno = date.weekday()
    weekday=bool
    
    if weekno < 5:
        weekday=True
        
    else:  
        weekday=False
        
    return (weekday)

def graph (history_data):

    names = list(history_data.keys())
    values = list(history_data.values())
    plt.bar(range(len(history_data)), values, tick_label=names)
    plt.show()
      
    stock_list=[]
    for i in fundamentals:
        stock_list.append(Aktie(fundamentals[i][0],fundamentals[i][1],fundamentals[i][2],fundamentals[i][3], get_history_data(fundamentals[i][0]), omx ))
    
    return(stock_list)
    
        
def get_history_data_offline (company_list):
    #Get data from : kurser.txt
    #Format: datum, böorskurs
    #Store data as a dictionary
    #Return: dictionary-> index

    txt=open("kurser.txt", "r", encoding="utf8")
    content=txt.read()
    content_list=content.split()
    txt.close()
    #print(content_list)

    cut_points=list()
    for i in range(0,len(content_list)):
        if content_list[i] in company_list:
            cut_points.append(i)
    cut_points.append(len(content_list))
    #print(cut_points)


        
    data=dict()
    for i in range (0,len(cut_points)-1):
        index=dict()
        #print('i= ',cut_points[i])
        for j in range (cut_points[i]+1, cut_points[i+1],2):
            #print('j= ',j)
            index[content_list[j]]=content_list[j+1]
        data[content_list[cut_points[i]]]=index
    
    return(data)

def get_history_data_online (companies):
    #Store data as a dictionary
    #Return: dictionary-> {name:{datum:value}}
    
    #Get dates for last 30 days
    start_date = dt.datetime.now().date() - dt.timedelta(days=30)
    end_date = dt.datetime.now().date()
    
    
    history_data=dict()
    
    for key in companies:
        raw_data = panda.DataReader(companies[key],'yahoo',str(start_date),str(end_date))

        index=dict()

        for i in range (0, 30):
            date=start_date+dt.timedelta(days=i)
        
            if check_day(date):
                date.strftime('%Y-%m-%d')
                
                high=raw_data.loc[str(date),'High']
                low=raw_data.loc[str(date),'Low']
                börskurs=round((high+low)/2,3)
            
                index[str(date)]=börskurs
                        
        history_data[key]=index
        
    return (history_data) 


def get_fundamentals_data_offline (company_list):
    

    txt=open("fundamenta.txt", "r", encoding="utf8")
    content=txt.read()
    content_list=content.split()
    txt.close()
    #print(content_list)

    cut_points=list()
    for i in range(0,len(content_list)):
        if content_list[i] in company_list:
            cut_points.append(i)
    cut_points.append(len(content_list))
    #print(cut_points)


        
    data=dict()
    for i in range (0,len(cut_points)-1):
        data_list=list()
        #print('i= ',cut_points[i])
        for j in range (cut_points[i]+1, cut_points[i+1]):
            #print('j= ',j)
            data_list.append(content_list[j])
        data[content_list[cut_points[i]]]=data_list
    
    return(data)
    
def get_fundamentals_data_online (companies):
    #Return dict: {name:[soliditet, p/e, p/s]}
    
    #info
    #ticker = yf.Ticker('GOOGL').info
    #print(ticker.keys())
    
    fundamentals_data=dict()
    
    for key in companies:
        data_list=list()
        company = yf.Ticker(companies[key]).info
    
    #Price-to-Sales
        try:
            data_list.append(company["priceToSalesTrailing12Months"])
            
        except KeyError:
            data_list.append("None")
    
    #Price-to-Earnings
        try:
            data_list.append(company["trailingPE"])
            
        except KeyError:
            data_list.append("None")
    
    #Debt-To-Equity
        try:
            data_list.append(company["debtToEquity"])
            
        except KeyError:
            data_list.append("None")
        
        fundamentals_data[key]=data_list
    
    return (fundamentals_data)


def get_omx_offline():
    txt=open("generalindex.txt", "r", encoding="utf8")
    content=txt.read()
    content_list=content.split()
    txt.close()
    #print(content_list)

       
    data=dict()
    for i in range (3,len(content_list),2):
        data[content_list[i]]=content_list[i+1]
    
    return(data)

def get_omx_online():
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
    
    stock_list=[]
    for key in fundamentals:
        stock_list.append(Aktie(key,fundamentals[key][0],fundamentals[key][1],fundamentals[key][2],history[key], omx))
    
    return(stock_list)


def choose_offline_vs_online ():
    while True:
        try:
            print("Hämta data online?")
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
                
        #print(history_data)
        #print(fundamentals_data)
        
        stock_list=create_list_object(fundamentals_data, history_data,omx)
        
    else:
        company_list=['Ericsson','Electrolux','AstraZeneca']
        
        history_data=get_history_data_offline(company_list)
        fundamentals_data=get_fundamentals_data_offline(company_list)
        omx=get_omx_offline()
        
        #print(history_data)
        #print(fundamentals_data)
        
        stock_list=create_list_object(fundamentals_data, history_data,omx)
        

        
    return(stock_list)


def show_main_menu ():
    
    print("1 -> Fundamental analys (Vid långsiktigt aktieinnehav)")
    print("2 -> Teknisk analys (Vid kort aktieinnehav)")
    print("3 -> Rangordning av aktier med avseende på dess betavärde")
    print("4 -> Avsluta")
    print('\n')
    print("Vilket alternativ vill du välja? ")

def show_fundamental_menu (stock_list):
    
    while True:
        print('') 
        print('-----Fundamental menu-----')
        
        try:
    
            for i in range(0,len(stock_list)):
                print(i+1,'->',stock_list[i].företagsnamn)
            print(len(stock_list)+1, '-> Gå till Main menu')
        
            print('')  
            val = int(input("Vilken aktie vill du göra fundamental analys på? "))
            print('')
        
            if val < len(stock_list)+1:
                print('')  
                print("-----Fundamental analys för ",stock_list[val-1].företagsnamn,"-----" )
                print("företagets soliditet är:", stock_list[val-1].soliditet, "%")
                print("företagets p/e-tal är:", stock_list[val-1].pe)
                print("företagets p/s-tal är:",stock_list[val-1].ps)
            elif val==len(stock_list)+1:
                break
            else:
                print('Try again')
                
        except ValueError:
            os.system('cls')
            
        print('')
        print('')

def show_teknisk_menu (stock_list):
    
    while True:
        
        print('') 
        print('-----Teknisk menu-----')
        
        try:
            for i in range(0,len(stock_list)):
                print(i+1,'->',stock_list[i].företagsnamn)
            print(len(stock_list)+1, '-> Gå till Main menu')
        
            print('')   
            val = int(input("Vilken aktie vill du göra teknisk analys på? "))
            print('')
    
            if val <len(stock_list)+1:
                print('')
                print("-----Teknisk analys för ",stock_list[val-1].företagsnamn,"-----" )
                print("kursutveckling(30 senaste dagarna)", stock_list[val-1].kursutveckling, "%")
                print("betavärde", stock_list[val-1].betha)
                print("högsta kurs(30 senaste dagarna): ", stock_list[val-1].högsta_kurs)
                print("lägsta kurs(30 senaste dagarna): ",stock_list[val-1].lägsta_kurs)
                
            elif val==len(stock_list)+1:
                break
            
            else:
                print('Try again')
                
        except ValueError:
            os.system('cls')    
            
    print('')
    print('')

def sort_betha (stock_list):
    
    print('') 
    betha=dict()
    
    for company in stock_list:
        betha[company.företagsnamn]=round(float(company.betha),3)
    
    sorted_betha = sorted(betha.items(), key=lambda x: x[1], reverse=True)
    
    for i in range(len(sorted_betha)):
        print(i+1,"->", *sorted_betha[i])

def whant_gui():
    os.system('cls') 
    while True:
        try:
            print("GUI?")
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
                     
def main():
       
    stock_list= choose_offline_vs_online()
    gui=whant_gui()
    
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
                    print('Tack för att du använder programmet.')
                    break
        
                else:
                    os.system('cls')
                
            except ValueError:
                os.system('cls')
                
    else:
        gui_menu()
            
os.system('cls')   
main()