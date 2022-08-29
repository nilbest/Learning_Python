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
    new_time_name = "AM"
    
    final_min = start_min + duration_min
    
    if final_min > 60:
        hour = int(math.trunc(final_min / 60))
        final_min = final_min -  hour*60
        duration_hour = duration_hour + hour
        #print(hour)
    
    final_hour = start_hour + duration_hour
 
    
    add_Day = int(math.trunc(final_hour / 24))
 
    if add_Day > 0:
        #print("Test"+str((final_hour / 24)-int(math.trunc(final_hour / 24))))
        Test=(final_hour / 24)-int(math.trunc(final_hour / 24))
        final_hour = round(Test*24)
    
    if final_hour >= 12:
        #print("Test"+str(final_hour))
        if final_hour > 12:
            final_hour = final_hour - 12
        else:
            final_hour = final_hour
        #print(final_hour)
        new_time_name = "PM"
    
    if final_hour < 1:
        final_hour = 12
        
    
    
    if Day !=None:
        new_Day = Day.capitalize()
        Days= {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
        searche_Days={"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
        calculate_Day = ((add_Day/7)-int(math.trunc(add_Day/7)))*7
        new_Day = searche_Days[new_Day]
        new_Day = Days[int(new_Day+calculate_Day)]  if int(new_Day+calculate_Day) <= 7 else Days[int(new_Day+calculate_Day-7)]
        
            
        
        
    if final_min < 10:
        final_min = "0"+str(final_min)
        
    ### Ausgabe Formatter ###
    if Day !=None:
        if add_Day == 1:
            # Returns: 1:40 AM (next day)
            new_time = f"{final_hour}:{final_min} {new_time_name}, {new_Day} (next day)"
            return new_time
    
        if add_Day > 1:
            # Returns: 12:03 AM, Thursday (2 days later)
            new_time = f"{final_hour}:{final_min} {new_time_name}, {new_Day} ({add_Day} days later)"
            return new_time
        
        new_time = f"{final_hour}:{final_min} {new_time_name}, {new_Day}"
        return new_time
    
    if add_Day == 1:
        # Returns: 1:40 AM (next day)
        new_time = f"{final_hour}:{final_min} {new_time_name} (next day)"
        return new_time
    
    if add_Day > 1:
        # Returns: 7:42 AM (9 days later)
        new_time = f"{final_hour}:{final_min} {new_time_name} ({add_Day} days later)"
        return new_time
    
    new_time = f"{final_hour}:{final_min} {new_time_name}"
    return new_time