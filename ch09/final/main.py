import random
import ImageAPI
import GifAPI

def main():
  capi = GifAPI.GifAPI(limit = 10)
  gapi = ImageAPI.ImageAPI(number = 2)
  gif_results = capi.get()
  image_results = gapi.get()
  for gif in capi.get():
    facts = ['_id']+['tags']+['owner']
    random.shuffle(facts)
    return gif_results
  for image in gapi.get():
    return image_results
  both = cat_image + cat_gif
  choice = input("Would you like to see a cat 'image', a cat 'gif', or 'both'?")
  if choice is str(image):
    return cat_image
  if choice is str(gif):
    return cat_gif
  if choice is str(both):
    return both
  
main()
    