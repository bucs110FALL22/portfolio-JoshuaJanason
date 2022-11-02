import time
#import uuid

class Animal:
  def __init__(self, name, type):
    self.id = self(id) #make unique
    self.name = name #uuid()
    self.type = type
    self.arrived = time.strftime("%d/%m/%Y")
    self.adopted = None 

  def set_adopted(self):
    self.arrived = time.strftime("%d/%m/%Y")

  def __str__(self):
    result_str = f"{self.name}[{self.type}]"
    result_str += f"\narrived: {self.arrived}"
    result_str += f"\nadopted:{self.adopted}"
  
def main():
      fido = Animal("fido", "cat")
      fido.setAdopted()
main()

