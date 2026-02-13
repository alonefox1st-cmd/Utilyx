Utilyx
A lightweight Python utility module providing simple helpers for configuration loading, configuration writing, safe exiting, and standardized printing. Designed to be minimal, readable, and easy to drop into any project.

🚀 **Features**
- Unified Print wrapper for consistent output
- Graceful exit helpers (quit and Exit)
- Config loader supporting:
- JSON
- INI
- Config writer supporting:
- JSON
- INI
- Clean error messages instead of raw exceptions

📦 **Installation**
pip install utilyx

🧰 **Usage**
Importing
import utilyx

or if you dont want to do utilyx.{module_name}
from utiltyx import *



🖨️ **Printing**
from utilyx import Print

Print("Hello, world!")



❌ **Exiting**
from utilyx import quit, Exit

quit("User requested exit")   # Prints message, then exits
Exit("Fatal error")           # Exits without printing



📥 **Loading Config Files**
Load JSON
from utilyx import loadconfig

config = loadconfig("json", "config.json")
print(config)


Load INI
config = loadconfig("ini", "settings.ini")
print(config["Section"]["key"])



📤 **Writing Config Files**
**Write JSON**
from utilyx import writeconfig

data = {"name": "Utilyx", "version": 1}
writeconfig("json", "config.json", data)


**Write INI**
import configparser
from utilyx import writeconfig

parser = configparser.ConfigParser()
parser["App"] = {"debug": "true"}

writeconfig("ini", "settings.ini", parser)

📄 **License**
MIT License
