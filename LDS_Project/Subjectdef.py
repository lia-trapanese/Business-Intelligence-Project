# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:54:50 2022

@author: Lia Trapanese, Giovanni D'Orsi
"""

import ast
import csv

with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdatasetnew\answerdatacorrect.csv', 
          mode='r') as file:
        
        # creo un dizionario in cui ad ogni indice è associata una lista di subjects (svolte nei tests degli users) in formato numerico       
        diziosubj = dict() 
        sbjs = set()
        count_id = 0
        
        for line in file.readlines()[1:]:
            row= line.split('"')  
            
            subjs_group = ast.literal_eval(row[1])      # prendo la lista di materie che è in posizione 1, perche lo split è stato fatto in base all'apice " pittosto che '.
                                                        # Quindi in posizione 0 ho una stringa con tutte le colonne che precedono la colonna delle subjects
            if str(subjs_group) not in sbjs:            # stringa per inserirla nel set per evitare duplicati
                diziosubj[count_id] = subjs_group               # ho popolato il dizionario assegnando una chiave ad ogni lista di materie
                sbjs.add(str(subjs_group))              
                count_id +=1
            else:
                continue



inv_diziosubj = {str(v): k for k, v in diziosubj.items()}      
#print(inv_diziosubj) 

              
with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdatasetnew\subject_metadata.csv', mode='r') as subfile:        
    with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\Subject.csv', mode='w') as sufile:
        
        header= 'subjectid,description\n'
        sufile.write(header)
            
        subject= dict()                                         # dizionario con chiave l'indice della materia e come valore una lista contenente descrizione materia e il livello
        skip= True
        
        rows = csv.reader(subfile)
        
        for row in rows:                                        # leggo le righe del file subject_metadata

            if skip:        
                skip = False
                continue
            else:
                subjnum= row[0]                                  # prendo la colonna che indica gli indici delle materie
                  
                if subjnum not in subject.keys():
                    subject[int(subjnum)]= []
                    subject[int(subjnum)].append(row[1])         # ho un dizionario con chiave l'indice delle materie e come valore la rispettiva materia
                    subject[int(subjnum)].append(row[3])         # più il livello
      


        for k in diziosubj.keys():
            
            diziosubj[k] = [(subject[diziosubj[k][i]][0],subject[diziosubj[k][i]][1]) for i in range(len(diziosubj[k]))] 
            # per ogni indice di lista di materie, converto l'indice della materia in una tupla contenente la descrizione della materia e il suo livello.
            diziosubj[k].sort(key= lambda x:x[1])                # ordino in base al livello
            sufile.write( str(k) + ',' + str([diziosubj[k][i][0].replace(',',' ') for i in range(len(diziosubj[k]))]).replace(',',' - ').replace('\'','') + '\n')
            # scrivo il file e formatto le materie sostituendo la virgola con il trattino per mantenere la descrizione integra. 




