available_tables = ['Table 1', 'Table 2', 'Table 3', 'Table 4', 'Table 5', 'Table 6']
table_assignments = {}
table_customers = {}
table_orders = {}

def read_login_credentials(file_name):
    credentials = {}
    with open(file_name, 'r') as file:
        for line in file:
            username, password = line.strip().split(',')
            credentials[username] = password
    return credentials

def validate_login(credentials, username, password):
    if username in credentials and credentials[username] == password:
        return True
    return False

def assign_table(username, table):
    print("Assign Table")
    # Implement the logic to assign a table to a customer
    available_tables.remove(table)
    table_assignments[username] = table

    if table not in table_customers:
        table_customers[table] = 0

    print(f"{table} has been assigned to {username}.")

    num_customers = int(input("Enter the number of customers for this table: "))
    table_customers[table] = num_customers
    print('GGGGGGGGGGGGGGG')
    print(table_customers)
    print(f"{table} has {num_customers} customers.")

def show_assigned_tables(username):
    tables = [table for table, waiter in table_assignments.items() if waiter == username]
   # print(f"Tables assigned to {username}:")
   # for table in tables:
   #     print(table)

def change_customers(username):
    show_assigned_tables(username)
    table = input("Select the table you want to change the number of customers for: ")
    if table in table_customers:
        num_customers = int(input(f"Enter the new number of customers for {table}: "))
        table_customers[table] = num_customers
        print(f"Table {table} now has {num_customers} customers.")
        show_assigned_tables(username)
    else:
        print(f"{table} is not assigned to {username}.")

def add_to_order(username):
    print("Add to Order")
    # Implement the logic to add items to the order

    table = table_assignments.get(username)
    if table:
        order = input(f"Enter the order for {table}: ")
        table_orders[table].append(order)
        print(f"Order '{order}' added for table {table}.")
    else:
        print(f"{username} is not assigned to any table.")

def prepare_bill():
    print("Prepare Bill")
    # Implement the logic to prepare the bill for the table

def complete_sale():
    print("Complete Sale")
    # Implement the logic to complete the sale and finalize the transaction

def cash_up():
    print("Cash Up")
    # Implement the logic to calculate the cash-up or closing balance


def show_available_tables():
    print("Available Tables:")
    for table in available_tables:
        print(table)

# Main function
def main():
    login_file = 'Login.txt'
    credentials = read_login_credentials(login_file)

    username = input("Enter username: ")
    password = input("Enter password: ")

    if validate_login(credentials, username, password):
        print("Login successful!")

        # The following code displays the menu
        
        while True:
        # Display the menu options
            print("Menu:")
            print("1. Assign Table")
            print("2. Change Customers")
            print("3. Add to Order")
            print("4. Prepare Bill")
            print("5. Complete Sale")
            print("6. Cash Up")
            print("0. Log Out")

            choice = input("Enter your choice: ")

            if choice == "1":
                show_available_tables()

                if len(available_tables) == 0:
                    print("No tables available.")
                else:
                    selected_table = input("Select a table: ")
                    if selected_table in available_tables:
                        assign_table(username, selected_table)
                    else:
                        print("Invalid table selection.")
            elif choice == "2":
                change_customers(username)
            elif choice == "3":
                add_to_order(username)
            elif choice == "4":
                prepare_bill()
            elif choice == "5":
                complete_sale()
            elif choice == "6":
                cash_up()
            elif choice == "0":
                print("Logging out...")
                main()
            else:
                print("Invalid choice. Please try again.")

    else:
        print("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()