# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:49:36 2022

@author: Lia Trapanese
"""
from utilities import *              
           
countries = open(r'C:/Users/Utente/Desktop/Università/Pisa/Primo semestre - Secondo anno/Laboratory of datat science/PROGETTO/codici finiti/WorldRegionsContinentsCountries.csv', "r")
countriesdic= dict()

for line in countries.readlines()[1:]:
    row= line.split(',')  
   
    countcode= row[2].strip().lower()
    if countcode not in countriesdic.keys():
        countriesdic[countcode] = []                       #popolo il dizionario che ha come key il countrycode e come valore una lista vuota
        countriesdic[countcode].append(row[4])             #aggiungo nella lista il continente
        countriesdic[countcode].append(row[1])           #aggiungo il country_name

countriesdic['uk']= ['Europe', 'United Kingdom']

countries.close()

            
            

with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdatasetnew\answerdatacorrect.csv', mode='r') as file:
    with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\Geography.csv', mode='w') as geofile:
        
        countinserted= set()                                           #evito i duplicati di country_code
        
        
        regcodifica= codificaRegione('answerdatacorrect.csv')
        geofile.write('geoid'+','+'region'+','+'country_name'+','+'continent'+'\n')
        
        for line in file.readlines()[1:]:
            
            row= line.split(',')  
              
            ccode = row[len(row)-1].strip().lower().replace('\n','')
            regid =  row[len(row)-3]
            reg= row[len(row)-2]
            
            if (regid + str(regcodifica[reg]) + ccode) in countinserted:                    #concatenazione di country_code e region per discriminare la riga
                continue
            else:
                countinserted.add(regid + str(regcodifica[reg]) + ccode)
                geofile.write( (regid + str(regcodifica[reg]) + ccode) + ',' + reg + ',' + countriesdic[ccode][1] + ',' + countriesdic[ccode][0] + '\n')
                
            
        

