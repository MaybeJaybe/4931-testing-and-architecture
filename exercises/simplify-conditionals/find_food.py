# by Kami Bigdely
# Remove control flag

def find_food(food, fridge):
    for item in fridge:
        if food in item:
            return item

    return None

if __name__ == "__main__":
    food = 'wasabi'
    food_list = ['onion', 'cucumber','guacamole', 'kabab barg', 'wasabi']
    found_item = find_food(food, food_list)
    print(food, "Found: " + found_item  if found_item != None else "not found")
