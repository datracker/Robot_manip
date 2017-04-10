#!/usr/bin/env python

import numpy as np
import rospy
import math

from visualization_msgs.msg import Marker
#from visualization_msgs.msg import MarkerArray
#from geometry_msgs.msg import Point
#from sensor_msgs.msg import JointState

def cube_pub():
    rospy.init_node("cube_joint", anonymous=True)
    pub = rospy.Publisher("joint_state", Marker, queue_size=10)
    rate = rospy.Rate(1)

    #rospy.loginfo(cube)
    while not rospy.is_shutdown():        
        cube = Marker()
        cube.header.frame_id = "/base_link"
        cube.header.stamp = rospy.get_time()
        cube.ns = "cube_namespace"
        cube.id = 0
        cube.type = Marker.CUBE
        cube.action = Marker.ADD

        cube.pose.position.x = 0.5
        cube.pose.position.y = 1.0
        cube.pose.position.z = 1.5

        #cube.pose.orientation.x = 0.0
        #cube.pose.orientation.y = 0.0
        #cube.pose.orientation.z = 0.0
        #cube.pose.orientation.w = 1.0

        cube.scale.x = 1
        cube.scale.y = 1
        cube.scale.z = 1

        cube.color.a = 1.0
        cube.color.r = 256.0
        cube.color.g = 256.0
        cube.color.b = 256.0

        #cube.mesh_resource = "package://pr2_description/meshes/base_v0/base.dae"
        #vis_pub.publish(cube)

        rospy.loginfo(cube)
        pub.publish(cube)
        rate.sleep()

if __name__ == '__main__':
    try:
        cube_pub()
    except rospy.ROSInterruptException:
        pass
