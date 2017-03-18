#include <time.h>
#include "ros/ros.h"
#include "frequency_test/Freq.h"
#include "frequency_test/SuperAwesome.h"

int64_t prev_msg = 0; 
double nRecv = 0; // number of received messages in each time interval
double start_time; 
ros::Publisher pub; 

void chatterCallback(const frequency_test::SuperAwesome::ConstPtr& SuperAwesomeData)
{
  double current_time = ros::Time::now().toSec();
  double dt = current_time - start_time;
  
  double time_interval = 3; // calculate message receiving frequency every 3 seconds
  nRecv++;
  if (dt > time_interval) {
    start_time = current_time;
    int64_t current_msg = SuperAwesomeData->count;
	int64_t nSent = current_msg - prev_msg;
    double hz = nSent / time_interval; // message receiving frequency
    double info_loss = 1 - nRecv / nSent; // message loss rate via transmition
    nRecv = 0;
    prev_msg = current_msg;
	frequency_test::Freq freq_msg;
    freq_msg.freq = hz;
    freq_msg.loss = info_loss;
    pub.publish(freq_msg);
  }
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "listener");
  ros::NodeHandle n;
  start_time = ros::Time::now().toSec();

  pub = n.advertise<frequency_test::Freq>("freq", 1000);

  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

  ros::spin();

  return 0;
}

