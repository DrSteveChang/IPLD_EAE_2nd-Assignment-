# -----------------------------------------------------------------------------
# Warehouse Storage Management System
# Assignment 02 - EAE Business School
# -----------------------------------------------------------------------------
# Topics Covered:
# 1. Arithmetic Operations  6. Conditionals     11. Sets
# 2. Data Types             7. Loops            12. File I/O
# 3. Strings                8. Functions        13. Libraries
# 4. Lists                  9. Dictionaries
# 5. Comparisons            10. Tuples
# -----------------------------------------------------------------------------

import os           # Library: Check file existence
import datetime     # Library: Timestamping for logs
import random       # Library: Generating random IDs
import shutil       # Library: File operations for backup

# --- CONSTANTS ---
FILE_NAME = "warehouse_inventory.txt"
LOG_FILE_NAME = "transaction_log.txt"
BACKUP_DIR = "backups"
LOW_STOCK_THRESHOLD = 5
REQUIRED_CATEGORIES = {"Electronics", "Furniture", "Stationery", "Cleaning"}


# --- HELPER FUNCTIONS ---

def get_valid_number(prompt, data_type=int):
    """
    Topic: Functions, Loops (While), Conditionals
    Robust input handler that prevents crashes on invalid input.
    """
    while True:
        try:
            value = data_type(input(prompt))
            if value < 0:
                print("Error: Value cannot be negative.")
                continue
            return value
        except ValueError:
            print(f"Error: Invalid input. Please enter a valid {data_type.__name__}.")

def log_transaction(action, details):
    """
    Topic: File I/O (Appending), Libraries
    Appends a timestamped record of actions to a log file.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    trans_id = random.randint(1000, 9999)
    try:
        with open(LOG_FILE_NAME, "a") as file:
            file.write(f"[{timestamp}] ID:{trans_id} | {action} | {details}\n")
    except Exception as e:
        print(f"Logging Error: {e}")

def create_backup():
    """
    Topic: Libraries (shutil), File I/O
    Creates a timestamped copy of the inventory file.
    """
    if not os.path.exists(FILE_NAME): 
        return print("Error: No file to backup.")
    
    if not os.path.exists(BACKUP_DIR): 
        os.makedirs(BACKUP_DIR)
        
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"inventory_backup_{timestamp}.txt")
    
    try:
        shutil.copy2(FILE_NAME, backup_path)
        print(f"Backup created: {backup_path}")
        log_transaction("BACKUP", f"Created backup {backup_path}")
    except Exception as e:
        print(f"Backup Error: {e}")


# --- FILE OPERATIONS ---

def load_inventory():
    """
    Topic: File I/O (Read), Strings, Dictionaries
    Reads data from text file into a nested dictionary.
    """
    inventory = {}
    if not os.path.exists(FILE_NAME):
        print("Starting with empty database.")
        return inventory

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 5:
                    inventory[int(data[0])] = {
                        "name": data[1],
                        "category": data[2],
                        "price": float(data[3]),
                        "quantity": int(data[4])
                    }
        print(f"System loaded. {len(inventory)} items active.")
    except Exception as e:
        print(f"Critical Error loading inventory: {e}")
    return inventory

def save_inventory(inventory):
    """
    Topic: File I/O (Write), Loops
    Writes dictionary data to text file.
    """
    try:
        with open(FILE_NAME, "w") as file:
            for item_id, d in sorted(inventory.items()):
                file.write(f"{item_id},{d['name']},{d['category']},{d['price']},{d['quantity']}\n")
        print("Database saved successfully.")
    except Exception as e:
        print(f"Save Error: {e}")


# --- CORE BUSINESS LOGIC ---

def add_or_update_item(inventory):
    """
    Topic: Tuples (Return Values), Conditionals, Arithmetic
    """
    print("\n--- Add / Update Item ---")
    item_id = get_valid_number("Enter Item ID: ", int)
    
    if item_id in inventory:
        print(f"Item found: {inventory[item_id]['name']}")
        qty = get_valid_number("Enter quantity to ADD: ", int)
        inventory[item_id]['quantity'] += qty
        log_transaction("RESTOCK", f"Added {qty} to ID {item_id}")
        return (True, f"Stock updated. New Total: {inventory[item_id]['quantity']}")
    else:
        name = input("Enter Name: ").strip()
        if not name: return (False, "Name cannot be empty.")
        
        allowed = ("Electronics", "Furniture", "Stationery", "Cleaning", "General")
        cat = input(f"Category {allowed}: ").capitalize().strip()
        if cat not in allowed: cat = "General"
        
        price = get_valid_number("Price per unit: ", float)
        qty = get_valid_number("Initial Quantity: ", int)
        
        inventory[item_id] = {"name": name, "category": cat, "price": price, "quantity": qty}
        log_transaction("CREATE", f"Created '{name}' (ID: {item_id})")
        return (True, "New item created.")

def process_order(inventory):
    """
    Topic: Comparisons, Arithmetic
    """
    print("\n--- Process Order ---")
    if not inventory: return print("Inventory empty.")
    
    target_id = get_valid_number("Enter ID to sell: ", int)
    if target_id not in inventory: return print("ID not found.")
    
    item = inventory[target_id]
    print(f"Selected: {item['name']} | Stock: {item['quantity']} | Price: ${item['price']}")
    
    sell_qty = get_valid_number("Qty to sell: ", int)
    if sell_qty == 0: return
    
    if sell_qty > item['quantity']:
        print(f"Error: Only {item['quantity']} available.")
    else:
        cost = sell_qty * item['price']
        item['quantity'] -= sell_qty
        log_transaction("SALE", f"Sold {sell_qty} of ID {target_id}. Total: ${cost:.2f}")
        print(f"Sold! Total: ${cost:.2f}. Remaining: {item['quantity']}")

def remove_item(inventory):
    """
    Topic: Dictionaries (deletion)
    """
    print("\n--- Delete Item ---")
    item_id = get_valid_number("Enter ID to delete: ", int)
    
    if item_id in inventory:
        if input("Confirm delete? (yes/no): ").lower() == "yes":
            name = inventory[item_id]['name']
            del inventory[item_id]
            log_transaction("DELETE", f"Deleted {name} (ID: {item_id})")
            print("Item removed.")
    else:
        print("ID not found.")


# --- REPORTING FUNCTIONS ---

def search_inventory(inventory):
    """
    Topic: Strings (Search), Loops
    """
    query = input("\nSearch (Name/Category): ").lower().strip()
    found = False
    print(f"\n{'ID':<6} | {'Name':<20} | {'Qty':<5} | {'Price':<8}")
    print("-" * 45)
    for pid, item in inventory.items():
        if query in item['name'].lower() or query in item['category'].lower():
            print(f"{pid:<6} | {item['name']:<20} | {item['quantity']:<5} | ${item['price']:<8}")
            found = True
    if not found: print("No matches.")

def calculate_advanced_stats(inventory):
    """
    Topic: Arithmetic, Lists (Max/Min/Sum)
    """
    if not inventory: return print("\nNo data available.")
    
    total_val = sum(i['price'] * i['quantity'] for i in inventory.values())
    total_items = sum(i['quantity'] for i in inventory.values())
    prices = [(i['price'], i['name']) for i in inventory.values()]
    
    most_exp = max(prices, key=lambda x: x[0])[1]
    cheapest = min(prices, key=lambda x: x[0])[1]
    
    print("\n--- Analytics ---")
    print(f"Total Asset Value: ${total_val:,.2f}")
    print(f"Total Units: {total_items}")
    print(f"Most Expensive: {most_exp}")
    print(f"Cheapest: {cheapest}")

def check_category_health(inventory):
    """
    Topic: Sets (Difference Operation)
    """
    current = {item['category'] for item in inventory.values()}
    missing = REQUIRED_CATEGORIES - current
    if missing:
        print(f"\nALERT: Missing categories: {missing}")
    else:
        print("\nHealthy: All categories represented.")

def generate_low_stock_report(inventory):
    """
    Topic: Lists (Filtering)
    """
    low = [i for i in inventory.values() if i['quantity'] < LOW_STOCK_THRESHOLD]
    if low:
        print(f"\nWARNING: Low Stock (<{LOW_STOCK_THRESHOLD}):")
        for i in low: print(f"- {i['name']} (Qty: {i['quantity']})")
    else:
        print("\nAll items well stocked.")


# --- MAIN EXECUTION ---

def main():
    """
    Topic: Loops (While), Functions
    """
    inventory = load_inventory()
    menu = """
    \n=== WAREHOUSE SYSTEM ===
    1. Add/Update Item    4. Analytics        7. Delete Item
    2. Process Order      5. Category Check   8. Backup
    3. Search             6. Low Stock        9. Save & Exit
    """
    while True:
        print(menu)
        c = input("Select: ").strip()
        
        if c == '1':
            _, msg = add_or_update_item(inventory)
            print(msg)
        elif c == '2': process_order(inventory)
        elif c == '3': search_inventory(inventory)
        elif c == '4': calculate_advanced_stats(inventory)
        elif c == '5': check_category_health(inventory)
        elif c == '6': generate_low_stock_report(inventory)
        elif c == '7': remove_item(inventory)
        elif c == '8': create_backup()
        elif c == '9':
            save_inventory(inventory)
            print("Goodbye!")
            break
        else: print("Invalid selection.")

if __name__ == "__main__":
    main()