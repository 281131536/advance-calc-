from add import add
from sub import subtract
from mul import multiply
from div import divide

def main():
    print("Advanced Calculator")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Operations: add, sub, mul, div")
    choice = input("Enter operation: ")

    if choice == "add":
        print(f"Result: {add(a, b)}")
    elif choice == "sub":
        print(f"Result: {subtract(a, b)}")
    elif choice == "mul":
        print(f"Result: {multiply(a, b)}")
    elif choice == "div":
        print(f"Result: {divide(a, b)}")
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    main()
