squares = {1:1,5:25,2:4,3:9,4:16}
print ('squares=',squares)


#GET ALL THE KEYS AND VALUES BY CALLING ITEMS(). USE FOR LOOP
for key,value in squares.items():
    print(f'The square of {key} is {value}')

#remove an item using pop()
print('pop(4)=', squares.pop(4))

#new output
print('squares', squares)

#add a new square
squares[6] = 36
print('squares added [6]: ',squares)
#use popitem() to remove last added item
print('squares.popitem()', squares.popitem())
print('squares after popitem()', squares)

#delete a particular item
del squares[2]
print('squares after del square[2]', squares)

#delete an item with invalid notation gives an error
#del squares[7]

#del squares
#print(squares) #should give an error