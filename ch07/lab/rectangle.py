
class Rectangle:
    def __init__(self, x, y, h, w):
      self.x = x
      self.y = y
      self.height = h
      self.width = w

    def __str__(self):
      result_str = f"{self.x}[{self.y}]"
      result_str += f"\nheight: {self.height}"
      result_str += f"\nwidth:{self.width}"

def main():
  shape = Rectangle(100, 100, 15, 10)

main()