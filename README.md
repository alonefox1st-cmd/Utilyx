# Utilyx V1.0.1

A lightweight Python utility module providing simple helpers for configuration loading, configuration writing, safe exiting, and standardized printing. Designed to be minimal, readable, and easy to drop into any project.

---

---
## Community
- Pull requests are welcome
- Please no slurs
- Please be respectful of others
- No question is too dumb
- I will answer pull requests as soon as I can
- Everyone is welcome, your sexuality/gender/personality will be protected here

---

---
# **updatelog**:
- errorui function with tons of configuration
- loadfile function
- writefile function 
- deletefile function
- clearfile function
- loadfile and writefile has support for most file types
- bugfixes 
- added comments at the start of the file
- clearfile alias
- deletefile alias
- native_error_ui

---

---

# examples:
Print wrapper:
```python
import utilyx
utilyx.Print(str)
```
loadfile:
```python
from utilyx import loadfile #import the function
file_content=loadfile("txt", "logs.txt") #you can use text instead of txt
print(file_content)
```
writefile:
```python
from utilyx import writefile #works the same as config just supports most text files
log=writefile(type="log", filename="logs.log")
```
suggested way to import utilyx and use:
```python
from utilyx import * #imports all modules without requiring utilyx. at the start of calls
Print(str)
config=loadconfig("json", "config.json")#to read JSON files
print(config)
```

---

---

## Installation

```bash
pip install utilyx
```