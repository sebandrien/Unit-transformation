# Python Unit Conversion

An interactive program that repeatedly prompts the user to input a value in feet and converts it into inches. 

The while True: loop ensures the program runs indefinitely, continually asking for input until manually stopped. 

Inside the loop, the program attempts to read the user's input, convert it to an integer, and calculate the equivalent length in inches by multiplying the value by 12. It then prints the calculation and the conversion result. If the user enters an invalid value (non-integer), the except ValueError block catches the error and displays a message asking for an integer input. This provides an easy and user-friendly way to handle invalid inputs without crashing the program.

Output:
```py
Please enter a value in feet: 12
12 * 12 is 144
12 feet is equivalent to 144 inches
. . .
```
```py
Please enter a value in feet: 2
2 * 12 is 24
2 feet is equivalent to 24 inches
. . .
```
```py
Please enter a value in feet: 99
99 * 12 is 1188
99 feet is equivalent to 1188 inches
```
