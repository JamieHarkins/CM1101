from items import *

room_home = {
    "name": "Home",

    "description":
    """Uni Halls: You are in your room. There seems to be a funky smell coming from
under your bed, you decide its best not to investigate. You know that you have
left your bus pass and student card somewhere on your desk. """,

    "exits": {"east": "Bus"},

    "items": [item_buspass, item_id, item_worksheet_1]
}

room_bus = {
    "name": "Bus",

    "description":
    """Bus Stop: You are at the bus stop. Your bus is already waiting.""",

    "exits":  {"west": "Home", "east" : "SU", "north" : "University"},

    "items": []
}

room_su = {
    "name": "SU",

    "description":
    """SU: You find yourself in the students union, immediately you decide to go to
the pub. You have the option to get some vodka shots, but be careful not to
have too many.""",

    "exits": {"west": "Bus"},

    "items": []
}

room_university = {
    "name": "University",

    "description":
    """Queens Building: You are in the queens building. The winding corridors and many
floors are daunting, luckily you can just take the elevator. """,

    "exits": {"east": "Elevator", "south": "Bus", "west" : "Cafeteria", "north" : "Kirill"},

    "items": []
}

room_elevator = {
    "name": "Elevator",

    "description":
    """Elevator: You manage to squeeze into the elevator alongside seven other
students. There are three buttons for you to choose from:""",

    "exits": {"west" : "University", "1": "Lab", "2" : "Lecture", "3" : "Window"},

    "items": []
}

room_window = {
    "name": "Window",

    "description":
    """Window: You have arrived at the top floor. You notice an open window near
the other side of the room, it would be easy to relieve all of
your frustrations right now... """,

    "exits": {"west" : "Elevator"},

    "items": []
}

room_lecture = {
    "name": "Lecture",

    "description":
    """Lecture: You have entered the lecture room. There aren't many more seats
available but you manage to find one near the back of the room. Matt begins his
lecture. For all intents and purposes...""",

    "exits": {"west" : "Elevator"},

    "items": [item_worksheet_3]
}

room_lab = {
    "name": "Lab",

    "description":
    """Lab: You are in the lab. There are several computers around the room that
aren't occupied by other frustrated students. You take a seat, and after
waiting 20 minutes, you manage to log on.""",

    "exits": {"west" : "Elevator"},

    "items": [item_worksheet_2]
}

room_cafeteria = {
    "name": "Cafeteria",

    "description":
    """Café: You enter the café, this is where you come to grab a coffee after matt
has instructed you to do so. It might be a good idea to grab a coffee before
your next lecture to make sure you stay awake throughout.""",

    "exits": {"south" : "Transfer", "east" : "University"},

    "items": [item_coffee]
}

room_transfer = {
    "name": "Transfer",

    "description":
    """Transfer Hub: You have arrived at the transfer hub... this is the place where
dreams go to die. There are two other students, both who aren't looking very happy.
You can try to switch courses but as it is this late into the course, it may not be
such a good idea. But then again, Cardiff Met is always an option.""",

    "exits": {"north" : "Cafeteria"},

    "items": []
}

room_kirill = {
    "name": "Kirill",

    "description":
    """You are in Kirill's Office, you see a range off high school muscial posters on the wall.""",

    "exits": {"south" : "University"},

    "items": []
}


rooms = {
    "Home": room_home,
    "Bus": room_bus,
    "SU": room_su,
    "University": room_university,
    "Elevator": room_elevator,
    "Window": room_window,
    "Lecture": room_lecture,
    "Lab" : room_lab,
    "Cafeteria" : room_cafeteria,
    "Transfer" : room_transfer,
    "Kirill" : room_kirill
}
