# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:41:08 2022

@author: Utente
"""

def quarter_generator(moth):
    
    
    if  (moth) >= '1' and (moth) <= '3':
        return 'Q1'
    elif moth > '3' and moth<= '6':
        return'Q2'
    elif moth > '6' and moth <= '9':
        return 'Q3'
    else:
        return 'Q4'
    

        

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




def iscorrect(answer_value, correct_answer):
    if answer_value == correct_answer:
        corr = 1
    else:
        corr = 0
    return corr



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


