#8x8
#list of 8 lists
'''
0 1 2 3 4 5 6 7 
8 9 10 11. . . .
'''
class Board():
    def __init__(self):
        self.spot = ['.']*64
        self.turn = 'x'
        def set_row(y, value):
            for x in range(8):
                if (((x + y)%2)==0):
                    self.set(x,y,value)

        for y in [0, 1, 2]:
            set_row(y, 'o')
        for y in [5, 6, 7]:
            set_row(y, 'x')
    def change_turns(self):
        if self.turn == 'x':
            self.turn = 'o'
        else:
            self.turn = 'x'

    def move(self, old_x, old_y, new_x, new_y):
        if not self.is_valid_move(old_x, old_y, new_x, new_y):
            print("Not Valid Move")
            return
        value = self.get(old_x, old_y)
        self.set(new_x, new_y, value)
        self.set(old_x, old_y, '.') 
        self.change_turns()

    def is_valid_move(self, old_x, old_y, new_x, new_y):
        if False == self.is_within_bounds(old_x, old_y):
            print("chosen piece does not exist in bounds")
            return False
        if False == self.is_within_bounds(new_x, new_y):
            print("new location does not exist in bounds")
            return False   
             
        ### I need to integrate this with is_capture_possible()
        if self.get(new_x, new_y) !=  '.':
            print("Intended space is occupied.")
            return False

        value = self.get(old_x, old_y)
        if value == '.':
            print ("its a dot.")
            return False
        if value != self.turn:
            print ("it is the other player's turn")
            return False
        ## Hoping this will catch the condition of a capture.
        if self.capture_possible:
            self.capture(old_x, old_y, new_x, new_y)

        if value == 'x':
            dir = -1
        else:
            dir = 1
        if new_y - old_y != dir:
            print ("wrong way")
            return False

        if abs(old_x - new_x) != 1:
            print("x delta too high")
            return False
        print ("This time. . . This time.")
        return True

    def capture(self, old_x, old_y, new_x, new_y):
        # check if capture is possible
        if not self.capture_possible(old_x, old_y, new_x, new_y):
           # print("Not Valid Capture. Should be more info included.")
            return
        # set value of new square to that of old square
        value = self.get(old_x, old_y)
         
        self.set(new_x, new_y, value)
        # set value of old square to blank or '.'
        self.set(old_x, old_y, ".")
        # get victim and kill it
        if value == "x" or "0":
            victim_y = old_y-1
        else:
            victim_y = old_y+1

        if new_x - old_x > 0:
            victim_x = old_x + 1
        else:
            victim_x = old_x - 1
        self.set(victim_x, victim_y, ".")
        print("jumped!")
        self.change_turns()

    def capture_possible(self, old_x, old_y, new_x, new_y):
        #within bounds
        if not self.is_within_bounds(old_x, old_y):
            return False
        if not self.is_within_bounds(new_x, new_y):
            return False

        #direction
        value = self.get(old_x, old_y)
        if value == "x" or "O":
            dir = -2
            victim_y = old_y - 1
        else:
            dir = 2
            victim_y = old_y + 1
        if new_y - old_y != dir:
            print("Wrong Way")
            return False

        # correct turn
        if value != self.turn:
            print("Other player's turn")
            return False

        # victim is correct/exists
        if new_x - old_x > 0:
            victim_x = old_x + 1
        else:
            victim_x = old_x - 1
        victim = self.get(victim_x, victim_y)
        if victim == ".":
            print("Can't jump empty spaces")
            return False
        if victim == self.turn:
            print("Can't jump allies")
            return False
        print("Jump Authorized")
        return True

    def is_within_bounds(self, x, y):
        return (0 <= x and x < 8 and 0 <= y and y < 8)
        
    def get(self, x, y):
        return self.spot[x + y * 8]

    def set(self, x, y, value):
        self.spot[x + y * 8] = value

    def show(self):
        print("  ")
        for y in range(8):
            s = ""
            for x in range(8):
                s = s + " " + self.get(x, y)
            print(s)
            
 ####### Testing Below ########

b = Board()
b.show()       

### put in capture mechanics    
b.move(5, 5, 6, 4)

b.show()
b.move(4, 2, 5, 3)
b.show()
b.capture(6, 4, 4, 2)
b.show()
