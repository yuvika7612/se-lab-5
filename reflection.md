# Lab 5: Static Analysis Reflection

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

* **Easiest:** The easiest fixes were the `F401: unused import logging` and the `B307: use_of_eval`. The tools told me exactly what was wrong, and the fix was just to delete the bad lines of code.

* **Hardest:** The hardest to understand was the `W0102: Dangerous default value []` (the `logs=[]` bug). It wasn't a simple syntax error; I had to understand *why* a list is a problem as a default argument. The `TypeError` crash was also tricky because the static tools didn't catch it, and I had to fix it by adding manual type checking.

### 2. Did the static analysis tools report any "false positives"?

Yes, Pylint reported `W0603: Using the global statement` for `global stock_data`. While using `global` isn't ideal, the lab's small program requires it to function. A proper fix would mean redesigning the whole program, so I consider this a "false positive" or at least a low-priority warning for this specific lab.

### 3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate them in two main ways:

* **1. Local Development (Pre-commit Hooks):** I'd use a tool like `pre-commit` to automatically run Flake8 and Bandit every time I try to `git commit`. This would stop any style errors or security issues from ever getting into the repository.
* **2. Continuous Integration (GitHub Actions):** For a team project, I'd set up a GitHub Action to run all three tools (Pylint, Bandit, Flake8) automatically every time someone pushes code. If the Pylint score is too low or Bandit finds a high-severity issue, the build would fail, preventing the bad code from being merged.

### 4. What tangible improvements did you observe in the code?

The code improved in three major ways:

* **Security:** It's **much more secure**. [cite_start]Removing the `eval()` call eliminated a medium-severity vulnerability[cite: 3].
* **Robustness:** It's **more robust and less buggy**. [cite_start]Replacing the bare `except:` [cite: 1] with `except KeyError:` means the program won't hide unrelated bugs. Fixing the `TypeError` crash means the program can now handle bad input without crashing.
* **Readability:** It's **cleaner**. [cite_start]Removing unused imports [cite: 7] and fixing formatting makes the code easier for another developer to read. The Pylint score jumping from 4.80 to 8.87 proves the quality is much higher.