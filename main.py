while True:
    try:
        ft = int(input("Please enter a value in feet: "))  # Get input from the user and convert it to an integer
        inches = ft * 12  # Convert feet to inches
        print(f"{ft} * 12 is {inches}")
        print(f"{ft} feet is equivalent to {inches} inches")
        print(". . .")
        
    except ValueError:
        print("Invalid input. Please enter an integer value.")
