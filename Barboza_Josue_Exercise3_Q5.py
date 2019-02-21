#Josue Barboza 
#02/19/2019 
#GIS 210 

#5) Create a GDB. Using the list provided create a feature class for each of the elements in the list:  

featureList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities',
'Rivers'] 

import arcpy 
import os
from arcpy import env 
env.overwriteOutput =True
#5a) Creating GDB 
arcpy.CreateFileGDB_management(r'C:\Users\jbarboza\Desktop\JosueBarboza_Exercise3','Exercise3.gdb') 

#5b) Creating feature classes from list 
arcpy.env.workspace = "C:/Users/jbarboza/Desktop/JosueBarboza_Exercise3/Exercise3.gdb"

for x in featureList: 
    arcpy.CreateFeatureclass_management("C:/Users/jbarboza/Desktop/JosueBarboza_Exercise3/Exercise3.gdb", x, "POINT", "", "DISABLED", "DISABLED") 



