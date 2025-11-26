import sys

def add(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) == 3:
        # Use command-line arguments (for Jenkins parameters)
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        # Use default values if no input provided
        x = 10
        y = 20
    
    print("Sum:", add(x, y))