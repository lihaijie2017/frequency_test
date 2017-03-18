#!/usr/bin/env python

import rospy
import time
from frequency_test.msg import SuperAwesome, Freq


def callback(SuperAwesomeData):
    global start_time
    global prev_msg
    current_time = time.time()
    dt = current_time - start_time
    
    current_msg = SuperAwesomeData.count
    time_interval = 3
    if dt > time_interval:
        start_time = current_time
        hz = (current_msg - prev_msg) / time_interval
        prev_msg = current_msg
        freq_msg = Freq()
        freq_msg.freq = hz
        pub.publish(freq_msg)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', SuperAwesome, callback)
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('freq', Freq, queue_size=1)
    prev_msg = 0
    start_time = time.time()
    listener()

