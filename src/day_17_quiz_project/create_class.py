

# to create a class is to use the class keyword
# then give it a name
# finish the class by giving it a colon :
class User:


# because of the : after the class it is expecting something afterwards
# you must enter pass to get around this
    pass
'''

'''''
# instead of the pass you will use the init function
    def __init__(self):
        print("new user being created...")


# after creating a class create your first user object
# to initalize an object from a class you must add the ()
user_1 = User()
user_1.id = "001"
# create a variable to attach to an object
user_1.username = "anthony"
print(user_1.username)

# how to simply creating objects from the class

# in python in order to create the constructor is by using a special function which is the init function


class Car:
    def __init__(self):
    # initialise attributes


# this is used to initialise the attributes
class Car:
    def __init__(self, seats):
        self.seats = seats

# this is what it looks like when we call our constructor

        my_car = Car(5)
# this is the same if we wrote this as:
        my_car.seats = 5



PascalCase

#first word is lower case
camelCase

# all the words lower case separated by _
snake_case


class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
# self.id is the attribute associated with the class User

# you can set a default value for example followers will be set to 0
        self.followers = 0
# and you do not have to create a followers parameter in the init function

user_1 = User("001", "anthony")


print(user_1.username)
print(user_1.id)

user_2 = User("002", "melissa")
print(user_2.username)
print(user_2.followers)
