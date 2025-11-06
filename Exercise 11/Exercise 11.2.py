import random
class Car:
    def __init__(self,regis_num,max_speed,cur_speed=0,trvl_dis=0):
        self.regis_num = regis_num
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.trvl_dis = trvl_dis
    def info(self):
        print(f"The informations of the car:\nRegistration number: {self.regis_num}\nMaximum Speed: {self.max_speed}km/h\nCurrent Speed: {self.cur_speed} km/h\nTravelled Distance: {self.trvl_dis}km")
    def accelerate(self,change_speed):
        self.cur_speed = self.cur_speed + change_speed
        
    def drive(self,time):
        self.trvl_dis = self.trvl_dis + self.cur_speed*time


class Electric_cars(Car):
    def __init__(self,regis_num,max_speed,c_battery):
        super().__init__(regis_num,max_speed)
        self.c_battery = c_battery

    def info(self):
        print('Electric car🔋')
        super().info()
        print(f'Capacity of battery: {self.c_battery} kWh\n')
class Gasoline_cars(Car):
    def __init__(self,regis_num,max_speed,v_tank):
        super().__init__(regis_num,max_speed)
        self.v_tank = v_tank
    def info(self):
        print('Gasoline car ⛽')
        super().info()
        print(f'Volume of tank: {self.v_tank} Liters\n')

#Setup
e1 = Electric_cars('ABC-15',180,52.5)
g1 = Gasoline_cars('ACD-123',165,32.3)

#Run
e1.accelerate(70)
g1.accelerate(90)
e1.drive(3)
g1.drive(3)
e1.info()
g1.info()


        

        
    
        