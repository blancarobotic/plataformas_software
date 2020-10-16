#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def callback(msg):

    mover=Twist()

    distancia_delantera=msg.ranges[len(msg.ranges)/2]
    distancia_derecha=msg.ranges[0]
    distancia_izquierda=msg.ranges[len(msg.ranges)-1]

    if distancia_derecha<1:
        mover.angular.z=0.5
        pub.publish(mover)
        rate.sleep()
        mover.angular.z=0

    elif distancia_delantera>1 and msg.ranges[(len(msg.ranges)/2)+50]>1 and msg.ranges[(len(msg.ranges)/2)-50]>1:    
        mover.linear.x=0.5
        pub.publish(mover)
        rate.sleep()
        mover.linear.x=0

    elif distancia_izquierda<1:
        mover.angular.z=-0.5
        pub.publish(mover)
        rate.sleep()
        mover.angular.z=0


rospy.init_node("info_robot")
pub=rospy.Publisher('/cmd_vel',Twist,queue_size=1)
sub=rospy.Subscriber('/kobuki/laser/scan',LaserScan,callback)
rate=rospy.Rate(2)
rospy.spin()