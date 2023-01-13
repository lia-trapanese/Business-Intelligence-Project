# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:53:26 2022

@author: Lia Trapanese, Giovanni D'Orsi
"""

import pyodbc
import csv

def load_todb(file, table):
    
    server = 'tcp:131.114.72.230'
    database="Group_11_DB"
    username="Group_11"
    password="WJYVTXS0"
    
    connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
    cnxn = pyodbc.connect(connectionString)
    cursor = cnxn.cursor()  
    
    csv_file = csv.DictReader(file, delimiter = ",")
    columns_list = csv_file.fieldnames        # lista con i nomi delle colonne
    columns= str(csv_file.fieldnames).replace('[', '').replace(']', '').replace('\'','').strip()    # stringa con nomi delle colonne senza spazi da utilizzare nella insert into
    questions= (len(csv_file.fieldnames)*'?').replace('', ',')[1:-1]          # genera in automatico i ? in base ai campi da inserire nella tabella
   
    
    sql_query = "INSERT INTO "+table+"("+columns+") VALUES ("+questions+")"  
    i=1
    
    for row in csv_file:
        # controlla che il nome della tabella da caricare in modo tale da utilizzare il numero corretto di valori da scrivere.
        if table=='Users':
            val=(row[columns_list[0]],row[columns_list[1]], row[columns_list[2]], row[columns_list[3]])
        elif table=='Subject':
            val=(row[columns_list[0]],row[columns_list[1]])
        elif table=='Geography':
            val=(row[columns_list[0]],row[columns_list[1]], row[columns_list[2]], row[columns_list[3]])
        elif table=='Organization':
            val=(row[columns_list[0]],row[columns_list[1]], row[columns_list[2]], row[columns_list[3]])
        elif table=='Answers':
            val=(row[columns_list[0]],row[columns_list[1]], row[columns_list[2]], row[columns_list[3]], row[columns_list[4]],row[columns_list[5]], row[columns_list[6]], row[columns_list[7]],row[columns_list[8]],row[columns_list[9]])
        elif table=='Date':
            val=(row[columns_list[0]],row[columns_list[1]], row[columns_list[2]], row[columns_list[3]], row[columns_list[4]])
        else:
            raise ValueError('Table not in scope')
        cursor.execute(sql_query, val)
        print("Loading row %d" %i)
        i=i+1
        
    file.close()
    cnxn.commit()
    cursor.close()
    cnxn.close()

#LOADING ALL TABLES
tb_toload= ['Geography','Date','Organization','Subject','Users','Answers']
for tb in tb_toload:
    file = open(r"C:/Users/Utente/Desktop/Università/Pisa/Primo semestre - Secondo anno/Laboratory of datat science/PROGETTO/codici finiti/"+tb+".csv", "r")
    load_todb(file, tb)


