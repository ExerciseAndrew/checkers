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
            print("Old no boundy")
            return False
        if False == self.is_within_bounds(new_x, new_y):
            print("New no boundy")
            return False   
             
        
        if self.get(new_x, new_y) !=  '.':
            print (".")
            return False

        value = self.get(old_x, old_y)
        if value == '.':
            print ("its a dot.")
            return False
        if value != self.turn:
            print ("Not sure why. It's just broke.")
            return False

        if value == 'x':
            dir = -1
        else:
            dir = 1
        if new_y - old_y != dir:
            print ("wrong way, little boy")
            return False

        if abs(old_x - new_x) != 1:
            print("too much or too little")
            return False
        print ("This time. . . This time.")
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
    
b = Board()
b.show()       

### put in capture mechanics    
b.move(5, 5, 6, 4)

b.show()
