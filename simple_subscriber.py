#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import Float32

def callback(data):
  num = math.log(data.data)
  pub = rospy.Publisher("random_float_log", Float32, queue_size=10)
  rospy.loginfo("got log %s", num)
  pub.publish(num)

if __name__ == '__main__':
  rospy.init_node('simple_subscriber')
  rospy.Subscriber("my_random_float", Float32, callback)
  rospy.spin()
