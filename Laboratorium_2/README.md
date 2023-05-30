## Length Jump Competition

For a long jump competition, you want to save the values of the jumpers' results to later calculate statistics. The program should have the following dialogue:

### Menu 1 - Enter the competitors' results

```
Menu
1 - Enter the competitors' results.
2 - View statistics for previously entered results.
3 - Exit

Your choice: 1
Number of competitors: 10
Enter the result for participant 1: 8.16
Enter the result for participant 2: 7.48
Enter the result for participant 3: .........
```

### Menu 2 - View statistics for previously entered results

```
Menu
1 - Enter the competitors' results.
2 - View statistics for previously entered results.
3 - Exit

Your choice: 2
The average is 8.01m with a standard deviation of 0.56m.
The highest value was 8.16m, and the lowest was 7.13m.
```

To calculate the standard deviation, you can use the "statistics" module. Check which functions are available in this module (compare with how we used the "math" module).

The following are the requirements for the program:
- It should have a function named "input_data()" and a function named "statistics()" with appropriate parameters and optional return values.
- The main program should handle the menu selection. This example involves practicing conditionals and loops.
- Do not use a separate variable for each jump result.

Considerations: The "input_data()" function should not perform any output of results (menu option 2), but it should handle the following tasks: input, type conversion, and return value. This lab aims to practice control structures and conditions using while loops, for loops, "in" keyword, "range()", "len()", "if" statements, "break" keyword, and lists.
