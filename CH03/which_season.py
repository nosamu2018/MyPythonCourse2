print ("Welcome to which season program")
month_string = input("Input number of month(e.g January = 1) ? ")
day_string = input("Input number of day of month (e.g Day =1 )? ")
# convert to int
month = int(month_string)
day = int(day_string)

if (month==1) or (month==2):
    Season = 'Winter'
elif (month==4) or (month==5):
    Season = 'Spring'
elif (month==7) or (month==8) or (month==9):
    Season = 'Summer'
elif (month==3) and (day>19):
    Season='Spring'
elif (month==6) and (day>20):
    Season = 'Summer'
elif (month==9) and (day>21):
    Season = 'Autumn'
elif (month==12) and (day>20):
    Season = 'Winter'
else:
    Season = 'Autumn'
print ('Season is ', Season)
