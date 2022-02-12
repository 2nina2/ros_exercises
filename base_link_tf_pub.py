#!/usr/bin/env python
import rospy, random
from std_msgs.msg import Float32
import tf2_ros
import tf
import geometry_msgs.msg
import numpy as np
import tf2_geometry_msgs 

if __name__ == '__main__':
  try:
    rospy.init_node("base_link_tf_pub")
    br = tf2_ros.TransformBroadcaster()
    rate = rospy.Rate(20)
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    while not rospy.is_shutdown():
      transform = geometry_msgs.msg.TransformStamped()
      transform.header.stamp = rospy.Time.now()
      transform.header.frame_id = "world"
      transform.child_frame_id = "base_link_gt_2"
      t = transform.header.stamp.to_sec()
      try:
        transform_old = tfBuffer.lookup_transform("world","left_cam", rospy.Time())
        q = [transform_old.transform.rotation.x, transform_old.transform.rotation.y, transform_old.transform.rotation.z, transform_old.transform.rotation.w]
        R = tf.transformations.quaternion_matrix(q)
        p = np.array([[transform_old.transform.translation.x], [transform_old.transform.translation.y], [transform_old.transform.translation.z], [1]])
        T = np.hstack((R[:,0:3], p))
        pose = np.array([[1,0,0,.05],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        left_t = np.matmul(T, pose)

        q_left = tf.transformations.quaternion_from_matrix(left_t)
        transform.transform.translation.x = left_t[0,3]
        transform.transform.translation.y = left_t[1,3]
        transform.transform.translation.z = left_t[2,3]
        transform.transform.rotation.w = q_left[3]

        transform.transform.rotation.x = q_left[0]
        transform.transform.rotation.y = q_left[1]
        transform.transform.rotation.z = q_left[2]

        br.sendTransform(transform)
      except(tf2_ros.LookupException):
        continue
      rate.sleep()
  except rospy.ROSInterruptException:
    pass

