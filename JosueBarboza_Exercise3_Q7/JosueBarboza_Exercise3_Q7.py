import arcpy  
from arcpy import env 
env.overwriteOutput = True 
 
arcpy.env.workplace = r'C:\Users\jbarboza\Desktop\Exercise3.gdb'
inFeatures = r'C:\Users\jbarboza\Desktop\Exercise3.gdb\CallsforService' 
outLocation = r'C:\Users\jbarboza\Desktop\Exercise3.gdb' 
outFeatureClass = 'Alarm' 
delimitiedField = arcpy.AddFieldDelimiters(inFeatures, 'CFSType') 
expression = delimitiedField + " = 'Alarm Call'"

arcpy.FeatureClassToFeatureClass_conversion( inFeatures, outLocation, outFeatureClass, expression)  


