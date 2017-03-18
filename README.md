Run
```
roslaunch frequency_test test_performance.launch
```

Add following variables in ```rqt_plot``` to view the message loss for each channel
```
/py2py/freq/loss
/py2cpp/freq/loss
/cpp2py/freq/loss
/cpp2cpp/freq/loss
```

Add following variables in ```rqt_plot``` to view the output frequency for each channel
```
/py2py/freq/freq
/py2cpp/freq/freq
/cpp2py/freq/freq
/cpp2cpp/freq/freq
```

You can modify the message generating rate by editing 
```
double publish_rate = ... ;
```
in ```talker.cpp``` or 

```
publish_rate = ...
``` 
in ```talker.py```

Sample outputs with a message generating frequency linear to time can be seen in ```result```
