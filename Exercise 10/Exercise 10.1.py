
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
            
h = Elevator(1,7)
h.go_to_floor(10)
h.go_to_floor(0)



