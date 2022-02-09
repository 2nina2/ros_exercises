#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import Float32, String
from sensor_msgs.msg import LaserScan
from ros_exercises.msg import OpenSpace

def callback(data):
  long_r = 0
  long_ang = math.pi*(2/3.)
  for i in range(len(data.ranges)):
    if long_r < data.ranges[i]:
        long_r = data.ranges[i]
        long_ang = math.pi*(2/3.) + i*(math.pi/300.)
  msg = OpenSpace()
  msg.angle = long_ang
  msg.distance = long_r

  #pub1.publish(long_r)
  #pub2.publish(long_ang)
  pub3.publish(msg)

if __name__ == '__main__':
  rospy.init_node('open_space_publisher')
  rospy.Subscriber(rospy.get_param('~subscriber_topic'), LaserScan, callback)
  #pub1 = rospy.Publisher(rospy.get_param('~pub_topic_dist',"open_space/distance"), Float32, queue_size=10)
  #pub2 = rospy.Publisher(rospy.get_param('~pub_topic_ang'), Float32, queue_size=10)
  pub3 = rospy.Publisher(rospy.get_param('~pub_topic_msg'), OpenSpace, queue_size =10) 
  rospy.spin()
