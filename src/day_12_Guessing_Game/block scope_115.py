#There is no block scope in python

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# if you create a vaiable within a function it is only avaiable to that function
# if you create a vaiable within a if block, while loop, for loop, or anything that has the inditation and the colon then that does not count