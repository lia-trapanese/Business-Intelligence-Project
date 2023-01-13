# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:41:08 2022

@author: Lia Trapanese, Giovanni D'Orsi
"""

def quarter_generator(moth):
    
    if  moth >= 1 and moth <= 3:
        return 'Q1'
    elif moth > 3 and moth <= 6:
        return 'Q2'
    elif moth > 6 and moth <= 9:
        return 'Q3'
    elif moth > 9 and moth <= 12:
        return 'Q4'
    else: 
        return

        
# creo un dizionario il quale prende come chiave il contenuto della colonna in posizione keyindex, e valore quello in posizione valindex.
def createDic(filename, keyindex, valindex):    
    file= open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti'+filename , mode='r')
    skip=True
    filedic= dict()
    for line in file.readlines():
        
        row= line.split(',')
        if skip:
            skip=False
            continue
        else:
            filedic[row[keyindex]] = row[valindex]
    file.close()        
    return filedic



# assegna il valore 1 se l'utente ha risposto correttamente a tutte le domande, 0 altrimenti
def iscorrect(answer_value, correct_answer):
    if answer_value == correct_answer:
        corr = 1
    else:
        corr = 0
    return corr



# Mappo le regioni ad un codice unico per generare geoid 
def codificaRegione(filename):
    
    regioncod= dict()
    
    with open(r'C:/Users/Utente/Desktop/Università/Pisa/Primo semestre - Secondo anno/Laboratory of datat science/PROGETTO/TRACCIA/answerdatasetnew/'+ filename , mode='r') as file:         
       
        value= 0
        
        for line in file.readlines():
            row2= line.split(',')  
            
            if row2[len(row2)-2] not in regioncod.keys():
                regioncod[row2[len(row2)-2]] = value
                value += 1           
    return regioncod  


# converto i valori numerici in gender
def nameGender(col):
    
    if col == '0':
        return 'Neutral'
    elif col == '1':
        return 'Female'
    elif col == '2':
        return 'Male'
        
        
        
        
    
    

    
    
