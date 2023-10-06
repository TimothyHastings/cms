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
#   TODO: Read the commands from a help.txt file.
#
def display_help():
    print("Help to come")

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

def add_customer(cms, command_line):
    # add first last age
    if len(command_line) == 4:
        customer = Customer()
        customer.first_name = command_line[1]
        customer.family_name = command_line[2]
        customer.age = command_line[3]
        cms.customers.append(customer)
    else:
        print("Invalid arguments")

def find_customer(cms, command_line):
    # find id
    id = int(command_line[1])
    for customer in cms.customers:
        if id == customer.id:
            print("Found")
            return
    print("Not Found")

