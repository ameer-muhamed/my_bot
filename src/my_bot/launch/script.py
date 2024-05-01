#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_robot(pub, linear_speed, angular_speed, duration):
    twist = Twist()
    twist.linear.x = linear_speed
    twist.angular.z = angular_speed

    start_time = rospy.Time.now().to_sec()
    while (rospy.Time.now().to_sec() - start_time) < duration:
        pub.publish(twist)

    # Stop the robot
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)

def main():
    rospy.init_node('move_robot_node', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.sleep(1)  # Wait for the publisher to initialize

    try:
        # Move straight for 10 meters
        move_robot(pub, linear_speed=0.2, angular_speed=0.0, duration=50.0)

        # Turn left by 45 degrees
        move_robot(pub, linear_speed=0.0, angular_speed=0.5, duration=5.0)

    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()

