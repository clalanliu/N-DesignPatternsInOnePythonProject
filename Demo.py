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
)


if __name__ == "__main__":
    # Interactions
    logging.basicConfig(level=logging.INFO)
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
    light_with_motion_sensor = MotionSensor(LivingRoomSmartLight(WiFi()))
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
