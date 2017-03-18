#!/usr/bin/env python

import rospy
import time
from frequency_test.msg import SuperAwesome, Freq


def callback(SuperAwesomeData):
    global start_time
    global prev_msg
    global nRecv # number of messages received for each time interval
    nRecv += 1

    current_time = time.time()
    dt = current_time - start_time
    
    current_msg = SuperAwesomeData.count
    time_interval = 3 # count every 3 seconds
    if dt > time_interval:
        start_time = current_time
        nSent = current_msg - prev_msg
        hz = nSent / time_interval # message receiving frequency 
        info_loss = 1 - nRecv / float(nSent) # message loss rate
        nRecv = 0
        prev_msg = current_msg
        freq_msg = Freq()
        freq_msg.freq = hz
        freq_msg.loss = info_loss
        pub.publish(freq_msg)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', SuperAwesome, callback)
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('freq', Freq, queue_size=1)
    nRecv = 0
    prev_msg = 0
    start_time = time.time()
    listener()

