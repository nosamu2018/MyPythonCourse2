some_nums = [2,6,4,2,22,54,12,8,-1]
#Print the lenght
len(some_nums)
#Print the sum using a function called sum.
print('the sum of the list is: ',sum(some_nums))
print (some_nums[0])

highest_num = some_nums[0]
for x in some_nums:
    if x > highest_num:
        highest_num = x
print('the highest number is ', highest_num)
#Now change some_nums so that every other items is the number 11.

#You cannot change values while in a for loop that is iterating over the collection.
#You can though, create a for loop with a range, and use its counter as an index
#some_nums = [2,6,4,2,22,54,12,8,-1]
for x in range(len(some_nums)-1):
    print (x)
    if (x%2==0):
        some_nums [x] = 11
    print(some_nums) 