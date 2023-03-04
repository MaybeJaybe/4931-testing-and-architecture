# by Kami Bigdely
# Extract superclass.

class ShapeDef():
    def __init__(self, visible):
        self.visible = visible
    
    def set_visible(self, is_visible):
        self.visible = is_visible



class Circle(ShapeDef):
    
    def __init__(self, x, y, r, visible = True):
      self.center_x = x
      self.center_y = y
      self.r = r
      
    def display(self):
        print('drew the circle.')
        
    def get_center(self):
        return self.center_x, self.center_y
    
    
class Rectangle(ShapeDef):
    
    def __init__(self, x, y, width, height, visible = True):
        # left-bottom corner.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def display(self):
        if self.visible:
            print('drew the rectangle.')
            
    def hide(self):
        self.visible = False
        
    def make_visible(self):
        self.visible = True
        
    def get_center(self):
        return self.x + self.width/2, \
               self.y + self.height/2 



if __name__ == "__main__":
    circle = Circle(0,0,10, False)
    circle.set_visible(True)
    circle.display()
    print('center point',circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display() # does not display because it's hidden.
    rect.make_visible()
    rect.display()
    print('center point',rect.get_center())