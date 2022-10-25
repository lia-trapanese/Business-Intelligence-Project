# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 17:03:58 2022

@author: Lia Trapanese
"""

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

geodic= createDic('\Geography.csv', 1 , 0)
datedic= createDic('\Date.csv', 1 , 0)




users=set()

with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdatasetnew\answerdatacorrect.csv', mode='r') as file:
    with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\User.csv', mode='w') as userfile:
        
        header= 'userid, dateofbirthid, geoid, gender\n'
        userfile.write(header)
        skip=True
        for riga in file: 
            rig= riga.split(',')
            
            if skip:
                skip=False
                continue
            else:
                if rig[1] in users:
                    continue
                else:
                    userfile.write(str(rig[1]) + ',' + datedic[rig[6]] + ',' + geodic[rig[len(rig)-2]] + ',' + rig[5] + '\n')
                    users.add(rig[1])
                    
                    
            
        
        

