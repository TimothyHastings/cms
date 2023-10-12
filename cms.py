class CustomerManagement:
    def __init__(self, name):
        self.name = name
        self.customers = list()
        self.policies = list()
        self.customer_file_name = "customers.csv"
        self.policies_file_name = "policies.csv"

    # Used to print info about an instance.
    def __str__(self):
        return self.name + "\nCustomers: " + str(len(self.customers)) + "\nPolicies: " + str(len(self.customers))

    def save(self, fname):
        f = open(fname, "w")
        for customer in self.customers:
            f.write(customer)
        f.close()
