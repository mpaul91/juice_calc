# Program for calculating cost of making e-juice batches

# Defining ingredient object
class Ingredient(object):
    def __init__(self, price, amount, percentage):
        # Assigns variables to methods
        self.price = price
        self.amount = amount
        # Methods for calculating the price per mililiter of ingredient
        self.per_ml = (float(price) / float(amount)) / 100
        self.percentage = float(percentage) / 100
    # Function to calculate total ml of the ingredient in a given batch size
    def batch_total(self, batch_size):
        return (self.percentage * batch_size)


# Juice ingredients with pricing (in cents) based on the last order
nicotine = Ingredient(1900, 120, 2)
vegetable_glycerin = Ingredient(2800, 3785, 77)
strawberry = Ingredient(3000, 1000, 7)
strawberry_ripe = Ingredient(2100, 500, 5)
watermelon = Ingredient(4750, 1000, 7)
koolada = Ingredient(900, 120, 2)
# SHOULD THE PERCENTAGE OF EACH INGREDIENT BE EMBEDDED IN THE OBJECT, OR IN THE RECIPE??
# COULD EVENTUALLY HAVE THE RECIPE ACTIVELY EDIT THE INGREDIENT OBJECT "PERCENTAGE"
# AND HAVE USER EDIT THE RECIPE AND STORE DIFFERENT RECIPES

# To apply strings to each ingredient for easy printing
orig_recipe = {
nicotine : "Nicotine",
vegetable_glycerin : "Vegetable Glycerin",
strawberry: "Strawberry",
strawberry_ripe: "Strawberry Ripe",
watermelon: "Watermelon",
koolada: "Koolada"
}

# Calculates price of a batch by using an ingredients list
def batch_price(recipe, batch_size):
    total = 0.0
    batch_size = float(batch_size)
    for ingredient in recipe:
        total = total + (ingredient.per_ml * ingredient.batch_total(batch_size))
    return total

# Function for neat printing of the recipe
def print_recipe(recipe):
    print (" ")
    print ("OG Recipe:")
    for ingredient in recipe:
        print (recipe[ingredient] + ":", int(ingredient.percentage * 100), "%")
    print (" ")
get_input = True
# Print results for user
while get_input == True:
    order_size = int(input("Order size? >"))        # Input is immediately converted to int without verification(yet)
    if order_size == 1:
        print_recipe(orig_recipe)
        print (" ")
        print ("Enter '0' to exit or '1' to print recipe")
    elif order_size == 0:
        get_input = False
    else:
        print ("Cost: %.2f" % batch_price(orig_recipe, order_size))
        print (" ")
        print ("Enter '0' to exit or '1' to print recipe")
