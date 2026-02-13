import configparser
import json

def Print(msg):
    print(msg)
    return msg

def quit(msg="user requested exit"):
    Print(msg)
    raise SystemExit(msg)

def Exit(msg="Exiting"):
    raise SystemExit(msg)

def loadconfig(type="json", filename="config.json"):
    if type == "json":
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except Exception as e:
            return f"Error loading JSON: {e}"

    elif type == "ini":
        parser = configparser.ConfigParser()
        try:
            parser.read(filename)
            return parser
        except Exception as e:
            return f"Error loading INI: {e}"

    else:
        return f"sorry, we don't support '{type}' yet. please wait till next update."

def writeconfig(type="json", filename="config.json", data=None):
    if data is None:
        return "Error: No data provided to write."

    if type == "json":
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            return f"Error writing JSON: {e}"

    elif type == "ini":
        if not isinstance(data, configparser.ConfigParser):
            return "Error: INI data must be a ConfigParser object."

        try:
            with open(filename, "w") as f:
                data.write(f)
        except Exception as e:
            return f"Error writing INI: {e}"

    else:
        return f"sorry, we don't support '{type}' yet. please wait till next update."