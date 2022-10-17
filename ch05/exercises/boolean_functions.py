
def percentage_to_letter(score=0):
  if score >= 90:
    letter = ("A")
    return letter
  if score <= 80:
    letter = ("B")
    return letter
  if score <= 70:
    letter = ("C")
    return letter
  if score <= 60:
    letter = ("D")
    return letter
  if score < 60:
    letter = ("F")
    return letter

score = float(input("Please enter a score: "))
result = percentage_to_letter(score=0)

def is_passing(grade = None):
  if result == ("A", "B", "C", "D"):
    return True
  else:
    return False
  