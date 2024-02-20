# #Requires AutoHotkey v2.0
# ^+i:: ; Ctrl + Shift + I
# {
#     Send("^c")
#     Run("Runs_selection_in_Java_with_args.py")
# }
# return

import pyperclip
import re
import subprocess
import os
import math

directory_path = os.getcwd()
os.chdir(directory_path)
powershell_command = f"rm *.java; rm *.class"
print(powershell_command)
subprocess.run(["powershell", powershell_command], check=True)

clipboard_content = pyperclip.paste()

def save_content(name, content):
    lines = content.splitlines()
    for i, line in enumerate(lines, start=1):
        spaces = " "*(math.floor(math.log10(len(lines)))-math.floor(math.log10(i))+1)
        print(f"{i}{spaces}{line}")
    file_name = f"{name}.java"
    file_path = os.path.join(directory_path, file_name)
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(content.replace('\r\n', '\n'))
    print(f"File saved as {file_path}")
def extract_and_save_definitions(content):
    global lastClass
    pattern = r'public\s+(class|interface|record)\s+(\w+)'
    matches = list(re.finditer(pattern, content))
    for i, match in enumerate(matches):
        start = match.start() if i > 0 else 0
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        name = match.group(2)
        save_content(name, content[start:end])
        if match.group(1) == 'class':
            lastClass = name
extract_and_save_definitions(clipboard_content)
powershell_command = f"javac {lastClass}.java; java {lastClass} @($(read-host 'Args for Java program') -split '\s+'); read-host\n"
print(powershell_command)
subprocess.run(["powershell", powershell_command], check=True)
print("Java program compiled and executed successfully.")
