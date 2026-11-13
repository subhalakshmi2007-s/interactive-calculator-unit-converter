CONVER = {"km_to_m": 0.621371,"kg_to_p": 2.20462}

def read_num(p):
    while True:
        try:
            num= float(input(p))
            return num
        except ValueError:
            print("Invalid input! Please enter a number.")

def km_to_miles(km):
    return km * CONVER["km_to_m"]

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def kg_to_pounds(kg):
    return kg * CONVER["kg_to_p"]


def unit_converter():
    while True:
        print("\n----- UNIT CONVERTER -----")
        print("1. KM to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. KG to Pounds")
        print("4. Back to Main Menu")
        choice = input("Choose conversion: ")
        if choice == "1":
            km = read_num("Enter kilometers: ")
            print("Miles:", km_to_miles(km))
        elif choice == "2":
            c = read_num("Enter Celsius: ")
            print("Fahrenheit:", celsius_to_fahrenheit(c))
        elif choice == "3":
            kg = read_num("Enter kilograms: ")
            print("Pounds:", kg_to_pounds(kg))
        elif choice == "4":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice! Please select 1 to 4.")

def main():
    while True:
        print("\n----- INTERACTIVE CALCULATOR -----")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Unit Converter")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "6":
            print("Thank you for using calculator!")
            break
        elif choice in ("1", "2", "3", "4"):
            a = read_num("Enter first number: ")
            b = read_num("Enter second number: ")
            if choice == "1":
                print("Result:", a + b)
            elif choice == "2":
                print("Result:", a - b)
            elif choice == "3":
                print("Result:", a * b)
            elif choice == "4":
                if b == 0:
                    print("Cannot divide by zero!")
                else:
                    print("Result:", a / b)
        elif choice == "5":
            unit_converter()
        else:
            print("Invalid choice! Please select 1 to 6.")
if __name__ == "__main__":
    main()