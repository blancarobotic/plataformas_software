#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node("publicador_6")
pub=rospy.Publisher("/contador", Int32, queue_size=1)
rate=rospy.Rate(2)

contador=Int32()


while not rospy.is_shutdown():
    contador.data=int(input("dame un numero: "))
    pub.publish(contador)
    rate.sleep()