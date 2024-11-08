from models import Database

def display_menu():
    print("\nChocolate House")
    print("1. Show the Seasonal Flavors")
    print("2. Provide the Seasonal Flavors")
    print("3. Delete the Seasonal Flavors")
    print("4. Show the Ingredients Inventory")
    print("5. Provide the Ingredient")
    print("6. Delete the Ingredient")
    print("7. Show the Customer Suggestions")
    print("8. Provide the Customer Suggestion")
    print("9. Delete the Customer Suggestion")
    print("0. Exit")

def list_flavors(db):
    flavors = db.list_flavors()
    print("\nSeasonal Flavors:")
    for flavor in flavors:
        print(f"ID: {flavor[0]}, Name: {flavor[1]}, Description: {flavor[2]}, Available: {bool(flavor[3])}")

def add_flavor(db):
    flavor_name = input("Enter flavor name: ")
    description = input("Enter description: ")
    availability = input("Is it available (y/n)? ").lower() == 'y'
    db.add_flavor(flavor_name, description, availability)
    print("Flavor added successfully.")

def delete_flavor(db):
    flavor_id = int(input("Enter the ID of the flavor to delete: "))
    db.delete_flavor(flavor_id)

def list_ingredients(db):
    ingredients = db.list_ingredients()
    print("\nIngredients Inventory:")
    for ing in ingredients:
        print(f"ID: {ing[0]}, Name: {ing[1]}, Quantity: {ing[2]} {ing[3]}")

def add_ingredient(db):
    name = input("Enter ingredient name: ")
    quantity = int(input("Enter quantity: "))
    unit = input("Enter unit: ")
    db.add_ingredient(name, quantity, unit)
    print("Ingredient added successfully.")

def delete_ingredient(db):
    ingredient_id = int(input("Enter the ID of the ingredient to delete: "))
    db.delete_ingredient(ingredient_id)

def list_suggestions(db):
    suggestions = db.list_suggestions()
    print("\nCustomer Suggestions:")
    for sugg in suggestions:
        print(f"ID: {sugg[0]}, Name: {sugg[1]}, Suggestion: {sugg[2]}, Allergy Concerns: {sugg[3]}")

def add_suggestion(db):
    customer_name = input("Enter customer name: ")
    flavor_suggestion = input("Enter flavor suggestion: ")
    allergy_concerns = input("Enter allergy concerns: ")
    db.add_customer_suggestion(customer_name, flavor_suggestion, allergy_concerns)
    print("Suggestion added successfully.")

def delete_suggestion(db):
    suggestion_id = int(input("Enter the ID of the suggestion to delete: "))
    db.delete_suggestion(suggestion_id)

def main():
    db = Database()
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == "1":
            list_flavors(db)
        elif choice == "2":
            add_flavor(db)
        elif choice == "3":
            delete_flavor(db)
        elif choice == "4":
            list_ingredients(db)
        elif choice == "5":
            add_ingredient(db)
        elif choice == "6":
            delete_ingredient(db)
        elif choice == "7":
            list_suggestions(db)
        elif choice == "8":
            add_suggestion(db)
        elif choice == "9":
            delete_suggestion(db)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
