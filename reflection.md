# Lab 5: Static Analysis Reflection

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

* **Easiest:** The easiest fixes were the `F401: unused import logging` and the `B307: use_of_eval`. The tools told me exactly what was wrong, and the fix was just to delete the bad lines of code.

* **Hardest:** The hardest to understand was the `W0102: Dangerous default value []` (the `logs=[]` bug). It wasn't a simple syntax error; I had to understand *why* a list is a problem as a default argument. The `W0603: Using the global statement` was also hard because the fix wasn't just one line—it required refactoring the entire program to pass `stock_data` as a parameter.

### 2. Did the static analysis tools report any "false positives"?

Initially, I thought the `W0603: Using the global statement` warning might be a "false positive" or "too strict" for a small script. However, to get the 10/10 score, I successfully refactored the code to remove the global variable entirely, proving it was a valid warning.

A better example of a low-priority warning (or "false positive") from the original report was `C0103: invalid-name` for function names. While `addItem` works, Pylint strictly enforces the `add_item` (snake_case) convention, which is a style choice rather than a true bug.

### 3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate them in two main ways:

* **1. Local Development (Pre-commit Hooks):** I'd use a tool like `pre-commit` to automatically run Flake8 and Bandit every time I try to `git commit`. This would stop any style errors or security issues from ever getting into the repository.
* **2. Continuous Integration (GitHub Actions):** For a team project, I'd set up a GitHub Action to run all three tools (Pylint, Bandit, Flake8) automatically every time someone pushes code. If the Pylint score is too low or Bandit finds a high-severity issue, the build would fail, preventing the bad code from being merged.

### 4. What tangible improvements did you observe in the code?

The code improved in four major ways:

* **Security:** It's **much more secure**. Removing the `eval()` call eliminated a medium-severity vulnerability.
* **Robustness:** It's **more robust**. Replacing the bare `except:` and adding `isinstance()` type-checking means the program handles bad data and errors gracefully instead of crashing.
* **Maintainability:** It is **far more maintainable**. Refactoring the code to remove the `global` variable (to fix `W0603`) makes the program much safer, cleaner, and easier to debug or expand later.
* **Readability:** It's **cleaner**. Removing unused imports, fixing all naming conventions, and adding docstrings makes it professional. The Pylint score jumping from **4.80 to a perfect 10/10** proves the quality is significantly higher.
