#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

sumatorio=Int32()
sumatorio.data=0
tope=Int32()
tope.data=0

def callback(msg):

    global sumatorio,tope #establecemos las variables globales

    if tope.data>11:
        print(sumatorio.data)
        sumatorio.data=0
        tope.data=0
    
    sumatorio.data=sumatorio.data+msg.data
    tope.data+=1

rospy.init_node("subscriptor_ejercicio8") #inicializamos el nodo
sub=rospy.Subscriber("/contador",Int32,callback) #nos subscribimos al topic del ejercicio 6
rospy.spin()