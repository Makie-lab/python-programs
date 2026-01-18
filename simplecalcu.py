def show_menu():
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Search Calculation History")
    print("6. Advanced Calculator (expressions)")
    print("7. View Full History")
    print("8. Exit")


def get_operation():
    return int(input("\nChoose an operation (1-8): "))


def get_numbers():
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    return num1, num2


def calculate(operation, num1, num2):
    if operation == 1:
        print("\nYou chose addition!")
        return num1 + num2
    elif operation == 2:
        print("\nYou chose subtraction!")
        return num1 - num2
    elif operation == 3:
        print("\nYou chose multiplication!")
        return num1 * num2
    elif operation == 4:
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return None
        print("\nYou chose division!")
        return num1 / num2


def linear_search(history, target):
    """Search for exact number/operator in history."""
    matches = []
    
    # Normalize target: accept "5" or "5.0" as the same
    try:
        target_num = float(target)
        target_strs = {str(target_num), str(int(target_num))}  # e.g. {"5.0","5"}
    except ValueError:
        # If it's not a number, just search as string (like "+", "-", "*", "/")
        target_strs = {target}
    
    for entry in history:
        # Split entry into tokens (numbers/operators/results)
        tokens = entry.replace("=", "").split()
        for token in tokens:
            if token in target_strs:
                matches.append(entry)
                break  # avoid duplicates if multiple matches in same entry
    
    if matches:
        return "\n".join(matches)
    else:
        return "No matching calculation found."



def advanced_calculator(history):
    print("\n==================================================")
    print("         Advanced Calculator (Expressions)        ")
    print("==================================================")
    print("\nType 'exit' to return to the main menu.")
    print("You can use parentheses and operators (+, -, *, /, **).")

    while True:
        expression = input("\nEnter an expression: ")
        if expression.lower() == "exit":
            print("Returning to main menu...")
            break
        try:
            result = eval(expression, {"__builtins__": None}, {})
            entry = f"{expression} = {result}"
            print("Result:", entry)
            history.append(entry)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except Exception:
            print("Invalid input. Please enter a valid expression.")


def main():
    print("==================================================")
    print("            Welcome to Our Calculator!            ")
    print("==================================================")

    history = []

    while True:
        try:
            show_menu()
            operation = get_operation()

            if operation == 8:
                print("Babush thankyou!")
                break

            if operation < 1 or operation > 8:
                print("Please choose a valid option (1-8).")
                continue

            if operation == 5:
                search_val = input("Enter a number or operator to search in history: ")
                print("Matches found:")
                print(linear_search(history, search_val))
                continue

            if operation == 6:
                advanced_calculator(history)
                continue

            if operation == 7:
                if history:
                    print("\n--- Calculation History ---")
                    for h in history:
                        print(h)
                else:
                    print("History is empty.")
                continue

            # Basic operations (1–4)
            num1, num2 = get_numbers()
            result = calculate(operation, num1, num2)

            if result is not None:
                entry = f"{num1} {['+','-','*','/'][operation-1]} {num2} = {result}"
                print("Result:", entry)
                history.append(entry)

        except ValueError:
            print("Invalid input. Please enter numbers only.")


main()
