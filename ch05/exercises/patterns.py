#Part 1
def star_pyramid():
    print("Enter how many lines of stars you would like")
    rows = int(input(":"))
    for i in range(1, rows + 1):      
      print("*" * i)

star_pyramid()


#Part 2 
def rstar_pyramid():
    print("Enter how many lines of stars you would like")
    r_rows = int(input(":"))
    for i in range(r_rows, 0, - 1):      
      print("*" * i)

rstar_pyramid()