import logging
from abc import ABC, abstractmethod

from SmartHomeSystem import RoomBuilder, RoomDirector
from SmartHomeSystem import AlertSystem

logger = logging.getLogger(__name__)


# Meta class/Monostate method
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Singleton SmartHome
class SmartHome(metaclass=Singleton):
    def __init__(self):
        if not hasattr(self, "initiated"):
            self.rooms = {}
            self.alert_system = AlertSystem()
            self.initiated = True
            self.home_lock = None
            logger.info("Initialized the smart home.")

    def add_room(self, builder: RoomBuilder):
        director = RoomDirector(builder)
        room = director.build_room()
        self.rooms[room.name] = room

    def add_alert_system_to_room_devices(self, room_name: str):
        room = self.rooms.get(room_name)
        if room:
            for device in room.devices:
                device.add_observer(self.alert_system)
        else:
            logger.warning(f"No room found with name {room_name}")

    def operate_room(self, room_name: str):
        room = self.rooms.get(room_name)
        if room:
            room.operate_devices()
        else:
            logger.warning(f"No room found with name {room_name}")

    def __str__(self):
        room_names = ", ".join(self.rooms.keys())
        return f"SmartHome with rooms: {room_names}"


""" using __new__
class SmartHome:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SmartHome, cls).__new__(cls)
            cls._instance.__initiated = False
        return cls._instance

    def init(self):
        if self.__initiated:
            return
        self.rooms = []
        self.devices = []
        self.__initiated = True
"""

if __name__ == "__main__":
    home1 = SmartHome()
    home2 = SmartHome()
    assert home1 is home2
