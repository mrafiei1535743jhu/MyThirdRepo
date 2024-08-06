import argparse
from utilities import * 

def main():
    
    args = myargs()
    
    # Create an instance of the Calculator class
    calculator = Calculator(args.num1, args.num2)

    # Perform the operation
    if args.operation == "add":
        result = calculator.add()
    elif args.operation == "subtract":
        result = calculator.subtract()
    elif args.operation == "multiply":
        result = calculator.multiply()
    elif args.operation == "divide":
        try:
            result = calculator.divide()
        except ValueError as e:
            print(e)
            return

    # Print the result
    print(f"The result of {args.operation}ing {args.num1} and {args.num2} is: {result}")

if __name__ == "__main__":
    main()
