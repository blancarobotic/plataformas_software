#!/usr/bin/env python

import rospy
from publicador.msg import datos

rospy.init_node('publicador_customizado')
pub=rospy.Publisher('/mensaje_personalizado',datos,queue_size=1)
rate=rospy.Rate(2)
mis_datos=datos()
mis_datos.edad=19
mis_datos.nombre="blanca"
mis_datos.coeficiente=5.5

while not rospy.is_shutdown():
    pub.publish(mis_datos)
    rate.sleep()