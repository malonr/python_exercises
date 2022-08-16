my_guests = ['fer', 'betsy','cristina']

msg = "I would like to invite you to eat in a fancy restaurant"

print(f"{msg},{my_guests[0].title()}")
print(f"{msg},{my_guests[1].title()}")
print(f"{msg},{my_guests[2].title()}")

print(f"{my_guests[2].title()} won't be able to go to the restaurant")

my_guests[2] = 'ascaria'

print(f"{msg},{my_guests[0].title()}")
print(f"{msg},{my_guests[1].title()}")
print(f"{msg},{my_guests[2].title()}")

print("I found a bigger dinner table, more people is coming! ")

my_guests.insert(0, 'honorio')
my_guests.insert(2, 'melanio')
my_guests.append('sandra')

print(f"{msg},{my_guests[0].title()}")
print(f"{msg},{my_guests[1].title()}")
print(f"{msg},{my_guests[2].title()}")
print(f"{msg},{my_guests[3].title()}")
print(f"{msg},{my_guests[4].title()}")
print(f"{msg},{my_guests[5].title()}")

print("Sorry to tell you, I only can invite two people for dinner")

msg_2 = "I'm sorry, I can't invite you to dinner "

sorry_1 = my_guests.pop(0)
print(f"{msg_2},{sorry_1.title()}")

sorry_2 = my_guests.pop(1)
print(f"{msg_2},{sorry_2.title()}")

sorry_3 = my_guests.pop(2)
print(f"{msg_2},{sorry_3.title()}")

sorry_4 = my_guests.pop(2)
print(f"{msg_2},{sorry_4.title()}")

print(f"You're still invited to dinner, {my_guests[0].title()}")
print(f"You're still invited to dinner, {my_guests[1].title()}")

del my_guests[0]
del my_guests [0]

print(my_guests)











