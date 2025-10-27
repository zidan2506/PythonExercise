
            
class Elevator:
    def __init__(self,bot_f,top_f):
        self.bot_f = bot_f
        self.top_f = top_f
        self.cur_f = bot_f
    def floor_up(self):
        self.cur_f +=1
    def floor_down(self):
        self.cur_f -=1
    def go_to_floor(self,floor):
        reached = False
        while not reached:
            if self.cur_f == floor:
                self.cur_f = floor
                reached = True
                break
            if self.cur_f >floor:
                self.floor_down()
            if self.cur_f < floor:
                self.floor_up()
            if self.cur_f > self.top_f:
                self.cur_f = self.top_f
                break
            if self.cur_f < self.bot_f:
                self.cur_f = self.bot_f
                break
            print(f'The current floor is {self.cur_f}')
class Building:
    def __init__(self,bot_floors,top_floors,elevators):
        self.elevators = []
        self.bot_floors = bot_floors
        self.top_floors = top_floors
        for i in range(elevators):
            self.elevators.append(Elevator(bot_floors,top_floors))
    def run_elevator(self,elevator_number,des):
        print(f'Elevator {elevator_number} is working')
        self.elevators[elevator_number-1].go_to_floor(des)
    def fire_alarm(self):
        print('Fireeee 🔥🔥🔥')
        for ele in range(len(self.elevators)):
            self.run_elevator(ele+1,self.bot_floors)
    def test(self):
        for i in self.elevators:
            print(i)

#Setting
b1 = Building(1,7,3)
#Run
b1.run_elevator(1,7)
b1.run_elevator(2,5)
b1.run_elevator(3,6)
b1.fire_alarm()


# b1.test()