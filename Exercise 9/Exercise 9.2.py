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
        # return f"The {self.regis_num} car's current speed is {self.cur_speed} km/h"
        

c1 = Car('ABC-123',142)
c1.accelerate(30)
c1.accelerate(70)
c1.accelerate(50)
print(f'The current speed is: {c1.cur_speed}')
c1.accelerate(-200)
print(f'The current speed is: {c1.cur_speed}')
