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
    def __init__(self,name,distance,cars):
        self.name = name
        self.distance = distance
        self.cars = []
        for i in cars:
            self.cars.append(i)
    def hour_passes(self):
            for car in self.cars:
                car.accelerate(random.randint(-10,15))
                car.drive(1)
    def print_status(self):
        for car in self.cars:
            car.info()
    def race_finished(self):
        self.condi= False
        for car in self.cars:
            if car.trvl_dis >= self.distance:
                 self.condi = True
        return self.condi
        
#Setting 
cars = []
for i in range(10):
    i = Car(f'ABC-{i+1}',random.randint(100,200))
    cars.append(i)
c = 0
race1 = Race('Grand Demolition Derby',8000,cars)
#Run
while not race1.race_finished():
    c +=1
    race1.hour_passes()
    if c%10 ==0:
        print(f'Hour {c}')

        race1.print_status()
    if race1.race_finished():
        print(f'One of the cars has reached the finish line at hour {c}\n')
        race1.print_status()