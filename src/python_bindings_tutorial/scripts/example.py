from moveit_ros_planning_interface._moveit_roscpp_initializer import roscpp_init
from std_msgs.msg import Int64
from python_bindings_tutorial import AddTwoInts

roscpp_init('node_name', [])
a = Int64(4)
b = Int64(2)
addtwoints = AddTwoInts()
sum = addtwoints.add(a, b)
sum