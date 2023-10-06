class CustomerManagement:
    def __init__(self, name):
        self.name = name
        self.customers = list()
        self.policies = list()

    # Used to print info about an instance.
    def __str__(self):
        return self.name + "\nCustomers: " + str(len(self.customers)) + "\nPolicies: " + str(len(self.customers))


"""
    def get_info(self):
        return self.name + "\nCustomers: " + str(len(self.customers)) + "\nPolicies: " + str(len(self.customers))
"""
