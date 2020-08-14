#!/usr/bin/python
import rospy
import cv2
import numpy as np
import math as m

import tf

from std_msgs.msg import Header

from geometry_msgs.msg import Pose, PoseWithCovarianceStamped, Point, Quaternion, Twist, PoseStamped
from nav_msgs.msg import Path, Odometry

from tf.transformations import euler_from_quaternion, quaternion_from_euler


def get_aruco_shit():
    # Node init 
    rospy.init_node('read_tf', anonymous = True)
    pub_pose = rospy.Publisher("aruco_pose", Pose, queue_size = 100)

    my_pose = Pose()


    # Publisher definition
    rate = rospy.Rate(30) # 30hz

    #print("Start node")
    rospy.loginfo("TF reader -> is run")
    listener = tf.TransformListener()
    listener.waitForTransform('/base_link', '/marker_frame', rospy.Time(), rospy.Duration(4.0))

    try:
        while not rospy.is_shutdown():

            (trans,rot) = listener.lookupTransform('/base_link', '/marker_frame', rospy.Time(0))

            
            my_pose.position.x = trans[0]
            my_pose.position.y = trans[1]
            my_pose.position.z = trans[2]

            my_pose.orientation.x = rot[0]
            my_pose.orientation.y = rot[1]
            my_pose.orientation.z = rot[2]
            my_pose.orientation.w = rot[3]
                

            #my_path.poses.append(pose)

            
            print("trans: ", trans)  
            #callback(trans, rot)

            # Get data from cameras
            rate.sleep()
    except:
        print("it's over")
        print(my_pose)
        while not rospy.is_shutdown():
            print("haha")
            pub_pose.publish(my_pose)
            rospy.Rate(2).sleep()
    
get_aruco_shit()
