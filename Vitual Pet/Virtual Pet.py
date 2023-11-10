# Virtual Pet
from random import randrange

class Pet(object):
    """A Virtual Pet"""
    excitement_reduce = 3
    excitement_max = 10
    excitement_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 3
    vocab = ['"Grrr..."', '"Hello"']

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.food = randrange(self.food_max)
        self.excitement = randrange(self.excitement_max)
        self.vocab = self.vocab[:]

    def __clock_tick(self):
        self.excitement -= 1
        self.food -= 1

    @property
    def mood(self):
        if self.excitement > self.excitement_warning and self.food > self.food_warning:
            return "happy"
        elif self.food < self.food_warning:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        return "\nI'm " + self.name + "." + "\nI feel " + self.mood + "."

    def teach(self, word):
        self.vocab.append(word)
        self.__clock_tick()

    def talk(self):
        print(
            "I'm a",
            self.animal_type,
            " named",
            self.name,
            ".",
            "I feel ",
            self.mood,
            " now.\n"
        )
        self.__clock_tick()

    def feed(self):
        print("***crunch*** \n ...Tasty, thanks!")
        meal = randrange(0, self.food_max)
        self.food += meal

        if self.food < 0:
            self.food = 0
            print("I'm starving!")
        elif self.food > self.food_max:
            self.food = self.food_max
            print("I'm full!")
        self.__clock_tick()

    def play(self):
        print("Woooo!")
        fun = randrange(self.excitement_max)
        self.excitement += fun
        if self.excitement < 0:
            self.excitement = 0
            print("I'm bored...")
        elif self.excitement > self.excitement_max:
            self.excitement = self.excitement_max
            print("I'm happy!")
        self.__clock_tick()

def main():
    pet_name = input("What is your pet's name?")
    pet_type = input("What type of animal are they?")

    # create a new pet
    my_pet = Pet(pet_name, pet_type)

    input(
        "Hello! I'm " +
        my_pet.name +
        " and I'm new around here..." +
        "\nPress enter to start. "
    )

    choice = input("Choice: ")

    while choice != "0":
        print(
            """
            ***INTERACT WITH YOUR PET***

            1 - Feed your pet
            2 - Talk to your pet
            3 - Teach your pet a new word
            4 - Play with your pet
            0 - Quit
            """
        )

        if choice == "0":
            print("Bye!")
        elif choice == "1":
            my_pet.feed()
        elif choice == "2":
            my_pet.talk()
        elif choice == "3":
            new_word = input("What do you want them to learn? ")
            my_pet.teach(new_word)
        elif choice == "4":
            my_pet.play()
        else:
            print("Sorry, you can't do that")

        choice = input("Choice: ")

main()
