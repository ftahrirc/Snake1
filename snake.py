import turtle,random
class Cell:
  def__init__(self,size,t,x,y):
    self.x=x
    self.y=y
    self.t=t
    self.size=size
  def draw_square(self):
    for side in range(4):
      self.t.fd(self.size)
      self.t.left(90)
      
      
  def draw_snake()(self)
    for side in range(5):
      cell=cell(10,turtle.turtle(),i*10,i*10)
      cell.draw_square()
      cell.draw_snake()
      cell=Cell(10,turtle.Turtle(),0,0)
      cell.draw_square()
 class food:
    def__init__(self):
    self.cell=Cell(x,y)
    
    
    
    
    
    
    
    
    
  class Cell:
   def __init__(self,t):
     # set initial position
     self.x = 0
     self.y = 0
     # set initial size of a cell
     self.cell_size = 10
     # set the turtle
     self.t = t
  
