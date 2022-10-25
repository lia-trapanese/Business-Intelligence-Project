# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:54:50 2022

@author: Utente
"""

import ast
import csv
with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdatasetnew\answerdatacorrect.csv', 
          mode='r') as file:
        
        f = file.readlines()
                
        d = dict()
        sbjs = set()
        count_id = 0
        skip=True
        for line in f:
            if skip == True:
                skip=False
                continue
            else:
                row= line.split('"')  
                subjs_group = ast.literal_eval(row[1])        #prendo la lista di materie che è in posizione 1, perche prima ho una stringa con tutte le colonne
                if str(subjs_group) not in sbjs:            #stringa per inserirla nel set per evitare duplicati
                    d[count_id] = subjs_group               #popolato il dizio con chiave con gruppo di materie e valore la lista di materie
                    sbjs.add(str(subjs_group))              
                    count_id +=1
                else:
                    continue


        
                
with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdatasetnew\subject_metadata.csv', mode='r') as subfile:        
    with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\Subject.csv', mode='w') as sufile:
        
        header= 'subjectid, description\n'
        sufile.write(header)
            
        subject= dict()
        skip= True
        
        rows = csv.reader(subfile)
        
        for row in rows:

            if skip:        
               skip = False
               continue
            else:
                subjnum= row[0]
                if subjnum not in subject.keys():
                    subject[int(subjnum)] = row[1]


        for k in d.keys():
            d[k] = [subject[d[k][i]] for i in range(len(d[k]))]
            sufile.write( str(k) + ',' + ' - '.join([x.replace(',',' ') for x in d[k]]) + '\n')

    


