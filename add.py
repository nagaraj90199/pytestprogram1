def add(a, b):
    return a + b

if __name__ == "__main__":
    try:
        # Try to take user input
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
    except Exception:
        # If input fails, use default values
        print("Input failed, using default values...")
        x = 10
        y = 20

    print("Sum:", add(x, y))
