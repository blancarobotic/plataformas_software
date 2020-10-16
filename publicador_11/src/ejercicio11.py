#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    dist_maxima=max(msg.ranges)
    dist_minima=min(msg.ranges)
    angulo_dist_min=msg.ranges.index(dist_minima)*0.090625
    angulo_dist_max=msg.ranges.index(dist_maxima)*0.090625
    arcos=[(0, 100), (10, 110), (20, 120), (30, 130), (40, 140), (50, 150), (60, 160), (70, 170), (80, 180), (90, 190), (100, 200), (110, 210), (120, 220), (130, 230), (140, 240), (150, 250), (160, 260), (170, 270), (180, 280), (190, 290), (200, 300), (210, 310), (220, 320), (230, 330), (240, 340), (250, 350), (260, 360), (270, 370), (280, 380), (290, 390), (300, 400), (310, 410), (320, 420), (330, 430), (340, 440), (350, 450), (360, 460), (370, 470), (380, 480), (390, 490), (400, 500), (410, 510), (420, 520), (430, 530), (440, 540), (450, 550), (460, 560), (470, 570), (480, 580), (490, 590), (500, 600), (510, 610), (520, 620), (530, 630), (540, 640)]
    distancias=[[] for _ in range(55)]
    
    for i in range(len(arcos)):
        for j in range(arcos[i][0],arcos[i][1]):
            grande=0.10
            actual=msg.ranges[j]
            if grande<actual:
                grande=actual
        distancias[i].append(grande)
    
    print "distancia maxima: ",dist_maxima,"angulo: ",angulo_dist_max,"\n"
    print "distancia minima: ",dist_minima,"angulo: ",angulo_dist_min
    print "mayor arco libre: ",(arcos[distancias.index(max(distancias))][0])*0.090625,"////",(arcos[distancias.index(max(distancias))][1])*0.090625
    
    
rospy.init_node("distancia11")
sub=rospy.Subscriber("/kobuki/laser/scan",LaserScan,callback)
rospy.Rate(2)
rospy.spin()