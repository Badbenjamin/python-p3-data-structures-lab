spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_list = []
    for food in spicy_foods:
        spicy_list.append(food["name"])
    return spicy_list
       

def get_spiciest_foods(spicy_foods):
    spiciest_list = []
    for food in spicy_foods:
        # print(food["heat_level"])
        if food["heat_level"] > 5:
            spiciest_list.append(food)
        else:
            pass
    return spiciest_list


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = int(food["heat_level"]) * "🌶"
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        # print(cuisine)
        # print(food["cuisine"])
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = int(food["heat_level"]) * "🌶"
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    food_length = len(spicy_foods)
    total_heat = 0
    # print(food_length)
    for food in spicy_foods:
        total_heat = total_heat + food["heat_level"]
        
    return total_heat / food_length

def create_spicy_food(spicy_foods, spicy_food):
   spicy_foods.append(spicy_food)
   return spicy_foods
   
   
# spicy_food = {
#         'name': 'Griot',
#         'cuisine': 'Haitian',
#         'heat_level': 10,
#     }

# create_spicy_food(spicy_foods, spicy_food)

# print(spicy_foods)
