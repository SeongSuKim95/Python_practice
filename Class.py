class Car:
    # class 생성자
    def __init__(self,name,color): # 생성자의 매개변수 = object의 속성
        self.name = name # member
        self.color = color # member
    # method

    def __del__(self):
        print("Deleting Instance")


    def show_info(self):
        print("이름:", self.name,"/색상:",self.color)

    #Setter
    def set_name(self,name):
        self.name = name

class Unit:
    def __init__(self,name,power):
        self.name = name
        self.power = power

class Monster(Unit):  # Class 상속

    def __init__(self,name,power,type):
        self.name = name
        self.power = power
        self.type = type

    def show_info(self):
        print(self.name)

car1 = Car("소나타","빨간색") #하나의 instance 생성
car1.show_info()

car2 = Car("아반떼","검은색") #또 다른 instance 생성
car2.show_info()

print(car1.name)
print(car2.color)

car1.set_name("아반떼")
print(car1.name)

monster = Monster("슬라임",10,"초급")
monster.show_info()