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
        # print(food["name"])
        # print(food["cuisine"])
        # print(food["heat_level"])

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass

print_spicy_foods(spicy_foods)