    class Animal:
        category = ""
        # class-level default attribute

        def __init__(self, name):
            self.name = name
            # allowing each animal to set a unique name at
            # creation, this is an instance-level attribute

        def set_category(self, category):
            self.category = category
            # setting instance-level attribute category
            # to class-level attribute


class Turtle(Animal):
    # child class of parent class Animal, will
    # inherit everything from parent class Animal
    category = "reptile"
    # setting class-level attribute here will overwrite
    # parent class Animal class-level category attribute


class Snake(Animal):
    category = "reptile"


class Zoo:
    def __init__(self):
        # creating a dictionary to store the animals at instance-level
        self.current_animals = {}

    def add_animal(self, animal):
        """Adding animals to a dict with names as keys and category as
        values. This will be passed in from outside of the class

        Args:
            animal (instance of class Animal): class composition magic
        """
        self.current_animals[animal.name] = animal.category
        # we have full access to attributes and methods via
        # composition and able to see the attributes: name, category

    def total_of_category(self, category):
        # get total number of animals for matched input param,
        # input param will be passed in from outside the class
        result = 0
        for animal in self.current_animals.values():
            # only looping through the values of dict and not keys
            # which is category to check if matches input param
            if animal == category:
                result += 1
        return result


zoo = Zoo()  #create an instance of Zoo class
turtle = Turtle("Turtle")  #create an instance of the Turtle class
snake = Snake("Snake")  #create an instance of the Snake class

zoo.add_animal(turtle)
# add animal to zoo, pay extra attention here as an object of class Turtle
# is being inserted into the method as an argument, this is the perfect
# example of composition as this will enable the class Zoo to have full
# access to everything the turtle object has access to including all
# attributes and methods
zoo.add_animal(snake)
# again same thing is happening here as a perfect example of composition

print(zoo.total_of_category("reptile"))
# total number of animals in this category
