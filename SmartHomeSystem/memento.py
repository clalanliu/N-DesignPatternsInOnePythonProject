from abc import ABC
from typing import Optional


class Memento(ABC):
    def __init__(self):
        pass


class RoomState(Memento):
    def __init__(
        self, walls: Optional[str], doors: Optional[str], windows: Optional[str]
    ):
        self.walls = walls
        self.doors = doors
        self.windows = windows


class Caretaker:
    def __init__(self):
        self.mementos = {}

    def add_memento(self, name: str, memento: Memento):
        self.mementos[name] = memento

    def get_memento(self, name: str):
        return self.mementos.get(name)
