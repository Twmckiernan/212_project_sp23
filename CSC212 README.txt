Create 3 Robot set up: 
In order to set up the device for use this comes in two main parts.


PART 1: Firmware update 
1. Take the Create 3 robot out of the box and place it on the charging dock to turn it on
2. Once you hear the activation sound ( in roughly 1-3 minutes )  locate the two buttons on the roomba located on either side of the main power button
3. Press and hold the 2 buttons for 20-30 seconds until the colored ring on the bot turns blue and the bot chimes.
4. On your laptop connect to the bots wifi signal ( EX NAME: CREATE ABC)
5. Once connected go to 192.168.10.1
6. At the top of the screen locate the “UPDATE” header and click on it
7. Now click “Update Firmware” There are two different firmwares, Galactic and Humble, update both.


PART 2: Wifi and Bluetooth connection
1. Repeat steps 1-5 from part 1
2.  Got to the “CONNECT” header 
3. Give your robot a unique name and device ID
4. Then scroll down to “CONNECT NETWORK”
5. Type in the Wifi Name and password into correct fields and hit connect
6. Wait for your robot to connect, if the bot connected to the wifi properly you should hear the start-up chime
7. Go to https://python.irobot.com/ to access virtual playground 
8. Hit “CONNECT” 
9. In the bot that pops up find your robots unique ID
10. Click on “PAIR” 
11. If worked correctly the Web player will no longer have a connect box but one that reads “Disconnect”
You have now successfully updated your bot and are ready to start testing your Create 3’s capabilities


















 Basic Raspberry Pi Setup: 
1. Go to https://www.raspberrypi.com/software/ for the windows Raspberry Pi imager 
2. Download the Raspberry Pi imager on a computer with an SD slot or microSD slot
3. Choose Raspberry Pi 64-bit OS as the operating system, the microSD as the storage and then write.
4. Insert the micro sd card into your raspberry pi and let it read the card
5. Connect a display, keyboard and mouse to the Pi to continue set up
6. Connect the pi to the adapter board on the roomba ( located in the tray) 
7. Note:  Turn the switch on the adapter board from Bluetooth to usb
8. Open the network settings in the top right of the imager and connect it to the same wifi as the roomba.
Swap file set up: 
1. sudo fallocate -l 8G /swapfile
2. sudo dd if=/dev/zero of=/swapfile bs=1M count=2048
3. Set the file permissions of the swapfile to 600 to restrict access to the file:
   1. sudo chmod 600 /swapfile
4. Use the following command to format the swapfile as a swap space:
   1. sudo mkswap /swapfile 
5. Activate the swapfile by using the following command:
   1. sudo swapon /swapfile
6. To make the swapfile permanent across reboots, add the following line to the /etc/fstab file:
   1. /swapfile swap swap defaults 0 0
   2. sudo nano /etc/fstab
   3. Type control-o and enter to save.
7. Control-x to exit
Docker set up: 
1. Run sudo apt-get update && sudo apt-get upgrade
2. Run curl -fsSL https://get.docker.com -o get-docker.sh
   1. sudo sh get-docker.sh
3. Run the previous 2 commands one after another (2 and 2 A)
4. Run “sudo usermod -aG docker pi1 “to make yourself a Rootless user ( essentially an admin) 
5. Restart your Pi
6. To make sure your docker install worked correctly run “ hello world”
7. If this ran without an issue you are ready to move on
Creating a Dockerfile to install ROS package:
1. To create ROS docker images and install custom packages, follow the steps below
Dockerfile
___________________________________________
FROM arm64v8/ros:foxy
# install ros package
RUN apt-get update && apt-get install -y \
ros-${ROS_DISTRO}-demo-nodes-cpp \
ros-${ROS_DISTRO}-demo-nodes-py && \
rm -rf /var/lib/apt/lists/* \
rm /etc/ros/rosdep/sources.list.d/20-default.list
# launch ros package
CMD ["ros2", "launch", "demo_nodes_cpp", "talker_listener.launch.py"]
___________________________________________


2. docker build -t create3/ros:app .
3. docker run -it --network=host --privileged -e DISPLAY=$DISPLAY create3/ros:app bash
You should see a list of ros2 API from Roomba: 
root@raspberrypi:/# ros2 topic list
/battery_state
/cmd_audio
/cmd_lightring
/cmd_vel
/dock
/hazard_detection
/imu
/interface_buttons
/ir_intensity
/ir_opcode
/kidnap_status
/mobility_monitor/transition_event
/mouse
/odom
/parameter_events
/robot_state/transition_event
/rosout
/slip_status
/static_transform/transition_event
/stop_status
/tf
/tf_static
/wheel_status
/wheel_ticks
/wheel_vels
root@raspberrypi:/#
Set up xhost on raspberry pi for rvis
Running docker ps in a new terminal.
xhost +local:docker:CONTAINER_ID