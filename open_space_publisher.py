#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan

def callback(data):
  pub1 = rospy.Publisher("open_space/distance", Float32, queue_size=10)
  pub2 = rospy.Publisher("open_space/angle", Float32, queue_size=10)
  long_r = 0
  long_ang = math.pi*(2/3.)
  for i in range(len(data.ranges)):
    if long_r < data.ranges[i]:
        long_r = data.ranges[i]
        long_ang = math.pi*(2/3.) + i*(math.pi/300.)
  pub1.publish(long_r)
  pub2.publish(long_ang)

if __name__ == '__main__':
  rospy.init_node('open_space_publisher')
  rospy.Subscriber("fake_scan", LaserScan, callback)
  rospy.spin()
