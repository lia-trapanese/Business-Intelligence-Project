# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:49:36 2022

@author: Lia Trapanese, Giovanni Battista D'Orsi
"""

'it': [Italia, Europa]


                
           
countries = open(r'C:\Users\Utente\Desktop\WorldRegionsContinentsCountries.csv', "r")
skip=True
countriesdic= dict()

for line in countries.readlines():
    row= line.split(',')  
    if skip:        
       skip = False
       continue
    else:
        countcode= row[2].lower()
        if row[2] not in countriesdic.keys():
            countriesdic[countcode] = []                       #popolo il dizionario che ha come key il countrycode e come valore una lista vuota
            countriesdic[countcode].append(row[4])             #aggiungo nella lista il continente
            countriesdic[countcode].append([row[1]])           #aggiungo il country_name
        
 
countinserted= set()                                           #evito i duplicati di country_code

geography= ['goeid', 'region', 'country_name', 'continent']


with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdataset\answers_full.csv', mode='r') as file:
    with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\Geography.csv', mode='w') as geofile:
        
        geofile.write('geoid',  \n')
        for line in countries.readlines():
            row= line.split(',')  
            if skip:        
               skip = False
               continue
            else:  
                if row[15] is in countinserted:                    #prendo la colonna country_code in answer_full
                    continue
                else:
                    countinserted.add(row[15])
                    geofile.write(row[2]+','+....+','+coutriesdic[row[2]][0]+','+)
                
                
        
        
    countriesdic[]