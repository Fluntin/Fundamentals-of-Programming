## Word Frequency Analysis

To solve this task, you are required to write a program that reads all the words from a given text file (assumed to exist in the same directory as your program) and removes common words. You have the file "vanligaord.txt" available, which contains commonly occurring words.

Create a text file using a text editor or Notepad. Open your web browser and find a text (e.g., a news article), then select the text, copy it, and paste it into your text editor.
Save the file in the same directory as your Python program with a ".txt" extension.

Here's an example of how the program may run (program output is shown in red, user input is shown in green):
```
Which file would you like to read? katalonien.txt
The text contains 306 words.
Found 134 uncommon words:
Hundratusentals
katalaner
samlas
kräva
självständighet
......many more lines that do not need to be displayed!
Note: The uncommon words are listed, not the common ones.
```

Solution requirements:
- There should be a function that takes a file name as a parameter, reads the file, and returns the words in the file as a list.
- There should be a function that takes two lists (of the same type as mentioned in point 1 above) as parameters and returns a third list that represents the difference between the two lists.

Tips: Since the first lab (L1), global variables are not allowed to be used locally (they should be parameters). To ensure automated correctness checking, make the following change in your program:
```python
def main():
    # Here is your previous main program.
    # Global variables in this section will now become local variables in the main() function,
    # resulting in a "NameError" in functions where you haven't used parameters.

main()
```
