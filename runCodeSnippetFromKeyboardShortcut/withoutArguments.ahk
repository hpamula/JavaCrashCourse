#Requires AutoHotkey v2.0
^+j:: ; Ctrl + Shift + J
{
    Send("^c")
    Run("Runs_selection_in_Java.py")
}
return
