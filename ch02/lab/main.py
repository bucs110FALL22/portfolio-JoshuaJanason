import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 15
cost_per_class = cost_per_week/classes_per_week
nice_message = "Hello, your cost per class is $"
print(nice_message, cost_per_class) 
print(weeks, type(weeks))
print(classes, type(classes))
print(tuition, type(tuition))
print(cost_per_week, type(cost_per_week))
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))
print(nice_message, type(nice_message))

#Part B
my_list = ["Josh", 3, 9, "Hi", 20.0]
random_my_list = random.choice(my_list)
random_my_list_message = "Your random result is:"
print(random_my_list_message, random_my_list)
