#Modifying Global scope

enemies = 1


#you can't take something that is global and modify it within a local scope
# You must say you have a global variable that is defined somewhere outside the function
def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# you may not want to use global scope as it can cause confusion and errors
# avoid modifying global scope

# what could you do instead of modifying global scope, you can use the return statement
# what if instead of modifying the enemies you returned it as the output
enemies = 1
def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
