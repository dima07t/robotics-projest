# robotics-projest
# TurtleBot3 SLAM Robotics Project

## Project Overview
This project demonstrates a robotics SLAM pipeline using TurtleBot3 Burger in a Gazebo simulation environment with ROS 2 Jazzy.

The robot is launched in a virtual environment, controlled manually using keyboard teleoperation, and used to generate a 2D occupancy grid map with Cartographer SLAM. The generated map is visualized in RViz and saved for further robotics applications.

## Objective
The objective of this project is to simulate a mobile robot and perform real-time environment mapping using SLAM.

## Technologies Used
- ROS 2 Jazzy
- Gazebo
- TurtleBot3 Burger
- Cartographer SLAM
- RViz2
- Navigation Map Saver
- Ubuntu 24.04
- VirtualBox

## Implemented Features
- TurtleBot3 robot simulation in Gazebo
- Manual teleoperation using keyboard
- Real-time SLAM mapping
- Map visualization in RViz2
- Saving the generated occupancy grid map

## My Contribution
This project was implemented by configuring and integrating existing robotics frameworks in ROS 2. My contribution includes:
- setting up Ubuntu and ROS 2 Jazzy
- installing TurtleBot3, Gazebo, Cartographer, and RViz
- launching the simulation environment
- controlling the robot manually
- generating the SLAM map
- visualizing the map in RViz2
- saving the final map
- organizing the project structure and uploading it to GitHub

## Project Structure
```text
turtlebot3-slam-robotics-project/
├── README.md
├── requirements.md
├── project_description.md
├── .gitignore
├── my_map.yaml
├── my_map.pgm
├── screenshots/
└── scripts/
How to Run the Project
1. Launch Gazebo simulation
source /opt/ros/jazzy/setup.bash
export TURTLEBOT3_MODEL=burger
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
2. Launch Cartographer SLAM
source /opt/ros/jazzy/setup.bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
3. Launch RViz
source /opt/ros/jazzy/setup.bash
rviz2 -d /opt/ros/jazzy/share/turtlebot3_cartographer/rviz/tb3_cartographer.rviz
4. Launch keyboard teleoperation
source /opt/ros/jazzy/setup.bash
ros2 run turtlebot3_teleop teleop_keyboard
5. Save map
source /opt/ros/jazzy/setup.bash
ros2 run nav2_map_server map_saver_cli -f my_map

Output

The final output of the project is a 2D occupancy grid map saved as:

my_map.pgm

my_map.yaml

Notes

This project was tested inside a VirtualBox environment. Since Gazebo and SLAM were executed in a virtual machine, simulation performance may be lower than on native Linux. This may introduce mapping noise, but the full robotics pipeline remains functional.

Conclusion

This project demonstrates a complete robotics simulation workflow in ROS 2, including robot launch, manual control, SLAM mapping, RViz visualization, and map saving. It shows practical understanding of robotics system integration rather than low-level algorithm implementation from scratch
