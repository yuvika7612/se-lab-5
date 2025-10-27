"""
A simple inventory management system.
(Cleaned version for Lab 5)
"""

import json
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """Adds an item to the inventory stock."""
    if logs is None:
        logs = []

    # --- THIS IS THE FIX ---
    # Add validation to check the data types
    if not isinstance(qty, (int, float)):
        print(f"Error: Invalid quantity '{qty}'. Must be a number.")
        return
    if not isinstance(item, str) or not item:
        print(f"Error: Invalid item name '{item}'. Must be a string.")
        return
    # --- END FIX ---

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    """Removes a quantity of an item from stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    # FIX 3: Replaced bare 'except:' with specific 'KeyError'
    except KeyError:
        print(f"Warning: Item '{item}' not found, cannot remove.")
    except TypeError:
        print(f"Error: Invalid quantity '{qty}' for item '{item}'.")

def get_qty(item):
    """Gets the quantity of a specific item."""
    # Improved: Use .get() to safely return 0 for missing items
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    """Loads inventory data from a JSON file."""
    try:
        # Improved: Use 'with' to auto-close file and add 'encoding'
        with open(file, "r", encoding="utf-8") as f:
            global stock_data
            stock_data = json.load(f)
    except FileNotFoundError:
        print(f"Warning: {file} not found. Starting with empty inventory.")
        stock_data = {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode {file}. Using empty inventory.")
        stock_data = {}

def save_data(file="inventory.json"):
    """Saves inventory data to a JSON file."""
    try:
        # Improved: Use 'with' to auto-close file and add 'encoding'
        with open(file, "w", encoding="utf-8") as f:
            # Improved: Add 'indent=4' for readable JSON
            json.dump(stock_data, f, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

def print_data():
    """Prints a report of all items and their quantities."""
    print("--- Items Report ---")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")
    print("--------------------")

def check_low_items(threshold=5):
    """Returns a list of items below the threshold."""
    # Improved: Use a list comprehension for cleaner code
    return [item for item, quantity in stock_data.items() if quantity < threshold]

def main():
    """Main function to run the inventory system."""
    load_data() # Load first
    add_item("apple", 10)
    add_item("banana", -2)
    
    # These invalid calls are now handled more gracefully
    add_item(123, "ten") 
    remove_item("apple", 3)
    remove_item("orange", 1) # Now prints a warning
    
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    
    save_data()
    print_data()
    
    # FIX 1: The dangerous 'eval()' call has been removed.
    # eval("print('eval used')")  <-- DELETED

# Improved: Use standard __name__ == "__main__" guard
if __name__ == "__main__":
    main()