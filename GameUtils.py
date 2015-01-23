class Fighter:
    #sprite_images should be a list of tuples with the first value being
    #the image's name, and the second value being the file name where
    #the image is located.  The value of initial_image is the name
    #of the image you want the character to have as its default image
    def __init__(self,action_images,movement_images,default_image,position):
        #set the position of the top left corner of the sprite's image rectangle
        self.x = position[0]
        self.y = position[1]
        #set the fighter's initial velocity  to 0 in both directions
        self.vx = 0
        #self.vy = 0
        #set the fighter's initial life to 10
        self.life = 10
        #fill a dictionary with the passed-in sprite images referenced in sprite_images
        #and set their keys to the names that were passed in with them
        self.default_image = default_image
        self.action_images = action_images
        self.current_image = self.default_image
        #set up a walking sweeper that will allow you to switch back and forth
        #through the walking images
        self.walker = Sweeper(movement_images)

    def stop(self):
        self.current_image = self.default_image
        self.vx = 0
        #self.vy = 0
        
    def punch(self):
        self.current_image = self.action_images["punch"]
        self.vx = 0
        #self.vy = 0
        
    def kick(self):
        self.current_image = self.action_images["kick"]
        self.vx = 0
        #self.vy = 0
        
    def block(self):
        self.current_image = self.action_images["block"]
        self.vx = 0
        #self.vy = 0

    def hit(self):
        self.current_image = self.action_images["hit"]
        self.x = self.x - 50

        
    def walk(self,velocity):
        self.current_image = self.walker.sweep()
        self.vx = velocity
        #self.vy = 0
        
    def get_drawable_surface(self):
        return self.current_image.convert_alpha()

class Sweeper:
    def __init__(self,target):
        self.current = 0
        self.target = target

    def sweep(self):
        if (self.current + 1) < len(self.target):
            self.current = self.current + 1
        else:
            self.current = 0
            self.target.reverse()
        return self.target[self.current]
