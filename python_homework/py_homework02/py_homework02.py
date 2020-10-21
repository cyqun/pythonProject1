# coding=utf-8
import yaml

# 创建一个类（Animal）
class Animal:

    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.gender = sex

    def call(self):
        print("I can call")

    def run(self):
        print("I can run")


class Cat(Animal):
    def __init__(self, name, color, age, sex, hair="short hair"):
        super(Cat, self).__init__(name, color, age, sex)
        self.hair = hair

    def call(self):
        print("the cat can '喵喵叫'")

    def catch(self):
        print("the cat can catch mice")


class Dog(Animal):
    def __init__(self, name, color, age, sex, hair="long hair"):
        super(Dog, self).__init__(name, color, age, sex)
        self.hair = hair

    def call(self):
        print("the dog can '汪汪叫'")

    def housekeeping(self):
        print("the dog can housekeeping")


if __name__ == '__main__':
    with open("animal.yml") as yl:
        animal_data = yaml.load(yl)
    cat = Cat(animal_data[0]['cat']['name'], animal_data[0]['cat']['color'], animal_data[0]['cat']['age'], animal_data[0]['cat']['sex'])
    cat.catch()
    dog = Dog(animal_data[1]['dog']['name'], animal_data[1]['dog']['color'], animal_data[1]['dog']['age'], animal_data[1]['dog']['sex'])
    dog.housekeeping()
