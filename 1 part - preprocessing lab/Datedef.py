"""
Created on Tue Oct 18 11:54:21 2022
@author: Lia Trapanese
    
split answer_full.csv
create Date.csv

"""
from utilities import *


with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdatasetnew\answerdatacorrect.csv', mode='r') as file:
    
        
    header= ['dateid', 'date', 'day','month','year','quarter']
    
    dateid= []
    date = []
    day = []
    month = []
    year = []
    quarter = []
    
    no_duplicates = set()                                      #avoid duplicates. We use a list to mantain the order
             

    for line in file.readlines()[1:]: 
        row= line.split(',')  
        
        for col in range(len(row)):                        
            if col == 6 or col == 8:    
                if row[col] not in no_duplicates:
                    no_duplicates.add(row[col])
                    dateid.append(row[col][:10].replace('-', ''))
                    date.append(row[col][:10])
                    year.append(row[col][:4])
                    moth = row[col][5:7].lstrip('0') 
                    month.append(moth)   
                    quarter.append(quarter_generator(moth))
                    day.append(row[col][8:10])
        



with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\Date.csv', mode='w') as datefile:        
    
    for j in range(len(header)):
        if j == len(header)-1:
            datefile.write(str(header[j])+'\n')
        else:
            datefile.write(str(header[j])+',')
        
    for dateid, date, d, m, y, q in zip(dateid,date,day,month,year,quarter):
        datefile.write(str(dateid) +','+date +',' + d+','+m+','+y+','+q+'\n')
            



                    
                    
   
