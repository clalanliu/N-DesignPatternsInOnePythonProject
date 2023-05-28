from __future__ import annotations
import logging

from SmartHomeSystem import Room, LivingRoomBuilder, RoomBuilder, SmartDeviceFactory

logger = logging.getLogger(__name__)


class RequestableRoom(Room):
    def __init__(self, name):
        super().__init__(name)
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def process_request(self, request):
        for handler in self.handlers:
            handler.handle_request(request)


class RequestableLivingRoomBuilder(RequestableRoom, LivingRoomBuilder, RoomBuilder):
    def __init__(self, factory: SmartDeviceFactory):
        RoomBuilder.__init__(self, factory)

    def create_new_room(self):
        room_name = f"Living Room {id(self)}"
        self.room: RequestableRoom = RequestableRoom(room_name)


class Request:
    def __init__(self, message: str):
        self.message = message


class Handler:
    def __init__(self, successor: Handler = None):
        self.successor = successor

    def handle_request(self, request):
        pass


class SecurityHandler(Handler):
    def handle_request(self, request):
        if request.message == "Security Alert":
            logger.info(f"Security alert received")
        elif self.successor is not None:
            logger.info(f"SecurityHandler pass the request: {request}")
            self.successor.handle_request(request)


class MaintenanceHandler(Handler):
    def handle_request(self, request):
        if request.message == "Maintenance Request":
            logger.info(f"Maintenance request received")
        elif self.successor is not None:
            logger.info(f"MaintenanceHandler pass the request: {request}")
            self.successor.handle_request(request)


class NotificationHandler(Handler):
    def handle_request(self, request):
        if request.message == "Notification":
            logger.info(f"Notification received")
        elif self.successor is not None:
            logger.info(f"NotificationHandler pass the request: {request}")
            self.successor.handle_request(request)
