#!/usr/bin/env python
import rospy, random
from std_msgs.msg import Float32
from random import uniform

if __name__ == '__main__':
  try:
    rospy.init_node("simple_publisher")
    rate = rospy.Rate(20)
    pub = rospy.Publisher("my_random_float", Float32, queue_size = 10)
    while not rospy.is_shutdown():
      num = uniform(1,10.0)
      rospy.loginfo("The random number is: %s",num)
      pub.publish(num)
      rate.sleep()
  except rospy.ROSInterruptException:
    pass

