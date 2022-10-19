# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:49:36 2022

@author: Lia Trapanese, Giovanni Battista D'Orsi
"""
              
           
countries = open(r'C:\Users\Utente\Desktop\WorldRegionsContinentsCountries.csv', "r")
skip=True
countriesdic= dict()

for line in countries.readlines():
    row= line.split(',')  
    if skip:        
       skip = False
       continue
    else:
        countcode= row[2].strip().lower()
        if countcode not in countriesdic.keys():
            countriesdic[countcode] = []                       #popolo il dizionario che ha come key il countrycode e come valore una lista vuota
            countriesdic[countcode].append(row[4])             #aggiungo nella lista il continente
            countriesdic[countcode].append(row[1])           #aggiungo il country_name

countriesdic['uk']= ['Europe', 'United Kingdom']

 
countinserted= set()                                           #evito i duplicati di country_code




with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdataset\answers_full.csv', mode='r') as file:
    with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\Geography.csv', mode='w') as geofile:
        count=0
        skip1=True
        
        geofile.write('geoid'+','+'region'+','+'country_name'+','+'continent'+'\n')
        
        for line in file.readlines():
            
            row= line.split(',')  
            if skip1:        
               skip1 = False
               continue
            else:  
           
                ccode = row[len(row)-1].strip().lower().replace('\n','')
                reg =  row[len(row)-2].replace('\n','')
                
                if (ccode+reg) in countinserted:                    #concatenazione di country_code e region per discriminare la riga
                    continue
                else:
                    countinserted.add(str(ccode+reg))
                    geofile.write( ccode+str(count) + ',' + reg + ',' + countriesdic[ccode][1] + ',' + countriesdic[ccode][0] + '\n')
                    count+=1
                
           