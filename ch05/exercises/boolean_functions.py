
def percentage_to_letter(score=0):
  letter = "F"
  if score >= 90:
    letter = ("A")
  elif score >= 80:
    letter = ("B")
  elif score >= 70:
    letter = ("C")
  elif score >= 60:
    letter = ("D")
    return letter

score = float(input("Please enter a score: "))
result = percentage_to_letter(score=0)

def is_passing(grade = None):
  if letter == "A":
    return True
  if letter == "B":
    return True
  if letter == "C":
    return True
  return False
  