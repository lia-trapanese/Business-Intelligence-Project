# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 17:03:58 2022

@author: Lia Trapanese, Giovanni D'Orsi
"""

from funzioni import createDic, nameGender

geodic= createDic('\Geography.csv', 1 , 0)       # creo dizionario con chiave region e valore geoid
datedic= createDic('\Date.csv', 1 , 0)           # creo dizionario con chiave date e valore dateid



users=set()

with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdatasetnew\answerdatacorrect.csv', mode='r') as file:
    with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\Users.csv', mode='w') as userfile:
        
        header= 'userid,dateofbirthid,geoid,gender\n'
        userfile.write(header)
        skip=True
        for riga in file.readlines()[1:]: 
            rig= riga.split(',')
                        
            if rig[1] in users:
                continue
            else:
                userfile.write(str(rig[1]) + ',' + datedic[rig[6]] + ',' + geodic[rig[len(rig)-2]] + ',' + str(nameGender(rig[5])) + '\n')
                users.add(rig[1])           # evitare utenti duplicati
                
                    
            
              
        

