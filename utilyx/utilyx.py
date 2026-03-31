import configparser #imports what's required for config parsers
import json #imports the dep for loading JSON files
import os #for file operations such as delete_file
import tkinter as tk #imports what's required for gui
import sys
#============logic============

def Print(msg): #makes it easy for new devs so it doesn't matter if they forget python is cap sensitive
    print(msg)
    return msg

def quit(msg="user requested exit"):
    Print(msg)
    raise SystemExit(msg)

def Exit(msg="Exiting"): #makes it easy for new devs so it doesn't matter if they forget python is cap sensitive
    raise SystemExit(msg)

def loadconfig(type="json", filename="config.json"): #loads configs
    if type == "json": #if the str==JSON it will load JSON and if otherwise pass
        try:
            with open(filename, "r") as f: #opens the JSON file
                return json.load(f)  #returns and reads the file content
        except Exception as e: #catches errors so there not fatal
            return f"Error loading JSON: {e}"

    elif type == "ini": #if the str==ini it will load ini and if otherwise pass
        parser = configparser.ConfigParser() #not required just makes it easy on me
        try:
            parser.read(filename) #reads the file
            return parser #returns the content of the read file
        except Exception as e: #catches errors so there not fatal
            return f"Error loading INI: {e}"

    else:
        return f"sorry, we don't support '{type}' yet. please wait till next update."
def load_config(type="json", filename="config.json"):
    loadconfig(type, filename)

def writeconfig(type="json", filename="config.json", data=None): #writes configs
    if data is None:
        return "Error: No data provided to write."

    if type == "json":
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=4) #dumps the given data in the specified JSON file
        except Exception as e:
            return f"Error writing JSON: {e}"

    elif type == "ini":
        if not isinstance(data, configparser.ConfigParser):
            return "Error: INI data must be a ConfigParser object."

        try:
            with open(filename, "w") as f:
                data.write(f) #self-explanatory
        except Exception as e:
            return f"Error writing INI: {e}"

    elif type=="txt":
        print("please use utilyx.writefile(or writefile if your using import *)")
        return f"please use utilyx.writefile(or writefile if your using import *)"

    else:
        return f"sorry, we don't support '{type}' yet. please wait till next update."
def write_config(type="json", filename="config.json", data=None):
    writeconfig(type, filename, data)

#----------------------------------------------------------------------------------------------------------
#                     end of comments sorry it makes it harder personally for me to code
#----------------------------------------------------------------------------------------------------------
def clear_file(filename):
    f = open(filename, "w")
    f.write("")
    f.close()

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

def writefile(type="txt", filename="logs.txt", data=None):
    if type == "txt":
        with open(filename, "a") as f:
            f.write(data)
            return f"Successfully wrote content to {filename}"

    elif type == "text":
        print("this is a supported way but you can use txt instead")
        with open(filename, "a") as f:
            f.write(data)
            return f"Successfully wrote content to {filename}"


    elif type == "":
        print("please choose a file type")
        return f"please choose a file type"

    elif type == "json":
        writeconfig(type="json", filename=filename, data=data)

    elif type == "ini":
        writeconfig(type="ini", filename=filename, data=data)

    else:
        try:
            with open(filename, "a") as f:
                try:
                    f.write(data)
                except Exception as e:
                    print("error writing to file, maybe its binary:")
        except:
            errorui(message="ERROR code is:80040265(unknown or unreadable file) we cant read this file", error_code="80040265")
            return f"sorry, we don't support '{type}' yet. please wait till next update."
def write_file(type="txt", filename="logs.txt", data=None):
    return writefile(type, filename, data)

def loadfile(type="txt", filename="logs.txt"):
    if type == "txt":
        with open(filename, "r") as f:
            return f.readlines()

    if type == "text":
        with open(filename, "r") as f:
            return f.readlines()

    if type == "":
        print("please choose a file type")
        return f"please choose a file type"

    elif type == "json":
        loadconfig(type="json", filename=filename)

    elif type == "ini":
        loadconfig(type="ini", filename=filename)

    else:
        try:
            with open(filename, "r") as f:
                return f.readlines()
        except exception():
            errorui(message="ERROR code is:80040265(unknown and unreadable file) we cant read this file", error_code="80040265")
            return f"sorry, we don't support '{type}' yet. please wait till next update."
def load_file(type="txt", filename="logs.txt"):
    return loadfile(type, filename)

def errorui(error_code=1, message="UtilyX_Default", message_font="Arial", message_font_size=12, button_font="Arial", button_font_size=12, button_highlight_background="black", button_highlight_color="green", button_active_background="blue", button_active_foreground="white",button_disabledfg="gray", button_fg="black", button_bg="lightgray", bgcolor="red", fgcolor="black", uiheight_resize=True, uiwidth_resize=True, windowsize="500x300"):
    def on_button_click():
        root.destroy()
        exit(error_code)
    if message == "UtilyX_Default":
        message =f"Hay, we've ran into a unexpected error ({error_code}), close this window to end the task."
    else:
        pass
    root=tk.Tk()
    root.geometry(windowsize)
    root.configure(background=bgcolor)
    root.resizable(width=uiwidth_resize, height=uiheight_resize)
    root.title(f"ERROR: {error_code}")

    tk.Label(root, text=message, fg=fgcolor, bg=bgcolor, font=(message_font, message_font_size)).pack()
    tk.Button(root,
                   text="Close",
                   command=on_button_click,
                   activebackground=button_active_background,
                   activeforeground=button_active_foreground,
                   anchor="center",
                   bd=3,
                   bg=button_bg,
                   cursor="hand2",
                   disabledforeground=button_disabledfg,
                   fg=button_fg,
                   font=(button_font, button_font_size),
                   height=2,
                   highlightbackground=button_highlight_background,
                   highlightcolor=button_highlight_color,
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100).place(rely=0.90, relwidth=1, relheight=0.1)
    root.mainloop()
def error_ui(error_code=1, message="UtilyX_Default", message_font="Arial", message_font_size=12, button_font="Arial", button_font_size=12, button_highlight_background="black", button_highlight_color="green", button_active_background="blue", button_active_foreground="white", button_disabledfg="gray", button_fg="black", button_bg="lightgray", bgcolor="red", fgcolor="black", uiheight_resize=True, uiwidth_resize=True, windowsize="500x300"):
    errorui(error_code=error_code, message=message, message_font=message_font, message_font_size=message_font_size, button_font=button_font, button_font_size=button_font_size, button_highlight_background=button_highlight_background, button_highlight_color=button_highlight_color, button_active_background=button_active_background, button_active_foreground=button_active_foreground, button_disabledfg=button_disabledfg, button_fg=button_fg, button_bg=button_bg, bgcolor=bgcolor, fgcolor=fgcolor, uiheight_resize=uiheight_resize, uiwidth_resize=uiwidth_resize, windowsize=windowsize)

def native_error_ui(error_message="UtilyX_Default", error_code=1):
    if error_message == "UtilyX_Default":
        error_message = f"Hay, we've ran into a unexpected error ({error_code}), close this window to end the task."
    import PySide6

    def on_exit_pressed():
        raise SystemExit(error_code)

    from PySide6.QtWidgets import QApplication, QWidget, QTextBrowser, QToolButton
    from PySide6.QtUiTools import QUiLoader
    from PySide6.QtCore import QFile

    app = QApplication([])

    loader = QUiLoader()
    file = QFile("error_better.ui")
    file.open(QFile.ReadOnly)
    window = loader.load(file)
    file.close()

    window.setWindowTitle(f"ERROR: {error_code}")

    exit_button = window.findChild(QToolButton, "exit_button")
    errormsg = window.findChild(QTextBrowser, "error_msg")

    exit_button.clicked.connect(on_exit_pressed)
    errormsg.setText(error_message)

    window.show()
    app.exec()
def nativeerrorui(error_message="UtilyX_Default", error_code=1):
    return native_error_ui(error_message="UtilyX_Default", error_code=1)
        