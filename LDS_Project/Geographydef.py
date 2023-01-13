# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:49:36 2022

@author: Lia Trapanese
"""
from funzioni import *              


#APRO IL FILE DI DATA INTEGRATION CHE CONTIENE I CONTINENTI DA ASSOCIARE AD OGNI COUNTRY. CREO IL DIZIONARIO "countriesdic" CHE HA COME CHIAVE 
#IL COUNTRY CODE E COME VALORE UNA LISTA CON DUE ELEMENTI (IL CONTINENTE E LA COUNTRY).            
countries = open(r'C:/Users/Utente/Desktop/Università/Pisa/Primo semestre - Secondo anno/Laboratory of datat science/PROGETTO/codici finiti/WorldRegionsContinentsCountries.csv', "r")
countriesdic= dict()

for line in countries.readlines()[1:]:
    row= line.split(',')  
   
    countcode= row[2].strip().lower()                     
    if countcode not in countriesdic.keys():
        countriesdic[countcode] = []                       
        countriesdic[countcode].append(row[4])             # aggiungo nella lista il continente
        countriesdic[countcode].append(row[1])             # aggiungo il country_name

countriesdic['uk']= ['Europe', 'United Kingdom']           # modifica manuale

countries.close()

            
            

with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdatasetnew\answerdatacorrect.csv', mode='r') as file:
    with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\Geography.csv', mode='w') as geofile:
        
        countinserted= set()                                           #evito i duplicati di country_code
        
        
        regcodifica= codificaRegione('answerdatacorrect.csv')
        geofile.write('geoid'+','+'region'+','+'country_name'+','+'continent'+'\n')
        
        for line in file.readlines()[1:]:
            
            row= line.split(',')  
              
            ccode = row[len(row)-1].strip().lower().replace('\n','')              # estraggo il codice della country per mapparlo con il dizionario countriesdic
            regid =  row[len(row)-3]
            reg= row[len(row)-2]                     #region 
            
            if (regid + str(regcodifica[reg]) + ccode) in countinserted:          # concatenazione di country_code e region per discriminare la riga
                continue
            else:
                countinserted.add(regid + str(regcodifica[reg]) + ccode)
                geofile.write( (regid + str(regcodifica[reg]) + ccode) + ',' + reg + ',' + countriesdic[ccode][1] + ',' + countriesdic[ccode][0] + '\n')
                
            
        

