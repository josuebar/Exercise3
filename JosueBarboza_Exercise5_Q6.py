#Josue Barboza 
#02/19/2019 
#Exercise 3 

#6) 

import arcpy 
from arcpy import env 
arcpy.env.overwriteOutput = True 

arcpy.env.workspace = "C:/Users/jbarboza/Desktop/Exercise 3.gdb" 

arcpy.AddField_management("CallsforService", "Crime_Explanation", "TEXT") 

def BurglaryCall(): 
    if 'CFSType' == 'Burglary Call': 
        arcpy.CalculateField_managment('CallsforService', 'Crime_Explanation', BurglaryCall) 
        return 'This is a burglary'  
