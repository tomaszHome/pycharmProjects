lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 7, 8, 6, 23)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 7, 8, 6, 23)
    # Objects not only have data in the form -f self. but can also methods or actions
    # associated with them

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer('Rolf')
player_one.numbers = (1, 2, 3, 4, 5, 6)
player_two = LotteryPlayer('John')

# print(player_one.numbers == player_two.numbers)
# print(player.name)
# print(player.numbers)
# print(player.total())

##########################


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school(self):
        print("I'm going to {}.".format(self.school))

    @classmethod    # used so that the method can be executed with cls
    def go_to_school(cls):  # cls needs to be added when calling something classmethod
        # we can run Student.go_to_school() as the method is generic for any student
        print("I'm going to school")
        print("I am {}".format(cls))

    @staticmethod  # used so that the method can be executed without argument
    # In this instance we no longer have to specify anna.go_to_school() or rolf.go_to_school()
    # instead we can run Student.go_to_school() as the method is generic for any student
    def go_to_school():
        print("I'm going to school")


anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")
anna.marks.append(56)
anna.marks.append(35)
anna.marks.append(5)
anna.marks.append(3)
# print (anna.marks)
# print (anna.average())
anna.go_to_school()
rolf.go_to_school()

# Exercise code

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        new_store = cls(store.name + " - franchise")    # cls is same as Store
        return new_store

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock price: {}".format(store.name, int(store.stock_price()))