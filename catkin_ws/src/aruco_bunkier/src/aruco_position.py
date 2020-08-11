#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Vector3Stamped

def callback(data):
    print("X: ",data.vector.x)
    print("Y: ",data.vector.y)
    print("Z: ",data.vector.z)
    
def aruco_position():

    rospy.init_node('aruco_position', anonymous=True)

    rospy.Subscriber("/aruco_single/position", Vector3Stamped, callback)

    rospy.spin()

if __name__ == '__main__':
    aruco_position()
