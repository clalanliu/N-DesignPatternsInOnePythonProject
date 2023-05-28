import logging

from SmartHomeSystem import (
    SmartHome,
    LivingRoomBuilder,
    KitchenRoomBuilder,
    LivingRoomDeviceFactory,
    KitchenRoomDeviceFactory,
    ThirdPartySmartLight,
    SmartDeviceAdapter,
    SmartDeviceGroup,
    LivingRoomSmartLight,
    LivingRoomSmartThermostat,
    WiFi,
    MotionSensor,
    VoiceControl,
    SmartHomeFacade,
    SmartDeviceProxy,
    PaintingFactory,
    TurnOnCommand,
    TurnOffCommand,
    RemoteControl,
    RequestableLivingRoomBuilder,
    SecurityHandler,
    MaintenanceHandler,
    NotificationHandler,
    Request,
    LightOnExpression,
    LightOffExpression,
    ThermostatSetExpression,
    Caretaker,
    SmartLock,
    EcoTemperatureControl,
    NormalTemperatureControl,
    DeviceStatusVisitor,
)


if __name__ == "__main__":
    # Interactions
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    home = SmartHome()

    # Build rooms and add devices
    home.add_room(builder=LivingRoomBuilder(LivingRoomDeviceFactory()))
    home.add_room(builder=KitchenRoomBuilder(KitchenRoomDeviceFactory()))

    # Add alert system to all devices in each room
    for room_name in home.rooms.keys():
        home.add_alert_system_to_room_devices(room_name)  # Pass room_name here

    # Operate devices in each room
    for room_name in home.rooms.keys():
        home.operate_room(room_name)

    # Manually trigger an event to demonstrate the alert system
    room_name = list(home.rooms.keys())[0]  # Let's just pick the first room
    first_room = home.rooms[room_name]

    if first_room.devices:  # Check if there are devices in the room
        first_device = first_room.devices[0]  # Pick the first device
        first_device.operate()  # This should trigger the alert system

    # Add a third-party device to the first room
    third_party_light = ThirdPartySmartLight()
    adapter = SmartDeviceAdapter(third_party_light)
    first_room.add_device(adapter)
    first_room.devices[-1].operate()

    # Create a group and add devices to it
    group = SmartDeviceGroup()
    group.add_device(LivingRoomSmartLight(WiFi()))
    group.add_device(LivingRoomSmartThermostat(WiFi()))

    # Add the device group to the first room
    first_room.add_device(group)
    first_room.devices[-1].operate()

    # Create decorated devices
    light = LivingRoomSmartLight(WiFi())
    light_with_motion_sensor = MotionSensor(light)
    light_with_motion_sensor_voice_control = VoiceControl(light_with_motion_sensor)

    # Add decorated devices to the rooms
    first_room.add_device(light_with_motion_sensor_voice_control)
    first_room.devices[-1].operate()

    # Add facade
    facade = SmartHomeFacade()
    for room_name, room in home.rooms.items():
        for device in room.devices:
            facade.add_device(device)

    facade.turn_all_lights_on_and_off()
    facade.adjust_temperature(30)

    # Add access check using proxy
    first_room = home.rooms[room_name]
    first_room.devices[-1] = SmartDeviceProxy(light_with_motion_sensor_voice_control)
    first_room.devices[-1].operate()

    # Flyweight Painting Factory
    painting_factory = PaintingFactory()

    # Create paintings
    mona_lisa = painting_factory.get_painting(
        "Mona Lisa", "Leonardo da Vinci", "Renaissance", "Oil on canvas"
    )
    starry_night = painting_factory.get_painting(
        "The Starry Night", "Vincent van Gogh", "Post-Impressionism", "Oil on canvas"
    )
    mona_lisa_2 = painting_factory.get_painting(
        "Mona Lisa", "Leonardo da Vinci", "Renaissance", "Oil on canvas"
    )
    first_room = home.rooms[list(home.rooms.keys())[0]]
    first_room.add_painting(mona_lisa)
    first_room.add_painting(starry_night)
    second_room = home.rooms[list(home.rooms.keys())[1]]
    second_room.add_painting(mona_lisa_2)

    # Display the paintings in the room
    first_room.display_paintings()
    second_room.display_paintings()

    # Request handling using chain-of-responsibility
    security_handler = SecurityHandler()
    maintenance_handler = MaintenanceHandler()
    notification_handler = NotificationHandler()

    request1 = Request("Security Alert")
    request2 = Request("Maintenance Request")
    request3 = Request("Notification")

    home.add_room(builder=RequestableLivingRoomBuilder(KitchenRoomDeviceFactory()))
    home.rooms[list(home.rooms.keys())[-1]].add_handler(security_handler)
    home.rooms[list(home.rooms.keys())[-1]].add_handler(maintenance_handler)
    home.rooms[list(home.rooms.keys())[-1]].add_handler(notification_handler)
    home.rooms[list(home.rooms.keys())[-1]].process_request(request1)
    home.rooms[list(home.rooms.keys())[-1]].process_request(request2)
    home.rooms[list(home.rooms.keys())[-1]].process_request(request3)

    home.add_room(builder=RequestableLivingRoomBuilder(KitchenRoomDeviceFactory()))
    home.rooms[list(home.rooms.keys())[-1]].add_handler(maintenance_handler)
    home.rooms[list(home.rooms.keys())[-1]].add_handler(notification_handler)

    home.rooms[list(home.rooms.keys())[-1]].process_request(request1)
    home.rooms[list(home.rooms.keys())[-1]].process_request(request2)
    home.rooms[list(home.rooms.keys())[-1]].process_request(request3)

    # design control with command pattern
    turn_on_command = TurnOnCommand(light)
    turn_off_command = TurnOffCommand(light)

    remote_control = RemoteControl()

    remote_control.set_command(turn_on_command)
    remote_control.press_button()

    remote_control.set_command(turn_off_command)
    remote_control.press_button()

    # interpretor enables command processing
    light = LivingRoomSmartLight(WiFi())
    thermostat = LivingRoomSmartThermostat(WiFi())

    light_on_expression = LightOnExpression(light)
    light_off_expression = LightOffExpression(light)
    thermostat_set_expression = ThermostatSetExpression(thermostat, 25)

    expressions = [
        light_on_expression,
        light_off_expression,
        thermostat_set_expression,
    ]

    context1 = "ON"
    context2 = "OFF"
    context3 = "28"
    context4 = "ACTIVATE"
    context5 = "DEACTIVATE"

    for expression in expressions:
        expression.interpret(context1)
        expression.interpret(context2)
        expression.interpret(context3)
        expression.interpret(context4)
        expression.interpret(context5)

    # iterator through device
    iterator = first_room.create_iterator()

    for device in iterator:
        print(f"Device in first room: {device}")

    # using memento to record room states
    first_room.set_state("Beige", "Wooden", "Large")
    logger.info(
        f"Initial state of {first_room.name}: {first_room.walls}, {first_room.doors}, {first_room.windows}"
    )

    caretaker = Caretaker()
    caretaker.add_memento(first_room.name, first_room.create_state_memento())

    first_room.set_state("Blue", "Glass", "Medium")
    logger.info(
        f"Updated state of {first_room.name}: {first_room.walls}, {first_room.doors}, {first_room.windows}"
    )

    memento = caretaker.get_memento(first_room.name)
    if memento:
        first_room.restore_state(memento)
        logger.info(
            f"Restored state of {first_room.name}: {first_room.walls}, {first_room.doors}, {first_room.windows}"
        )

    # using state pattern in home lock
    home.home_lock = SmartLock(WiFi())
    home.home_lock.lock()  # Lock the smart lock
    home.home_lock.unlock()  # Unlock the smart lock
    home.home_lock.unlock()  # Try unlocking the already unlocked smart lock
    home.home_lock.lock()  # Lock the smart lock
    home.home_lock.lock()  # Try locking the already locked smart lock

    # using strategy patternfor temperature control
    thermostat.set_temperature_control_strategy(EcoTemperatureControl)
    thermostat.control_temperature()  # Apply eco temperature control
    thermostat.set_temperature_control_strategy(NormalTemperatureControl)
    thermostat.control_temperature()  # Apply eco temperature control

    # visitor pattern
    device_status_visitor = DeviceStatusVisitor()
    first_room.accept_visitor(device_status_visitor)
