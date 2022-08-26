import re
import math

def add_time(start, duration, Day=None):
    
    #### EXTRACTIG ALL DATA ####
    
    #Extract Time
    Time_name = re.findall(r'\wM',start)
    Time_name = Time_name[0]
    #print(Time_name)
    
    #Extract Houres
    start_hour = re.findall(r'[0-9]+',start)
    start_hour = int(start_hour[0])
    duration_hour = re.findall(r'[0-9]+',duration)
    duration_hour = int(duration_hour[0])
    #print(start_hour)
    
    #Extract Minutes
    start_min = re.findall(r':([0-9]+)',start)
    start_min = int(start_min[0])
    duration_min = re.findall(r':([0-9]+)',duration)
    duration_min = int(duration_min[0])
    #print(start_min)
    
    #### MATH #####
    if Time_name == "PM":
        start_hour = start_hour + 12
        
    hour=0
    add_Day=0
    
    final_min = start_min + duration_min
    if final_min > 60:
        hour = int(math.trunc(final_min / 60))
        final_min = final_min -  hour*60
        #print(hour)

    
    
        
    


    #new_time= "15:00"
    #return new_time