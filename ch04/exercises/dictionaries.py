text = "The asteroid, Dimorphos, is the size of a stadium — or the Great Pyramid of Giza, as one scientist put it Monday — and is about 7 million miles from Earth at the moment. It orbits a larger asteroid named Didymos. Neither poses a threat to our planet now or anytime in the foreseeable future."


replacements = {
  "asteroid":"dragon",
  "Dismorphos":"Josh",
  "stadium":"lake",
  "Great Pyramid of Giza":"Empire State Building",
  "scientist":"hunter",
  "Monday":"Sunday",
  "orbits":"circles",
  "Didymos":"Jordan",
  "planet":"city",
  "threat":"problem",
}
for key, value in replacements.items():
  text = text.replace(key, value)
print(text)