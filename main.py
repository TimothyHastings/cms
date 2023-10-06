from cli import command_processor
from cms import CustomerManagement
from customer import Customer


def test_code():
    c1 = Customer()
    c2 = Customer()
    c3 = Customer()

    c1.first_name = "Vasily"
    c2.first_name = "Tim"
    c1.display()
    c2.display()

    print(c1.id)
    print(c2.id)
    print(c3.id)



"""
The main entry point.
"""
if __name__ == '__main__':
    print("Welcome")
    test_code()

    # Create My CMS instance.
    cms = CustomerManagement("My CMS")

    print(cms)

    # Run the command line.
    command_processor(cms)
