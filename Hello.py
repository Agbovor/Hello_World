print("Hello World")
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"Hi, I'm {self.name}, a {self.age}-year-old {self.gender}."

    def celebrate_birthday(self):
        self.age += 1
        return f"Happy birthday to {self.name}! You are now {self.age} years old."

    def change_name(self, new_name):
        self.name = new_name
        return f"Name changed to {self.name}."

    def show_name(self):
        return self.name

# Creating instances of the Person class
person1 = Person("Luciana", 25, "female")
person2 = Person("Samson", 30, "male")

# Using the methods of the Person class
print(person1.introduce())
print(person2.introduce())

print(person1.celebrate_birthday())
print(person2.celebrate_birthday())

person1.change_name("Lucy")
print(person1.show_name())

# Creating multiple people and storing them in a list
people = [
    Person("Alice", 22, "female"),
    Person("Bob", 28, "male"),
    Person("Eve", 35, "female"),
    Person("Charlie", 42, "male"),
    Person("Diana", 29, "female")
]

# Using a loop to display all the names of the people
for person in people:
    print(person.show_name())
