class Rectangle:
  def __init__(self, x, y , h, w):
    list = [x,y,h,w]
    for i in range(len(list)):
      if list[i] < 0:
        list[i] = 0
    self.x = list[0]
    self.y = list[1]
    self.height = list[2]
    self.width = list[3]

  def __str__(self):
    string = "X: " + str(self.x) + " Y:" + str(self.y) + " Height: " + str(self.height) + " Width: " + str(self.width)
    return string