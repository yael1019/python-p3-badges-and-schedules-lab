def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    list_of_badges = []
    for name in names:
        list_of_badges.append(f'Hello, my name is {name}.')
    return list_of_badges

def assign_rooms(names):
    list_of_rooms = []
    for index, name in enumerate(names):
        list_of_rooms.append(f"Hello, {name}! You'll be assigned to room {index + 1}!")
    return list_of_rooms

# print(assign_rooms(["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"]))

def printer(names):
    list_of_names = batch_badge_creator(names)
    list_of_rooms = assign_rooms(names)
    for name in list_of_names:
        print(name)
    for room in list_of_rooms:
        print(room)
