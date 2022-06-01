# Dictionary in List

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited,times_visited, cities_visited):

# Create a new dictionary
    dict_country = {}
    dict_country["country"] = country_visited
    dict_country["visits"] = times_visited
    dict_country["cities"] = cities_visited

# now you can take your list travel_log then add to the list using append
# you will use the newly created dictionary to add
    travel_log.append(dict_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)