# Lab 5: Known Issue Table

[cite_start]This table documents all issues identified by static analysis tools and manual testing, along with the solutions implemented to achieve a 10/10 Pylint score.

| Issue Code(s) | Tool | Type | Line(s) (Original) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`B307` / `W0123`** | Bandit / Pylint | Security (Medium) | 59 | `Use of possibly insecure function` / `Use of eval` | **Fixed:** Removed the `eval("print('eval used')")` line entirely from the `main()` function. |
| **`W0102`** | Pylint | Bug / Warning | 8 | `Dangerous default value [] as argument` | **Fixed:** Changed the function definition to `logs=None`, then added `if logs is None: logs = []` inside the function. |
| **`E722` / `W0702`** | Flake8 / Pylint | Bug / Error | 19 | `do not use bare 'except'` / `No exception type(s) specified` | **Fixed:** Replaced the bare `except:` with `except KeyError:` and `except TypeError:` to specifically handle expected errors. |
| **`F401` / `W0611`** | Flake8 / Pylint | Style / Warning | 2 | `'logging' imported but unused` | **Fixed:** Deleted the `import logging` line from the top of the file. |
| **`N/A (Runtime)`** | Manual Testing | Bug / Crash | 50 | `TypeError: unsupported operand type(s) for +: 'int' and 'str'` | **Fixed:** Added `isinstance()` checks at the start of `add_item` and `remove_item` to validate `item` and `qty` data types before use. |
| **`W0603`** | Pylint | Code Smell (Warning) | 27 | `Using the global statement (global-statement)` | **Fixed:** Refactored the entire program to remove the global variable. `stock_data` is now a local variable in `main()` and is passed as a parameter to all functions that need it. |
| **`R1732` / `W1514`** | Pylint | Code Smell (Warning) | 26, 32 | `Consider using 'with' for resource-allocating operations` / `Using open without explicitly specifying an encoding` | **Fixed:** Replaced all `f = open()` calls with the `with open(..., encoding="utf-8") as f:` syntax for safe file handling. |
| **`C0103`** | Pylint | Style (Convention) | 8, 14, 22... | `Function name "addItem" doesn't conform to snake_case naming style` | **Fixed:** Renamed all functions to `snake_case` (e.g., `addItem` became `add_item`). |
| **`C0114` / `C0116`** | Pylint | Style (Convention) | 1, 8, 14... | `Missing module docstring` / `Missing function or method docstring` | **Fixed:** Added a module-level docstring and descriptive docstrings to every function. |
| **`C0303` / `C0304`** | Pylint | Style (Convention) | (Various) | `Trailing whitespace` / `Final newline missing` | **Fixed:** Removed all extra spaces from the ends of lines and added a single blank line at the very end of the file. |
