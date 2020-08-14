#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
import tf


def all_close(goal, actual, tolerance):

    """
    Convenience method for testing if a list of values are within a tolerance of their counterparts in another list
    @param: goal       A list of floats, a Pose or a PoseStamped
    @param: actual     A list of floats, a Pose or a PoseStamped
    @param: tolerance  A float
    @returns: bool
    """
    all_equal = True
    if type(goal) is list:
      for index in range(len(goal)):
        if abs(actual[index] - goal[index]) > tolerance:
          return False

    elif type(goal) is geometry_msgs.msg.PoseStamped:
      return all_close(goal.pose, actual.pose, tolerance)

    elif type(goal) is geometry_msgs.msg.Pose:
      return all_close(pose_to_list(goal), pose_to_list(actual), tolerance)

    return True

def callback(data,args):
  print("hello there")
  ur_robot = args[0]
  ur_scene = args[1]
  ur_move_group = args[2]
  ur_planning_frame = args[3]
  ur_eef_link = args[4]
  ur_group_names = args[5]

  move_group = ur_move_group
  
  print("elo grab") 
  print(data)
  data.position.x = data.position.x - 0.05
  data.position.y = data.position.y - 0.03
  data.position.z = 0.15
  data.orientation.x = -0.0
  data.orientation.y = 1.0
  data.orientation.z = 0.0
  data.orientation.w = -0.0


  move_group.set_pose_target(data)

  plan = move_group.go(wait=True)
  move_group.stop()
  move_group.clear_pose_targets()
  current_pose = move_group.get_current_pose().pose
  return all_close(data, current_pose, 0.01)


def main():
  try:
    print("Grab")
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"
    move_group = moveit_commander.MoveGroupCommander(group_name)

    planning_frame = move_group.get_planning_frame()
    
    eef_link = move_group.get_end_effector_link()

    group_names = robot.get_group_names()
    robot.get_current_state()

    # Misc variables    
    ur_robot = robot
    ur_scene = scene
    ur_move_group = move_group
    ur_planning_frame = planning_frame
    ur_eef_link = eef_link
    ur_group_names = group_names

    rospy.init_node('move_ur_python_interface', anonymous=True)
    rospy.Subscriber("/aruco_pose",geometry_msgs.msg.Pose,callback,(ur_robot,
                                                                     ur_scene,
                                                                     ur_move_group,
                                                                     ur_planning_frame,
                                                                     ur_eef_link,
                                                                     ur_group_names))
    rospy.spin()
  except rospy.ROSInterruptException:
      return
  except KeyboardInterrupt:
      return


if __name__ == '__main__':
  main()