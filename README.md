# JavaCrashCourse

Just open JavaCrashCourse.md file in any markdown editor (github works as well).
There is also helper functionality of quickly running code snippets implemented in `runSnippetFromKeyboardShortcut` directory. To use it you have to:
- download that directory
- have JDK installed with `java` and `javac` added to PATH
- on Windows download autohotkey from https://www.autohotkey.com/
- on other OS write script which triggers Python codes inside directory with e. g. keyboard shortcut

Autohotkey makes it possible to compile and run java:
- without arguments with `ctrl+shift+j` shortcut
- with arguments with `ctrl+shift+i` shortcut
<br>To use it select or copy code snippet and then press keyboard shortcut.
You can change shortcuts by editing `.ahk` text files.

Issues:
<br>It shouldn't be too troublesome for simple snippets, but:<br>
Python creates separate files for every public class, interface or record, but separates them by beginnings of their declaration, which makes all imports under first public class/interface/record don't work for classes below. To completely avoid it use only one public class/interface/record or improve Python codes:)
