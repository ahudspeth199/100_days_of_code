#local scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)

#notice the error when entering potion_strength the variable was created inside the function and not available outside the function


#if you want to access a variable outside the function you are talking about global scope

#global scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

# because player_health variable is created above the all functions it is a global scope


# whenever you give name to anything rather function or variable you must be aware of where you created it

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

#notice where you must call the funtion drink_potion()
    drink_potion()

print(player_health)