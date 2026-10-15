'''main'''
ingredients = set()
flavors = set()

allowed_ingredients = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
    "Bean Sprouts", "Noodle", "Chives", "Lime",
    "Egg", "Oil", "Peanuts"
}

allowed_flavors = {"Sweet", "Sour", "Salty"}

while True:
    item = input()
    if item == "Cook":
        break
    ingredients.add(item)

while True:
    flavor = input()
    if flavor == "End":
        break
    flavors.add(flavor)

if not ingredients.issubset(allowed_ingredients):
    print("This is not Pad Thai!!!")
elif ingredients != allowed_ingredients:
    print("This is bad!")
elif flavors == allowed_flavors:
    print("Delicious!")
else:
    print("Not Bad...")
