"""
Created on Tue Oct 18 11:54:21 2022
@author: Lia Trapanese, Giovanni D'Orsi
    
split answer_full.csv
create Date.csv

"""
from funzioni import *

with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdatasetnew\answerdatacorrect.csv', mode='r') as file:
           
    header= ['dateid', 'date', 'day','month','year','quarter']
    
    dateid= []
    date = []
    day = []
    month = []
    year = []
    quarter = []
    
    uniques = set()                               
   
    for line in file.readlines()[1:]:                                        # leggo saltando l'header
        row= line.split(',')  
        

        for col in range(len(row)):                        
            if col == 6 or col == 8:                                         # colonna 6 = DateofBirth, colonna 8 = DateAnswered
                if row[col][:10].replace('-', '') not in uniques:            # prendo solo la data togliendo i trattini e verifico che questo sia stato già processato
                    
                    uniques.add(row[col][:10].replace('-', ''))
                    dateid.append(row[col][:10].replace('-', ''))
                    date.append(row[col][:10])
                    year.append(row[col][:4])
                    moth = row[col][5:7].lstrip('0')                         #es. formatto il mese 01 in 1
                    month.append(moth)   
                    quarter.append(quarter_generator(int(moth)))
                    day.append(row[col][8:10])
                        



with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\Date.csv', mode='w') as datefile:        
    
    for j in range(len(header)):                                             # scrivo l'header 
        if j == len(header)-1:
            datefile.write(str(header[j])+'\n')
        else:
            datefile.write(str(header[j])+',')
        
    for dateid, date, d, m, y, q in zip( dateid, date, day, month, year, quarter):      # scrivo righe
        datefile.write(str(dateid) +','+date +',' + d+','+m+','+y+','+q+'\n')
            



                    
                    
   
