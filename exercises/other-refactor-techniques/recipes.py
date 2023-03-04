# by Kami Bigdely
# Extract Class
# foods = {
    # 'Butternut Squash Soup':[45, True, 'soup','North African',
    # ['butter squash','onion','carrot', 'garlic','butter','black pepper', 'cinnamon','coconut milk'],
    # '1. Grill the butter squash, onion, carrot and garlic in the oven until they get soft and golden on top. ' 
    # '2. Put all in blender with butter and coconut milk. Blend them till they become puree. Then move the contents into a pot. '
    # '3. Add coconut milk. Simmer for 5 minutes. '],

    # 'Shirazi Salad':[5, True, 'salad','Iranian', 
    # ['cucumber', 'tomato', 'onion', 'lemon juice'],
    # '1. dice cucumbers, tomatoes and onions ' 
    # '2. put all into a bowl '
    # '3. pour lemon juice. add salt '
    # '4. Mix them thoroughly '],
    
    # 'Home-made Beef Sausage': [60, False, 'deli','All',
    # ['sausage casing', 'regular ground beef','garlic','corriander seeds','black pepper seeds','fennel seed','paprika'],
    # '1. In a blender, blend corriander seeds, black pepper seeds, fennel seeds and garlic to make the seasonings. '
    # '2. In a bowl, mix ground beef with the seasoning '
    # '3. Add all the content to a sausage stuffer. Put the casing on the stuffer funnel. Rotate the stuffer handle (or turn it on) to make your yummy sausages! ']}
foods = [
    Recipe('Butternut Squash Soup', 45, True, 'soup','North African',
    ['butter squash','onion','carrot', 'garlic','butter','black pepper', 'cinnamon','coconut milk'],
    '1. Grill the butter squash, onion, carrot and garlic in the oven until they get soft and golden on top. ' 
    '2. Put all in blender with butter and coconut milk. Blend them till they become puree. Then move the contents into a pot. '
    '3. Add coconut milk. Simmer for 5 minutes. '),
    Recipe('Shirazi Salad', 5, True, 'salad','Iranian', 
    ['cucumber', 'tomato', 'onion', 'lemon juice'],
    '1. dice cucumbers, tomatoes and onions ' 
    '2. put all into a bowl '
    '3. pour lemon juice. add salt '
    '4. Mix them thoroughly '),
    Recipe('Home-made Beef Sausage', 60, False, 'deli','All',
    ['sausage casing', 'regular ground beef','garlic','corriander seeds','black pepper seeds','fennel seed','paprika'],
    '1. In a blender, blend corriander seeds, black pepper seeds, fennel seeds and garlic to make the seasonings. '
    '2. In a bowl, mix ground beef with the seasoning '
    '3. Add all the content to a sausage stuffer. Put the casing on the stuffer funnel. Rotate the stuffer handle (or turn it on) to make your yummy sausages! ')
    ]

class Recipe:
    def __init__(self, name, prep_time, is_veggie, food_type, cuisine, ingredients, recipe):
        self.name = name
        self.prep_time = prep_time
        self.is_veggie = is_veggie
        self.food_type = food_type
        self.cuisine = cuisine
        self.ingredients = ingredients
        self.recipe = recipe

for food in foods:
    print("Name:", food.name)
    print("Prep time:", food.prep_time, "mins")
    print("Is Veggie?", 'Yes' if food.is_veggie else "No")
    print("Food Type:", food.food_type)
    print("Cuisine:", food.cuisine)
    print("Ingredients:")
    for item in food.ingredients:
        print(item, end=', ')
    print()
    print("Recipe:", food.recipe)
    print("***")






# maybe i'm overthinking it so i'm just commenting this out cuz idk. 
# maybe i'm on the right track but probably overthinking it. 

    # def get_name(self):
    #     print("Name:", self.name)
    #     return 

    # def get_prep_time(self):
    #     return self.prep_time

    # def get_is_veggie(self):
    #     return self.is_veggie

    # def get_food_type(self):
    #     return self.food_type

    # def get_cuisine(self):
    #     return self.cuisine
    
    # def get_ingredients(self):
    #     for item in self.ingredients:
    #         print(item, end=', ')
    #     return self.ingredients

    # def get_recipe(self):
    #     return self.recipe

# for key, value in foods.items():
#     print("Name:",key)
#     print("Prep time:",value[0], "mins")
#     print("Is Veggie?", 'Yes' if value[1] else "No")
#     print("Food Type:", value[2])
#     print("Cuisine:", value[3])
#     for item in value[4]:
#         print(item, end=', ')
#     print()
#     print("Recipe:", value[5])
#     print("***")

    # The dictionary carries too much info and is hard to read 
    # so we would suggest creating a food class where you can initialize it with 
    # the food’s name, prep time, is_veggie, food_type, cuisine, (ingredients?) and recipe
    # Our group would create a class named Recipe. 
    # It would have attributes including recipe_name, prep_time, is_veggie, food_type, cuisine, ingredients (a list), and instructions. 
    # Each print statement would be a method of the class
    # Create a new class for the foods and move the print statements into class methods
