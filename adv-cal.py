from add import add
from sub import sub
from mul import mul
from div import div

def main():
    print("Advanced Calculator")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Operations: add, sub, mul, div")
    choice = input("Enter operation: ")

    if choice == "+":
        print(f"Result: {add(a, b)}")
    elif choice == "-":
        print(f"Result: {sub(a, b)}")
    elif choice == "*":
        print(f"Result: {mul(a, b)}")
    elif choice == "/":
        print(f"Result: {div(a, b)}")
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    main()
