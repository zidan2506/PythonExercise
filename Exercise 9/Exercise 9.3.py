class Car:
    def __init__(self,regis_num,max_speed,cur_speed=0,trvl_dis=0):
        self.regis_num = regis_num
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.trvl_dis = trvl_dis
    def info(self):
        print(f"The informations of the car:\nRegistation number: {self.regis_num}\nMaximum Speed: {self.max_speed}km/h\nCurrent Speed: {self.cur_speed} km/h\nTravelled Distance: {self.trvl_dis}km\n")
    def accelerate(self,change_speed):
        a=1        
        self.cur_speed = self.cur_speed + change_speed
        if self.cur_speed >= self.max_speed:
            self.cur_speed = self.max_speed
        if self.cur_speed <=0:
            self.cur_speed=0
    def drive(self,time):
        self.trvl_dis = self.trvl_dis + self.cur_speed*time

        # return f"The {self.regis_num} car's current speed is {self.cur_speed} km/h"
        

c1 = Car('ABC-123',142,60,2000)
c1.drive(1.5)
print(c1.trvl_dis)