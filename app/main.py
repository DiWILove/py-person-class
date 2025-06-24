class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_objects = []
    for person_dict in people_list:
        person = Person(name=person_dict["name"], age=person_dict["age"])
        person_objects.append(person)

    for person_dict in people_list:
        name = person_dict["name"]
        current = Person.people[name]

        if "wife" in person_dict and person_dict["wife"] is not None:
            spouse = Person.people[person_dict["wife"]]
            current.wife = spouse
            spouse.husband = current

        elif "husband" in person_dict and person_dict["husband"] is not None:
            spouse = Person.people[person_dict["husband"]]
            current.husband = spouse
            spouse.wife = current

    return person_objects
