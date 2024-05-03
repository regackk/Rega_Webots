#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

nodeName='messagesucbscriber'
topicName='information'

def callbackFunction(message):
	print("We received %d"%message.data)

rospy.init_node(nodeName)

rospy.Subscriber(topicName, Int32, callbackFunction)

rospy.spin()