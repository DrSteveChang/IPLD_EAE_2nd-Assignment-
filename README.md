**IPLD ASSIGNMENT 2**<br>
November 2025

This python program implements a simple Warehouse Storage Management System: **Assignment02_WHS/Assignment02_WHS.py**

***Requirements***
1. Ensure you have Python installed (version 3.latest is recommended).
2. Save the program in your local computer
3.  Execute the program:
        python3 Assignment02_WHS.py 

Once you run the program, an on-console menu-like interface will promt you to input your desired action (from 1 to 9).

The entire program circles around the inventory file. If you run this program for the first time, the ideal first input should be 1. add_or_update_item. Once you have an item in the inventory, you may start prompting different options as the item inventory keeps adding up. 

PYTHON TOPICS COVERED<br>
**1. Arithmetic Operations** <br>
**2. Data Types**: Extensive use of `int`, `float`, `str`, `list`, `dict`, `tuple`, and `set`. <br>
**3. Strings**: Used for input normalization (`.strip()`, `.lower()`), file parsing (`.split(',')`), and formatting (f-strings). <br>
**4. Lists**: Used in `calculate_advanced_stats` to find `max` and `min` prices, and in `generate_low_stock_report` for filtering.<br>
**5. Comparisons**: Checking if a quantity is below a threshold (`<`), if an ID is in the dictionary (`in`), or for valid category input (`not in`).<br>
**6. Conditionals**: `if`/`elif`/`else` blocks for menu selection in main execution funtion, input validation, and checking item existence.<br>
**7. Loops**: `while True` for the main menu and input validation; `for` loops for iterating over dictionary items and file lines.<br>
**8. Functions**: All functionality is declared inside functions (e.g., `main`, `load_inventory`, `add_or_update_item`).<br>
**9. Dictionaries**: The core data structure (`inventory`) for storing product records.<br>
**10. Tuples**: Used as the return type for `add_or_update_item` to pass back a status (`bool`) and a message (`str`).<br>
**11. Sets**: Used in `check_category_health` for the difference operation (`REQUIRED_CATEGORIES - current`) to find missing categories.<br>
**12. File I/O**: Reading inventory (`load_inventory`), writing inventory (`save_inventory`), and appending logs (`log_transaction`).<br>
**13. Libraries**: **`os`**, **`datetime`**, **`random`**, and **`shutil`** are imported and used for system tasks like timestamping and file handling.<br>