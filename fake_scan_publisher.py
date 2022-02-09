#!/usr/bin/env python
import rospy, math, random
from sensor_msgs.msg import LaserScan
from random import uniform


if __name__ == '__main__':
  try:
    rospy.init_node("fake_scan_publisher")
    rate = rospy.Rate(20)
    pub = rospy.Publisher("fake_scan", LaserScan, queue_size = 10)
    scann = LaserScan()
    while not rospy.is_shutdown():
      curr_time = rospy.Time.now()
      scann.header.stamp = curr_time
      scann.header.frame_id = "base_link"
      scann.angle_min = math.pi*(-2/3.)
      scann.angle_max = math.pi*(2/3.)
      scann.angle_increment = math.pi/300.
      scann.range_min = 1
      scann.range_max = 10.0
      scann.scan_time = .05
      ranges = []
      length = int((scann.angle_max - scann.angle_min)/scann.angle_increment) + 1
      for i in range(length):
        ranges.append(uniform(scann.range_min,scann.range_max))
      scann.ranges = ranges
      print(scann)
      pub.publish(scann)
      rate.sleep()
  except rospy.ROSInterruptException:
    pass

