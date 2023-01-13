# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:16:59 2022

@author: Lia Trapanese, Giovanni D'Orsi
"""

import sys 
sys.path.append('C:/Users/Utente/Desktop/Università/Pisa/Primo semestre - Secondo anno/Laboratory of datat science/PROGETTO/codici finiti/')

from funzioni import * 
from Subjectdef import *
  
        
diziodate = createDic('\Date.csv', 1 , 0)               # creo dizionario con chiave date e valore dateid
                   

def writeanswer(outputfilename, inputfilename):
    file = open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\TRACCIA\answerdatasetnew\\' + inputfilename, "r")                  
    rawanswer = csv.DictReader(file)           
    answerfile= open(r'C:\Users\Utente\Desktop\Università\Pisa\Primo semestre - Secondo anno\Laboratory of datat science\PROGETTO\codici finiti\\' + outputfilename, mode='w')
    
    answerfile.write('answerid,questionid,userid,organizationid,dateid,subjectid,answer_value,correct_answer,iscorrect,confidence\n')

    for riga in rawanswer:     
        orgid= str(riga['GroupId']) + '_' + str(riga['QuizId']) + '_' + str(int(float(riga['SchemeOfWorkId'])))       # genero orgid nello stesso modo in cui è stato creato per la tabella organization
        answerfile.write( str(riga['AnswerId']) + ',' + str(riga['QuestionId']) + ',' + str(riga['UserId']) + ',' + orgid + ',' + diziodate[riga['DateAnswered'][:10]] + ',' + str(inv_diziosubj[riga['SubjectId']]) + ',' + str(riga['AnswerValue']) + ',' + str(riga['CorrectAnswer']) + ',' + str(iscorrect(riga['AnswerValue'],riga['CorrectAnswer'])) + ',' + str(riga['Confidence']) + '\n' )          
                
    
    answerfile.close()  
    file.close()
        
            
outputfilename = 'Answer.csv'
inputfilename = 'answerdatacorrect.csv'
        
writeanswer(outputfilename, inputfilename)

                    
    


