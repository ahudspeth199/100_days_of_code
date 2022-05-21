# in addition to creating attributes we know we can create methods
# the attributes are the things the objects has
# the methods are the things the objects does

'''''
# Method
# inside the class declaration we have a function
# when a function is attached to an object then it is called a method
class Car:
    def enter_race_mode():
        self.seats = 2

# to call the method you must get a hold of the object then use the dot notation
my_car.enter_race_mode()
'''

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

# define a new method
# name your new method follow
# a method unlike a function allows must have a self parameter as the first parameter
# when this method is called it knows the object that called
    #def follow(self):
# in additon to the self parameter now pass in the user
# when a user decides to follow another user their following account goes up by 1
    def follow(self, user):
        user.followers += 1
        self.following += 1

# lets call this method

user_1 = User("001", "anthony")
user_2 = User("002", "melissa")

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)