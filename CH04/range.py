#Answer the question using code. How many are there if you count from 1 to 100 by 3?
#create a list using range
#some_range = list(range(0, 100, 3))
#then get the length using len() and print it to the screen.
some_range = list(range(0,100,3))
message = 'There are {} when counting between 0 and 100 in increments of 3'
print(message.format(len(some_range)))