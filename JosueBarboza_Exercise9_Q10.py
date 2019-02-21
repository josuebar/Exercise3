#Question 10 

import arcpy 

from arcpy import env 
env.overwriteOutput = True 
targetFeatures = r'C:\Users\jbarboza\Desktop\Exercise 3.gdb\Tracts' 
joinFeatures = r'C:\Users\jbarboza\Desktop\Exercise 3.gdb\General_Offense' 
outputFeatures = r'C:\Users\jbarboza\Desktop\Exercise 3.gdb\Joined_Tracts_Offense' 
arcpy.SpatialJoin_analysis (targetFeatures, joinFeatures, outputFeatures) 