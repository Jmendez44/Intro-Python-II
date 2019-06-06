

# Encapsulation - every object needs some sort of external-facing API in order to manipulate itd internal state

# Inheritance - allows us to leverage pre-existing code that exists on a base class
# Explicitly forms an object hierarchy

# Polymorphism

# In Python, you should use dictionaries to store key-value pairs

# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    # constructor
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name},{self.description}"
