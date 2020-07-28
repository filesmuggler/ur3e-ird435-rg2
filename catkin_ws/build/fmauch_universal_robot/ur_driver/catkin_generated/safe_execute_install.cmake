execute_process(COMMAND "/home/krzysztof/Repos/ur3e-ird435-rg2/catkin_ws/build/fmauch_universal_robot/ur_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/krzysztof/Repos/ur3e-ird435-rg2/catkin_ws/build/fmauch_universal_robot/ur_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
