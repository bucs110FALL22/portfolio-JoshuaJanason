import requests

class GifAPI:
  def __init__(self, limit=10, skip=0):
    self.api_url = f"https://cataas.com/api/cats?limit={limit}&skip={skip}"

  def get(self): 
    r = requests.get(self.api_url)
    response = r.json()
    print(response)
    cat_gif = input("Enter which cat picture you would like by entering the owner of the cat: ")
    if cat_gif is str(response("owner")):
      return cat_gif
    else:
      return None
    print(response.json)  

  def response(self):
    r = requests.get(self.api_url)
    response = r.json()
    print(response)
    amount = input("Enter how many cat images you would like to see: ")
    for amount in cat_gif:
      return cat_gif
   
    
    
    
    
    
    
    
   