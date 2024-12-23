class Person:
    """ Class attribute to store instances by their name"""
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # Add the instance to the class-level dictionary
        Person.people[name] = self


def create_person_list(people):
    """
    Converts a list of dictionaries into a list of Person instances,
    linking wife/husband attributes to Person instances.
    """
    """ Clear the class attribute to avoid conflicts with previous data"""
    Person.people.clear()

    """ Create all Person instances"""
    person_instances = [
        Person(person["name"], person["age"])
        for person in people
    ]

    """ Link wife/husband attributes """
    for person in people:
        person_instance = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            person_instance.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            person_instance.husband = Person.people[person["husband"]]

    return person_instances
