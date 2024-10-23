# print('hello')
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(full_name)
# print(f"Hello, {full_name.title()}!")
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)
# # learning lists
# print(bicycles[0])
# print(bicycles[0].title())
# message = f"My first bicycle was a {bicycles[0].title()}"
# print(message)
# #Exercise
# names = ['clo', 'lauredane', 'siona','kate']
# print(names)
# print(names[0])
# print(names[1].title())
# love_message =f'I love {names[0].title()} so much'
# print(love_message)
# cars = ['yarris', 'honda','mecedes','suzuki']
# print(cars)
# message_1 = f'One day i will own a {cars[2].upper()}'
# print(message_1)
# message_2 = f'Clodine owns a {cars[0].title()}'
# print(message_2)
# cars[0]= 'BMW'
# print(cars)
# #adding elements to a list using the append function that adds an element to the end of the list
# cars.append('yamaha')
# print(cars)
# #Adding a new element to any position on my list using the insert function
# cars.insert(1, 'tesla')
# print(cars)
# #removing elements from a list if you know the position of the item, use the del function
# del(cars[0])
# print(cars)
# #removing an item from a list and keeping it to use later using the pop statement. Pop statement removes the last elt in a list and still preserves it
# print(cars)
# popped_cars = cars.pop()
# print(cars)
# print(popped_cars)
# #printing a statement using popped cars
# print(f'The last motorcycle I owned was {popped_cars.title()}')
# #popping aitems from any position
# first_owned = cars.pop(0)
# print(first_owned)
# print(f'The first car I owned was a {first_owned.title()}')
# #removing an item by value
# cars.remove('mecedes')
# print(cars)
# #Exercises
# best_people = ['clodine', 'kate', 'elisabeth']
# print(best_people)
# sister = best_people[0]
# first_daughter = best_people[1]
# last_daughter = best_people[2]
# print(f'The craziest person invited is {sister.title()}')
# print(f'It will be a priviledge to have {first_daughter.upper()} at the party')
# print(f'\n{last_daughter.title()} will eat all the meat')
# best_people.remove('clodine')
# print(best_people)
# best_people.insert(0, "valery")

# print(best_people)
# #organising a list
# #sorting a list permanently with the sort() method
# print(cars)
# cars.append('mecedes')
# cars.append('yaris')
# print(cars)
# cars.sort()
# print(cars)
# #sorting in reverse alphabetical order
# cars.sort(reverse=True)
# print(cars)
# #sorting a list temporarily with the sorted() function

# #conrol flows is python
# number = int(input('Enter a number:'))
# if number >0:
#     print(f'{number} is a possive number.')
#     print('A statement outside the if statement')
# #Python indentations
# x = 0
# total = 3
# if x != 0: 
#     total += x
#     print(total)
# print('This is always executed.')
# #python if...else statements
number = int(input('Enter number:'))
if number > 0:
    print('Positive number')
else:
    print('Not a positive number')