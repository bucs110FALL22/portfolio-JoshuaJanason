class StringUtility:
  def __init__(self, string):
    self.string = string
    
  def __str__(self):
    return self.string

  def vowels(self):
    count = 0
    list = "aeiouAEIOU"
    for i in self.string:
      if i in list:
        count += 1
    if count >= 5: 
      count = "many"
    return str(count)
   
  def bothEnds(self):
    count = 0
    for i in self.string:
      count = count + 1 
    one_string = self.string[0:2]
    two_string = self.string[count-2:count]
    total_string = one_string + two_string
    if len(self.string) < 2:
      count = ""
    return str(total_string)

  def fixStart(self):
    star_string = self.string[0] + self.string[1:].replace(self.string[0], "*")
    if len(self.string) <= 1:
      self.string = self.string
    return star_string
    
#my code works for asciiSum it just doesn't go through since fixStart doesn't pass(I put hashmarks over the test on main.py to test this part and it worked)
  def asciiSum(self): 
    count = 0
    for i in self.string:
      count = count + ord(i)
    return int(count)

  def cipher(self):
    for i in range(self.string):
      new_letter = ord(i+1)
      final_string = new_letter(i)
    return str(final_string)

    
  