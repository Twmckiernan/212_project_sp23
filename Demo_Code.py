#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021-2023 iRobot Corporation. All rights reserved.
#

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

backend = Bluetooth()
robot = Root(backend)

await robot.move(275)
await robot.turn_left(135)
await robot.turn_left(-45)
await robot.move(230)
await robot.turn_left(135)
await robot.turn_left(-45)
await robot.move(265)
await robot.turn_left(135)
await robot.turn_left(-40)
await robot.move(230)
await robot.turn_left(135)
await robot.turn_left(-45)
