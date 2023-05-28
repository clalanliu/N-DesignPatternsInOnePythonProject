class RoomState:
    def __init__(self, walls, doors, windows):
        self.walls = walls
        self.doors = doors
        self.windows = windows


class Caretaker:
    def __init__(self):
        self.mementos = {}

    def add_memento(self, room_name, memento):
        self.mementos[room_name] = memento

    def get_memento(self, room_name):
        return self.mementos.get(room_name)
