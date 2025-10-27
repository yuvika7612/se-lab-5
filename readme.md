# Lab 5: Known Issue Table

[cite_start]This table documents the four priority issues identified by static analysis tools and the approach taken to fix them.

| Issue | Tool | Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `B307` / `W0123` | Bandit / Pylint | Security (Medium) | 59 | `Use of possibly insecure function` / `Use of eval` | **Fixed:** Removed the `eval("print('eval used')")` line entirely from the `main()` function. |
| `W0102` | Pylint | Bug / Warning | 8 | `Dangerous default value [] as argument` | **Fixed:** Changed the function definition to `logs=None`, then added `if logs is None: logs = []` inside the function. |
| `E722` / `W0702` | Flake8 / Pylint | Bug / Error | 19 | `do not use bare 'except'` / `No exception type(s) specified` | **Fixed:** Replaced the bare `except:` with `except KeyError:` to only catch the specific error of a missing item. |
| `F401` / `W0611` | Flake8 / Pylint | Style / Warning | 2 | `'logging' imported but unused` / `Unused import logging` | **Fixed:** Deleted the `import logging` line from the top of the file. |