# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:49:36 2022

@author: Lia Trapanese
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

countries.close()

#Mappo le regioni ad un codice unico per generare geoid



def codificaRegione(filename):
    
    regioncod= dict()
    
    with open(r'C:/Users/Utente/Desktop/Università/Pisa/Primo semestre - Secondo anno/Laboratory of datat science/PROGETTO/TRACCIA/answerdatasetnew/'+ filename , mode='r') as file:         
        skip1=True
        value= 1
        
        for line in file.readlines():
            
            row2= line.split(',')  
            if skip1:        
               skip1 = False
               continue
            else:  
                if row2[len(row2)-2] not in regioncod.keys():
                    regioncod[row2[len(row2)-2]] = value
            value += 1           
               
    return regioncod  



             
                
            

with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdatasetnew\answerdatacorrect.csv', mode='r') as file:
    with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\Geography.csv', mode='w') as geofile:
        
        countinserted= set()                                           #evito i duplicati di country_code
        skip2=True
        
        regcodifica= codificaRegione('answerdatacorrect.csv')
        geofile.write('geoid'+','+'region'+','+'country_name'+','+'continent'+'\n')
        
        for line in file.readlines():
            
            row= line.split(',')  
            if skip2:        
                skip2 = False
                continue
            else:  
            
                ccode = row[len(row)-1].strip().lower().replace('\n','')
                regid =  row[len(row)-3]
                reg= row[len(row)-2]
                
                if (regid + str(regcodifica[reg]) + ccode) in countinserted:                    #concatenazione di country_code e region per discriminare la riga
                    continue
                else:
                    countinserted.add(regid + str(regcodifica[reg]) + ccode)
                    geofile.write( (regid + str(regcodifica[reg]) + ccode) + ',' + reg + ',' + countriesdic[ccode][1] + ',' + countriesdic[ccode][0] + '\n')
                    
                
            

