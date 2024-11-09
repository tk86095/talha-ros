#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

def draw_rectangle(width, height):
    rospy.init_node('rectangle_mover', anonymous=True)
    cmd_vel_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    refresh_rate = rospy.Rate(10)

    move_cmd = Twist()

    # Speed settings for forward motion and turning
    linear_velocity = 0.5
    angular_velocity = 0.5

    def travel_distance(target_distance):
        move_cmd.linear.x = linear_velocity
        move_cmd.angular.z = 0.0
        traveled = 0.0
        while traveled < target_distance and not rospy.is_shutdown():
            cmd_vel_publisher.publish(move_cmd)
            traveled += linear_velocity / 10
            refresh_rate.sleep()
        move_cmd.linear.x = 0.0  # Stop moving forward
        cmd_vel_publisher.publish(move_cmd)

    def rotate_90_degrees():
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = angular_velocity
        turn_duration = 1.57 / angular_velocity
        start_time = time.time()
        while (time.time() - start_time) < turn_duration and not rospy.is_shutdown():
            cmd_vel_publisher.publish(move_cmd)
            refresh_rate.sleep()
        move_cmd.angular.z = 0.0  # Stop turning
        cmd_vel_publisher.publish(move_cmd)

    rospy.loginfo("Guiding the turtle in a rectangular path...")

    while not rospy.is_shutdown():
        # Traverse the rectangle path
        travel_distance(width)       # Move along the width
        rotate_90_degrees()          # Turn 90 degrees
        travel_distance(height)      # Move along the height
        rotate_90_degrees()          # Turn 90 degrees
        travel_distance(width)       # Move along the width again
        rotate_90_degrees()          # Turn 90 degrees
        travel_distance(height)      # Move along the height again
        rotate_90_degrees()          # Turn 90 degrees to complete the rectangle

if __name__ == '__main__':
    try:
        # Specify rectangle dimensions
        width = 2.0
        height = 1.0
        draw_rectangle(width, height)
    except rospy.ROSInterruptException:
        pass
