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
    rospy.init_node("dynamic_tf_cam_publisher")
    br = tf2_ros.TransformBroadcaster()
    rate = rospy.Rate(20)
    tfBuffer = tf2_ros.Buffer()
    lcam = rospy.Publisher('leftt_camera', geometry_msgs.msg.PoseStamped, queue_size=10)
    #rcam = rospy.Publisher("right_cam",
    listener = tf2_ros.TransformListener(tfBuffer)
    while not rospy.is_shutdown():
      transform = geometry_msgs.msg.TransformStamped()
      transform.header.stamp = rospy.Time.now()
      transform.header.frame_id = "world"
      transform.child_frame_id = "left_cam"
      #transform.transform.rotation.w = 1
      t = transform.header.stamp.to_sec()
      try:
        transform_old = tfBuffer.lookup_transform("world","base_link_gt", rospy.Time())
        q = [transform_old.transform.rotation.x, transform_old.transform.rotation.y, transform_old.transform.rotation.z, transform_old.transform.rotation.w]
        R = tf.transformations.quaternion_matrix(q)
        p = np.array([[transform_old.transform.translation.x], [transform_old.transform.translation.y], [transform_old.transform.translation.z], [1]])
        T = np.hstack((R[:,0:3], p))
        pose = np.array([[1,0,0,-.05],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        left_t = np.matmul(T, pose)

        q_left = tf.transformations.quaternion_from_matrix(left_t)
        transform.transform.translation.x = left_t[0,3]
        transform.transform.translation.y = left_t[1,3]
        transform.transform.translation.z = left_t[2,3]
        transform.transform.rotation.w = q_left[3]

        transform.transform.rotation.x = q_left[0]
        transform.transform.rotation.y = q_left[1]
        transform.transform.rotation.z = q_left[2]

        transform2 = geometry_msgs.msg.TransformStamped()
        transform2.header.stamp = rospy.Time.now()
        transform2.header.frame_id = "left_cam"
        transform2.child_frame_id = "right_cam"
      #transform.transform.rotation.w = 1
        transform2.transform.translation.x = .1
        transform2.transform.translation.y = 0
        transform2.transform.translation.z = 0
        transform2.transform.rotation.w = 1
        transform2.transform.rotation.x = 0
        transform2.transform.rotation.y = 0
        transform2.transform.rotation.z = 0


        #transform_old.transform.translation.x = transform_old.transform.translation.x - .05
        #transform.transform = transform_old.transform
        #transform.transform.translation.x = transform.transform.translation.x - .05 
        #p = geometry_msgs.msg.PoseStamped()
        #p.pose.position.x = -.05
        #p.pose.position.y = 0
        #p.pose.position.z = 0
        #pose_transformed = tf2_geometry_msgs.do_transform_pose(transform, transform_old)
        #rcam =  
        
        
        #lcam.publish(pose_transformed)
        #t = geometry_msgs.msg.TransformStamped()
        #t.transform.translation = pose_transformed.position
        #t.transform.rotation = pose.orientation
      #rcam = geometry_msgs.msg.TransformStamped()
      #rcam.header.stamp = rospy.Time.now()
      
      #rcam.header.frame_id = "world"
      #rcam.child_frame_id = "left_cam"
      #t = transform.header.stamp.to_sec()
        br.sendTransform(transform)
        br.sendTransform(transform2)
        #transform_old.transform.translation.x = transform_old.transform.translation.x + .1
      except(tf2_ros.LookupException):
        continue
      rate.sleep()
  except rospy.ROSInterruptException:
    pass

