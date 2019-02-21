#Question 9
import arcpy 
from arcpy import env 
env.overwriteOutput = True 
arcpy.env.workspace = r'C:\Users\jbarboza\Desktop\JosueBarboza_Exercise3\Exercise3.gdb' 

arcpy.CreateFeatureclass_management(r'C:\Users\jbarboza\Desktop\JosueBarboza_Exercise3\Exercise3.gdb', 'AZCities', 'POINT', '', 'DISABLED', 'DISABLED')  
arcpy.AddField_management('AZCities', 'City', 'TEXT') 
arcpy.CreateDomain_management(r'C:\Users\jbarboza\Desktop\JosueBarboza_Exercise3\Exercise3.gdb', 'City_Code', 'City_Type', 'TEXT', 'CODED','DUPLICATE','DEFAULT') 

arcpy.AddCodedValueToDomain_management(r'C:\Users\jbarboza\Desktop\JosueBarboza_Exercise3\Exercise3.gdb', 'City_Code', 'A', 'MetroArea') 
arcpy.AddCodedValueToDomain_management(r'C:\Users\jbarboza\Desktop\JosueBarboza_Exercise3\Exercise3.gdb', 'City_Code', 'B', 'Urban') 
arcpy.AddCodedValueToDomain_management(r'C:\Users\jbarboza\Desktop\JosueBarboza_Exercise3\Exercise3.gdb', 'City_Code', 'C', 'Rural') 
arcpy.AddCodedValueToDomain_management(r'C:\Users\jbarboza\Desktop\JosueBarboza_Exercise3\Exercise3.gdb', 'City_Code', 'D', 'Town') 
arcpy.AddCodedValueToDomain_management(r'C:\Users\jbarboza\Desktop\JosueBarboza_Exercise3\Exercise3.gdb', 'City_Code', 'E', 'Capital') 

