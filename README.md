# Turtle Rectangle Drawer

This ROS package controls a TurtleSim simulation to move the turtle in a rectangular path. The turtle follows the specified width and height, starting from its initial position, and makes 90-degree turns to complete a rectangle.

## Requirements

- **ROS Noetic** (with `turtlesim` package installed)
- **Python 3**

## Installation

1. **Install Turtlesim Package** (if not already installed)

    ```bash
    sudo apt-get install ros-noetic-turtlesim
    ```

2. **Create a Catkin Workspace** (if you haven't already)

    ```bash
    mkdir -p ~/ros_ws/src
    cd ~/ros_ws/src
    catkin_init_workspace
    ```

3. **Clone this Repository**

    ```bash
    cd ~/ros_ws/src
    git clone https://github.com/your_username/turtle_rectangle_drawer.git
    ```

4. **Build the Package**

    ```bash
    cd ~/ros_ws
    catkin_make
    source devel/setup.bash
    ```

## Running the Rectangle Drawer

1. **Start ROS Core** (in Terminal 1)

    ```bash
    roscore
    ```

2. **Launch Turtlesim** (in Terminal 2)

    ```bash
    rosrun turtlesim turtlesim_node
    ```

3. **Run the Rectangle Script** (in Terminal 3)

    ```bash
    rosrun turtle_rectangle_drawer draw_rectangle.py
    ```

This will guide the turtle through a rectangular path of specified width and height.

## Code Overview

- `draw_rectangle(width, height)`: Main function that moves the turtle in a rectangle with the specified width and height.
    - **Parameters**:
      - `width`: Length of the rectangle's width side (in meters).
      - `height`: Length of the rectangle's height side (in meters).
