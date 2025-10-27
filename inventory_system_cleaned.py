"""
A simple inventory management system.
"""

import json
from datetime import datetime

# --- NO GLOBAL VARIABLE ---

def add_item(stock_data, item="default", qty=0, logs=None):
    """Adds an item to the inventory stock."""
    if logs is None:
        logs = []

    # Validation to check the data types
    if not isinstance(qty, (int, float)):
        print(f"Error: Invalid quantity '{qty}'. Must be a number.")
        return
    if not isinstance(item, str) or not item:
        print(f"Error: Invalid item name '{item}'. Must be a string.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(stock_data, item, qty):
    """Removes a quantity of an item from stock."""
    try:
        if item not in stock_data:
            raise KeyError(f"Item '{item}' not found in inventory.")

        if not isinstance(qty, (int, float)) or qty < 0:
            raise TypeError("Quantity must be a positive number.")

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except (KeyError, TypeError) as e:
        print(f"Error removing item: {e}")

def get_qty(stock_data, item):
    """Gets the quantity of a specific item."""
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    """
    Loads inventory data from a JSON file.
    This function NO LONGER uses a global. It returns the data.
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
            return loaded_data
    except FileNotFoundError:
        print(f"Warning: {file} not found. Starting with empty inventory.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode {file}. Using empty inventory.")
        return {}

def save_data(stock_data, file="inventory.json"):
    """Saves inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

def print_data(stock_data):
    """Prints a report of all items and their quantities."""
    print("--- Items Report ---")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")
    print("--------------------")

def check_low_items(stock_data, threshold=5):
    """Returns a list of items below the threshold."""
    return [item for item, quantity in stock_data.items() if quantity < threshold]

def main():
    """Main function to run the inventory system."""
    # stock_data is now a local variable, loaded by the function
    stock_data = load_data()

    # Pass stock_data as the first argument to every function
    add_item(stock_data, "apple", 10)
    add_item(stock_data, "banana", -2)
    add_item(stock_data, 120, "ten")
    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)

    print(f"Apple stock: {get_qty(stock_data, 'apple')}")
    print(f"Low items: {check_low_items(stock_data)}")

    save_data(stock_data)
    print_data(stock_data)

if __name__ == "__main__":
    main()
    # (This file also includes the final newline and no trailing whitespace)
