import requests

class ImageAPI:
  def __init__(self, number = ''):
    self.api_url = f'https://http.cat/api?number={number}'

  def get(self): 
    r = requests.get(self.api_url)
    response = r.json()
    print(response)
    cat_image = input("Enter the number of which cat image you want: ")
    if cat_image is int(response('')):
      return cat_image
    else:
      return
    print(response.json)  
  