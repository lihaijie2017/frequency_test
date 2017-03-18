#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String
from frequency_test.msg import SuperAwesome

def talker():
    global start_time
    pub = rospy.Publisher('chatter', SuperAwesome, queue_size=10)
    rospy.init_node('talker', anonymous=True)

    # 'count' stores the total number of message generated and sent via talker.py
    count = 0
    while not rospy.is_shutdown():
        # customize publish rate (linear to time)
        publish_rate = (time.time() - start_time) * 200 + 1
        rate = rospy.Rate(publish_rate)

        message = SuperAwesome()
        message.data = "Super"
        message.count = count
        
        pub.publish(message)
        count += 1
        rate.sleep()

if __name__ == '__main__':
    start_time = time.time()
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

