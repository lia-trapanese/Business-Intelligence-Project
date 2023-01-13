# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:56:49 2022

@author: Lia Trapanese, Giovanni Battista D'Orsi
"""

with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdatasetnew\answerdatacorrect.csv', mode='r') as file:
    
    header = ['organizationid', 'groupid', 'quizid', 'schemeofworkid']
    
    organizationid = [] 
    groupid = []  
    quizid = []  
    schemeofworkid = []  
        
    no_duplicates = set()  # evita duplicati
    
    
    # LEGENDA: col 10 = groupid, col 11 = quizid, col 12 = schemeofworkid
    for line in file.readlines()[1:]:
        row= line.split(',')
        

        if str(row[10]) + '_' + str(row[11]) + '_' + (row[12][:-2]) not in no_duplicates:        # se non è stato già processato
            no_duplicates.add(str(row[10]) + '_' + str(row[11]) + '_' + (row[12][:-2]))      
            organizationid.append(str(row[10]) + '_' + str(row[11]) + '_' + (row[12][:-2]))      # organizationid = concatenazione di groupid, quizid e schemeofworkid
            groupid.append(row[10])
            quizid.append(row[11])
            schemeofworkid.append(row[12])


with open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\Organization.csv', mode='w') as orgfile:        
    
    for j in range(len(header)):
        if j == len(header)-1:
            orgfile.write(str(header[j])+'\n')
        else:
            orgfile.write(str(header[j])+',')
        
    for organizationid, groupid, quizid, schemeofworkid in zip(organizationid,groupid,quizid,schemeofworkid):
        orgfile.write(str(organizationid) +','+groupid +',' + quizid+','+schemeofworkid+'\n')


