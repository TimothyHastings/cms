from customer import Customer


def command_processor(cms):
    while True:
        line = input("> ")
        command_line = line.split(" ")
        command = command_line[0].lower()
        if command == "exit":
            print("Bye")
            exit(0)
        elif command == "help":
            display_help()
        elif command == "info":
            print(cms)
        elif command == "load":
            load_customers(cms, "customers.csv")
        elif command == "list":
            list_customers(cms, command_line)
        # Add commands here
        elif command == "add":
            add_customer(cms, command_line)
        elif command == "find":
            find_customer(cms, command_line)
        else:
            print("Invalid Command")

#
#   Read the commands from a help.txt file.
#
def display_help():
    fn = open('help.txt', 'r')
    lines = fn.readlines()

    # Strips the newline character
    for line in lines:
        print("{}".format(line.strip()))

#
#   TODO: List n customers and their policies. If n not provided list them all.
#
def list_customers(cms, command_line):
    # list n

    """
    n = 0
    if len(command_line) == 2:
        n = command_line[1]
        n = int(len(cms.customers))
   """
    # print(n)

    for customer in cms.customers:
        customer.display()

#
#   Add a new customer and append it to the csv file.
#
def add_customer(cms, command_line):
    # Add first name, last name and age.
    if len(command_line) == 4:
        customer = Customer()
        customer.first_name = command_line[1]
        customer.family_name = command_line[2]
        customer.age = command_line[3]
        cms.customers.append(customer)
        # Append the customer to the csv file
        customer.add(cms.customer_file_name)
    else:
        print("Invalid arguments")

#
#   Find customer by id.
#   TODO: find by other attributes
#
def find_customer(cms, command_line):
    # find id
    id = int(command_line[1])
    for customer in cms.customers:
        if id == customer.id:
            print(customer)
            return
    print("Not Found")

#
#   Load customers from a csv file.
#   TODO: handle error conditions.
#
def load_customers(cms, fname):
    f = open(fname, "r")
    Lines = f.readlines()
    max_id = 0
    for line in Lines:
        data = line.split(",")
        # Create a customer
        customer = Customer()
        customer.id = int(data[0])
        customer.first_name = data[1]
        customer.family_name = data[2]
        customer.age = int(data[3])
        customer.risk = int(data[4])
        customer.state = data[5]

        # Add the customer to the customer list
        cms.customers.append(customer)

        if customer.id > max_id:
            max_id = customer.id

    # Adjust the Customer next_id
    Customer.next_id = max_id + 1
    print(Customer.next_id)