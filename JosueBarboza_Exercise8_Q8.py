import arcpy 
record = r'C:\Users\jbarboza\Desktop\Exercise 3.gdb\CallsforService'

counts = arcpy.GetCount_management(record)  

print(counts[0]) 