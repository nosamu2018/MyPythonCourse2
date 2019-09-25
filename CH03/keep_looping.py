print ('Welcome to Keep looping program \n \n')
#create variable keep_looking and set it ot true
keep_looking = True
#begin while loop
while keep_looking:
    month = int(input('Enter numeric day for Month? '))
    day = int(input('Enter numberic day for day? '))

    if (month > 0) and (month < 13) and (day > 0) and (day <= 32):
        print ('You did it')
        keep_looking = False

    else:
        print('Invalid entries: Enter 1-12 for month and 1-31 for day \n \n ')
        
