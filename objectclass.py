class Person(object):
    def __init__(self, name, email, phone, friends, greeting_count):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends
        self.greeting_count = greeting_count

    def greet(self, other_person):
        print ('Hello %s, I am %s!' % (other_person.name, self.name))

    def print_contact_info (self):
        print(self.name, self.email, self.phone)

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friend(self):
        print (len(self.friends))

    def _repr_(self):
        return '' % (self.name, self.email, self.phone)

class Sonny(Person):
    def __init__(self, name, email, phone, friends, greeting_count):
        super().__init__(name, email, phone, friends, greeting_count)

    def greet(self):
        print("Greetings, Jordan!")

class Jordan(Person):
    def __init__(self, name, email, phone, friends, greeting_count):
        super().__init__(name, email, phone, friends, greeting_count)
    def greet(self):
        print("Greetings, Sonny!")

sonny = Sonny("Sonny", "sonny@hotmail.com" , "483-485-4948", [], 0)
jordan = Jordan("Jordan", "jordan@aol.com" , "495-586-3546", [], 0)
sonny.greet()
jordan.greet()
sonny.print_contact_info()
jordan.print_contact_info()
jordan.friends.append(sonny)
sonny.friends.append(jordan)
print(len(jordan.friends))
print(jordan.friends)
sonny.add_friend(jordan)
jordan.add_friend(sonny)
print(jordan.friends)
print(sonny.friends)
jordan.num_friend()
sonny.num_friend()

if jordan.greet():
     jordan.greeting_count == jordan.greeting_count + 1
else:
     jordan.greeting_count == jordan.greeting_count
jordan.greet()
print(jordan.greeting_count)

if sonny.greet():
     sonny.greeting_count == 1
sonny.greet()
print(sonny.greeting_count)

print(jordan._repr_())
print(sonny._repr_())

#Create a class vehicle
class Vehicle (object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.make, self.model, self.year )

car = Vehicle("Nissan" , "Leaf" , "2015")
print(car.make)
car.print_info()