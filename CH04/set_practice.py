import random
num_set = {2,6,4,2,22,54,12,8,-1}
print(num_set)
print(len(num_set))

#practice random and intersect
name_list= ['adam','barry','doug','ellen']
volunteer= set(random.sample(name_list,3))
qualified= set (random.sample(name_list,3))

print('Randomly selected Volunteers ', volunteer)
print('Randomly selected qualified ', qualified)

#To find out who is BOTH volunteering AND qualified, you can use the intersection function. 
# Create a new set called new_team and get the intersection of volunteers and qualified people.
new_list = volunteer.intersection(qualified)
print ('new team ', new_list)