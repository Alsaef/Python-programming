# Initialize an empty stack using a list
stack = []

# Function to push a value onto the stack
def push(value):
    stack.append(value)
    print(f"{value} pushed onto the stack.")

# Function to pop a value from the stack
def pop():
    if not stack:
        print("Stack is empty. Cannot pop.")
        return None
    else:
        value = stack.pop()
        print(f"{value} popped from the stack.")
        return value

# Function to display the contents of the stack
def display_stack():
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack contents:", stack)

while True:
    print("\nMenu:")
    print("1. Push onto Stack")
    print("2. Pop from Stack")
    print("3. Display Stack")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        value = int(input("Enter a value to push onto the stack: "))
        push(value)
    elif choice == 2:
        popped_value = pop()
        if popped_value is not None:
            print("Popped value:", popped_value)
    elif choice == 3:
        display_stack()
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
