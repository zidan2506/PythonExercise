import random

class Car:
    def __init__(self,regis_num,max_speed,cur_speed=0,trvl_dis=0):
        self.regis_num = regis_num
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.trvl_dis = trvl_dis
    def info(self):
        print(f"The informations of the car:\nRegistation number: {self.regis_num}\nMaximum Speed: {self.max_speed}km/h\nCurrent Speed: {self.cur_speed} km/h\nTravelled Distance: {self.trvl_dis}km\n")
    def accelerate(self,change_speed):
        self.cur_speed = self.cur_speed + change_speed
        if self.cur_speed >= self.max_speed:
            self.cur_speed = self.max_speed
        if self.cur_speed <=0:
            self.cur_speed=0
    def drive(self,time):
        self.trvl_dis = self.trvl_dis + self.cur_speed*time
class Race:
    def __init__(self,time):
        self.cars = []
        self.time = time
    def add(self,car):
        self.cars.append(car)
    def info_race(self):
        for index,car in enumerate(self.cars):
            print(f'{index}. {car.info()}')
    def start(self):
        i = 0
        condi = False
        while not condi:
            i+=1
            print(f'Race {i}')
            for car in self.cars:
                car.accelerate(random.randint(-10,15))
                car.drive(1)
                car.info()
                if car.trvl_dis >=10000:
                    condi=True

#Setting & Run
race1 = Race(2)
for i in range(10):
    i = Car(f'ABC-{i+1}',random.randint(100,200))
    race1.add(i)
race1.start()