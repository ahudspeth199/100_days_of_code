

from prettytable import PrettyTable

# PrettyTable documentation: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki


# Create a PrettyTable object and save it to a variable called table

table = PrettyTable()
print(table)

# how to add columns to the table
# methods are functions that are associated with an object
# method will add columns to a table you specify
# Method takes two inputs
# x.add_column("City name", ["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,1554769])
# x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])


table.add_column("Pokemon Name", ["Pikachu","Charizard","Wartortle","Gogoat","Alakazam","Toxicroak","Golbat"])
table.add_column("Type", ["Electric", "Fire", "Water", "Grass", "Psychic", "Poison", "Flying"])

print(table)