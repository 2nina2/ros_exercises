import rospy
from std_msgs.msg import String

if __name__ == '__main__':
  try:
    rate = rospy.Rate(20)
    pub = ("my_random_float", Float32)
    rospy.init_node("simple_publisher",anonymous=True))
    while not rospy.is_shutdown():
      num = 
