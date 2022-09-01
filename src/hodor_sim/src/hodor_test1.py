#!/usr/bin/env python

#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time
rospy.init_node('ebot_controller')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
vel = Twist()
rate = rospy.Rate(10)

vel.linear.x = 0.0
vel.linear.y = 0.0
vel.angular.z = 0.0
while not rospy.is_shutdown():
    vel.linear.x = 2.0
    vel.linear.y = 0.0
    vel.angular.z = 10.0
    # k = input("Enter a character")
    # if k == '1':
    #     vel.linear.x = 0.0
    #     vel.linear.y = 0.0
    #     vel.angular.z = 1.0
    #     print("Forward")
    #     time.sleep(30)
    # elif k == '2':
    #     vel.linear.x = 0.0
    #     vel.linear.y = 0.0
    #     vel.angular.z = -1.0
    # elif k == '3':
    #     vel.linear.x = 0.5
    #     vel.linear.y = 0.5
    #     vel.angular.z = 0.0
    # elif k == '4':
    #     vel.linear.x = 0.5
    #     vel.linear.y = -0.5
    #     vel.angular.z = 0.0
    # elif k == '5':
    #     vel.linear.x = 0.0
    #     vel.linear.y = 0.0
    #     vel.angular.z = 1.0
    # else:
    #     vel.linear.x = 0.0
    #     vel.linear.y = 0.0
    #     vel.angular.z = 0.0
    pub.publish(vel)
    rate.sleep()
