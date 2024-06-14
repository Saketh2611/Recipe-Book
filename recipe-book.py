# SAKETH-projects
class Recipe:
    def __init__(self, name, ingredients, category):
        self.name = name
        self.ingredients = ingredients
        self.category = category

    def __str__(self):
        ingredients_str = ", ".join(f"{ingredient}: {quantity}" for ingredient, quantity in self.ingredients.items())
        return f"Recipe: {self.name}\nCategory: {self.category}\nIngredients: {ingredients_str}\n"

class RecipeBook:
    def __init__(self):
        self.recipes = {}
        self.categories = {}

    def add_recipe(self, recipe):
        self.recipes[recipe.name] = recipe
        self.categories.setdefault(recipe.category, set()).add(recipe.name)
        print(f"Recipe '{recipe.name}' added successfully.")

    def search_recipe(self, name):
        recipe = self.recipes.get(name)
        print(recipe if recipe else f"Recipe '{name}' not found.")

    def list_recipes_by_category(self, category):
        recipes = self.categories.get(category, set())
        if recipes:
            print(f"Recipes in category '{category}': {', '.join(recipes)}")
        else:
            print(f"No recipes found in category '{category}'.")

    def generate_shopping_list(self, recipe_names):
        shopping_list = {}
        for recipe_name in recipe_names:
            recipe = self.recipes.get(recipe_name)
            if recipe:
                for ingredient, quantity in recipe.ingredients.items():
                    shopping_list[ingredient] = shopping_list.get(ingredient, 0) + quantity
            else:
                print(f"Recipe '{recipe_name}' not found.")
        print("Shopping List:", ", ".join(f"{ingredient}: {quantity}" for ingredient, quantity in shopping_list.items()))

def main():
    recipe_book = RecipeBook()
    
    while True:
        choice = input("\n1. Add Recipe\n2. Search Recipe\n3. List Recipes by Category\n4. Generate Shopping List\n5. Exit\nChoose an option: ")
        
        if choice == '1':
            name = input("Recipe name: ")
            category = input("Category: ")
            ingredients = {}
            while True:
                ingredient = input("Ingredient (or 'done' to finish): ")
                if ingredient == 'done':
                    break
                quantity = input(f"Quantity of {ingredient}: ")
                ingredients[ingredient] = quantity
            recipe_book.add_recipe(Recipe(name, ingredients, category))
        
        elif choice == '2':
            recipe_book.search_recipe(input("Recipe name: "))
        
        elif choice == '3':
            recipe_book.list_recipes_by_category(input("Category: "))
        
        elif choice == '4':
            recipe_names = input("Recipe names (comma-separated): ").split(", ")
            recipe_book.generate_shopping_list(recipe_names)
        
        elif choice == '5':
            break

if __name__ == "__main__":
    main()
