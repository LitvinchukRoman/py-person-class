class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = []
    for person in people:
        personality = Person(person["name"], person["age"])

        if "wife" in person and person["wife"] is not None:
            personality._wife_name = person["wife"]
        if "husband" in person and person["husband"] is not None:
            personality._husband_name = person["husband"]
        person_list.append(personality)

    for person in person_list:
        if hasattr(person, "_wife_name"):
            wife_obj = Person.people.get(person._wife_name)
            if wife_obj is not None:
                person.wife = wife_obj
            del person._wife_name
        if hasattr(person, "_husband_name"):
            husband_obj = Person.people.get(person._husband_name)
            if husband_obj is not None:
                person.husband = husband_obj
            del person._husband_name

    return person_list
