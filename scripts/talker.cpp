#include <time.h>
#include "ros/ros.h"
#include "frequency_test/Freq.h"
#include "frequency_test/SuperAwesome.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "talker");
  ros::NodeHandle n;

  ros::Publisher chatter_pub = n.advertise<frequency_test::SuperAwesome>("chatter", 1000);

  
  double start_time = ros::Time::now().toSec();

  int count = 0; // stores the total number of messages generated and sent
  while (ros::ok())
  {
    double current_time = ros::Time::now().toSec();
    double dt = current_time - start_time;
    double publish_rate = dt * 200 + 1; // publish rate linear to time
    ros::Rate loop_rate(publish_rate);
    
    frequency_test::SuperAwesome message;
    message.data = "Super";
	message.count = count;

    chatter_pub.publish(message);
    ros::spinOnce();
    loop_rate.sleep();
    count++;
  }

  return 0;
}


