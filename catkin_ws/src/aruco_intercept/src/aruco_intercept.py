#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('aruco_xyz', String, queue_size=10)
    rospy.init_node('', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
def listener():
    rospy.init_node('interceptor', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()