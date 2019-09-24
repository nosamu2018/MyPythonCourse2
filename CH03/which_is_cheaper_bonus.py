product1_price = input("What is the price of product 1? ")
#print("the type is", type(product1_price))
#print('the type is ',product1_price)
price1 = float(product1_price)

#print ('the type of price1 is',type(price1))
#ask for the weight of productq in ounces and convert it to float before storing
#as weight
weight1 = float(input("How many ounces is product 1? "))

# do the same for product2
price2 = float(input("What is the price of product 2? "))
weight2 = float(input("How many ounces is product 2? "))

# Play with the print statement for debug

#igure out which product is the best value. 
#Calculate the price per ounce for product 1 and product 2.
price_per_ounce1 = price1 / weight1
price_per_ounce2 = price2 / weight2
print("Price per ounce of product 1:")
print(price_per_ounce1)
print("Price per ounce of product 2:")
print(price_per_ounce2)

#Create a message that displays true or fales statement

print("Product 1 is cheaper",price_per_ounce1 < price_per_ounce2)


