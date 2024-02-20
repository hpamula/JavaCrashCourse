#Requires AutoHotkey v2.0
^+i:: ; Ctrl + Shift + I
{
    Send("^c")
    Run("Runs_selection_in_Java_with_args.py")
}
return
