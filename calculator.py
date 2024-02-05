
# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

def main():
    # enter the two numbers
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")

    # convert the entered value to float value
    num1 = float(a)
    num2 = float(b)

    # execute the two functions
    sum = add(num1, num2)     # sum of two numbers
    difference = subtract(num1, num2)    # difference of two numbers

    # print the values
    print("The sum is: ", sum)
    print("The difference is: ", difference)


if __name__ == "__main__":
    main()
