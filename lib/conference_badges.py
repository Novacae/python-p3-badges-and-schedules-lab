def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badges = []
    for name in names:
        badge_message = "Hello, my name is " + name + "."
        badges.append(badge_message) 
    return badges

def assign_rooms(names):
    room_assignments = []
    for i in range(len(names)):
        room_num = i + 1
        room_assignment = "Hello, " + names[i] + "! You'll be assigned to room " + str(room_num) + "!"
        room_assignments.append(room_assignment)
    return room_assignments

def printer(names):
    messages = batch_badge_creator(names)
    for message in messages:
        print(message)
    assignments = assign_rooms(names)
    for assignment in assignments:
        print(assignment)
