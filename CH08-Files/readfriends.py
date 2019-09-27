
with open('friends.txt') as friend_file:
    #while True:
    for x in friend_file:
        if not x.startswith('#'):
                #contents = friend_file.read()
            print(x)
    