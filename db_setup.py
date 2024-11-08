from models import Database

def initialize_data():
    db = Database()

    # Sample seasonal flavors
    db.add_flavor("Pumpkin Spice", "Spicy autumn flavor")
    db.add_flavor("Peppermint", "Cool winter flavor")

    # Sample ingredients
    db.add_ingredient("Cocoa", 100, "kg")
    db.add_ingredient("Sugar", 200, "kg")

    print("Sample data added successfully.")

if __name__ == "__main__":
    initialize_data()
