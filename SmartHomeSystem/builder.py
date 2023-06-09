import logging
from abc import ABC, abstractmethod
from typing import List, Optional

from SmartHomeSystem import (
    SmartDeviceFactory,
    PaintingFactory,
    DeviceIterator,
    RoomState,
    SmartDevice,
    Painting,
    DeviceVisitor,
)

logger = logging.getLogger(__name__)
painting_factory = PaintingFactory()


class Room:
    def __init__(self, name):
        self.name: str = name
        self.walls: Optional[str] = None
        self.doors: Optional[str] = None
        self.windows: Optional[str] = None
        self.devices: List[SmartDevice] = []
        self.paintings: List[Painting] = []

    def add_device(self, device: SmartDevice):
        self.devices.append(device)

    def operate_devices(self):
        for device in self.devices:
            device.operate()

    def add_painting(self, painting: Painting):
        self.paintings.append(painting)

    def display_paintings(self):
        for painting in self.paintings:
            painting.display()

    def create_iterator(self):
        return DeviceIterator(self.devices)

    def set_state(
        self, walls: Optional[str], doors: Optional[str], windows: Optional[str]
    ):
        self.walls = walls
        self.doors = doors
        self.windows = windows

    def create_state_memento(self):
        return RoomState(self.walls, self.doors, self.windows)

    def restore_state(self, state: RoomState):
        self.walls = state.walls
        self.doors = state.doors
        self.windows = state.windows

    def accept_visitor(self, visitor: DeviceVisitor):
        for device in self.devices:
            device.accept(visitor)


# Builder Pattern
class RoomDirector:
    def __init__(self, builder):
        self._builder = builder

    def build_room(self):
        self._builder.create_new_room()
        self._builder.set_walls()
        self._builder.set_doors()
        self._builder.set_windows()
        self._builder.add_light()
        self._builder.add_thermostat()
        return self._builder.room


# Update RoomBuilder
class RoomBuilder(ABC):
    def __init__(self, factory: SmartDeviceFactory):
        self.factory: SmartDeviceFactory = factory
        self.room: Optional[Room] = None

    def create_new_room(self, room_type: str):
        room_name = f"{room_type} {id(self)}"
        self.room = Room(room_name)

    @abstractmethod
    def set_walls(self):
        pass

    @abstractmethod
    def set_doors(self):
        pass

    @abstractmethod
    def set_windows(self):
        pass

    def add_light(self):
        light = self.factory.create_smart_light()
        self.room.add_device(light)

    def add_thermostat(self):
        thermostat = self.factory.create_smart_thermostat()
        self.room.add_device(thermostat)


# Update LivingRoomBuilder
class LivingRoomBuilder(RoomBuilder):
    def create_new_room(self):
        super().create_new_room("Living Room")

    def set_walls(self):
        logger.info("Building living room walls")

    def set_doors(self):
        logger.info("Building living room doors")

    def set_windows(self):
        logger.info("Building living room windows")


class KitchenRoomBuilder(RoomBuilder):
    def create_new_room(self):
        super().create_new_room("Kitchen")

    def set_walls(self):
        logger.info("Building kitchen room walls")

    def set_doors(self):
        logger.info("Building kitchen room doors")

    def set_windows(self):
        logger.info("Building kitchen room windows")
