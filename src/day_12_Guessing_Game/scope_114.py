## understanding scope
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# she used the example of an apple tree inside the fence and one outside the fence
# know apply that same example to the function and a print statment outside the function

