#!/usr/bin/env python
import rospy
import tf
import tf2_ros
import geometry_msgs.msg

if __name__ == '__main__':
  rospy.init_node('static_tf_cam_publisher')
  broadcaster = tf2_ros.StaticTransformBroadcaster()
  rcam = geometry_msgs.msg.TransformStamped()
  #broadcaster2 = tf2_ros.StaticTransformBroadcaster()
  #rcam.header.stamp = rospy.Time.now()
  rcam.header.frame_id = "base_link_gt"
  rcam.child_frame_id = "left_cam"
  rcam.transform.translation.x = -.05
  rcam.transform.translation.y = 0
  rcam.transform.translation.z = 0
  rcam.transform.rotation.x = 0
  rcam.transform.rotation.y = 0
  rcam.transform.rotation.z = 0
  rcam.transform.rotation.w = 1
  #broadcaster.sendTransform(rcam)
  lcam = geometry_msgs.msg.TransformStamped()
  #lcam.header.stamp = rospy.Time.now()
  lcam.header.frame_id = "base_link_gt"
  lcam.child_frame_id = "right_cam"
  lcam.transform.translation.x = .05
  lcam.transform.translation.y = 0
  lcam.transform.translation.z = 0
  lcam.transform.rotation.x = 0
  lcam.transform.rotation.y = 0
  lcam.transform.rotation.z = 0
  lcam.transform.rotation.w = 1
  broadcaster.sendTransform([rcam,lcam])
  rospy.spin()
