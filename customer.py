ACTIVE = "Active"
SUSPENDED = "Suspended"
INACTIVE = "Inactive"


class Customer:
    # Class variable for unique customer ids
    next_id = 0

    def __init__(self):
        Customer.next_id += 1
        self.id = Customer.next_id
        self.first_name = ""
        self.family_name = ""
        self.age = 0
        self.risk = 0
        self.state = ACTIVE

    def display(self):
        line = str(self.id) + " " + self.first_name + " " + self.family_name + " " + str(self.age) + " " + str(self.risk) + " " + self.state
        print("{}".format(line.strip()))
        #print("Customer: ", self.id, self.first_name, self.family_name, self.age, self.risk, self.state)

    def add(self, fname):
        f = open(fname, "a")
        f.write(str(self.id) + "," + self.first_name + "," + self.family_name + "," + \
                str(self.age) + "," + str(self.risk) + "," + self.state + "\n")
        f.close()

    def update(self, fname):
        pass
