#!/usr/bin/env python
import rospy, math, random
from sensor_msgs.msg import LaserScan
from random import uniform


if __name__ == '__main__':
  try:
    rospy.init_node("fake_scan_publisher")
    rate = rospy.Rate(int(rospy.get_param('~rate')))
    pub = rospy.Publisher(rospy.get_param('~topic'), LaserScan, queue_size = 10)
    scann = LaserScan()
    while not rospy.is_shutdown():
      curr_time = rospy.Time.now()
      scann.header.stamp = curr_time
      scann.header.frame_id = "base_link"
      scann.angle_min = float(rospy.get_param('~angle_min'))
      scann.angle_max = float(rospy.get_param('~angle_max'))
      scann.angle_increment = float(rospy.get_param('~angle_incr'))
      scann.range_min = int(rospy.get_param('~range_min'))
      scann.range_max = int(rospy.get_param('~range_max'))
      scann.scan_time = float(rospy.get_param('~angle_incr'))
      ranges = []
      length = int((scann.angle_max - scann.angle_min)/scann.angle_increment) + 1
      for i in range(length):
        ranges.append(uniform(scann.range_min,scann.range_max))
      scann.ranges = ranges
      pub.publish(scann)
      rate.sleep()
  except rospy.ROSInterruptException:
    pass

