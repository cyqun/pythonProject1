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
    with open("animal.yml",encoding='utf-8') as yl:
        animal_data = yaml.load(yl)
    cat = Cat(**animal_data["Cat"])
    print(f"猫的姓名：{cat.name}，颜色：{cat.color}，年龄：{cat.age}岁，性别：{cat.gender}，毛发：{cat.hair}")
    cat.catch()
    dog = Dog(**animal_data["Dog"])
    print(f"狗的姓名：{dog.name}，颜色：{dog.color}，年龄：{dog.age}岁，性别：{dog.gender}，毛发：{dog.hair}")
    dog.housekeeping()
