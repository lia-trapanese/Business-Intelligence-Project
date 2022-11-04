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
        
        addDate(6)
        addDate(8)

        



with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\Date.csv', mode='w') as datefile:        
    
    for j in range(len(header)):
        if j == len(header)-1:
            datefile.write(str(header[j])+'\n')
        else:
            datefile.write(str(header[j])+',')
        
    for dateid, date, d, m, y, q in zip(dateid,date,day,month,year,quarter):
        datefile.write(str(dateid) +','+date +',' + d+','+m+','+y+','+q+'\n')
            



                    
                    
   
