# ur3e-ird435-rg2
Object detection with Intel RealSense D435 and object manipulation with UR3e arm with OnRobot RG2

```
roslaunch ur_robot_driver ur3e_bringup_bunkier.launch robot_ip:=150.254.47.230   kinematics_config:=$(rospack find ur_calibration)/etc/ur3e_calibration_bunkier.yaml

roslaunch ur3e_d435_rg2_moveit ur3e_d435_rg2_moveit_planning_execution.launch

rosrun realsense_node_python realsense_point_cloud_ur3py
```

Moveit package has no dumb_link

TODO:
refactor dumb_link
regenerate moveit package with dumb link


ArUcO stuff

```
rosrun alsense_node_python realsense_rgb_depth_image_point_cloud.py

roslaunch aruco_bunkier aruco_marker_finder.launch markerId:=400 markerSize:=0.06

rosrun follower follower_node
```

TODO:
change frames for ur3e in aruco files

subscribe to aruco position


```
rosrun tf tf_echo /base_link /marker_frame
```


