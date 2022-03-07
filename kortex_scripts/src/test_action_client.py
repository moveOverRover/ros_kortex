#! /usr/bin/env python

import rospy
import time
import actionlib
from kortex_scripts.msg import CustomActionMsgGoal, CustomActionMsgResult, CustomActionMsgFeedback, CustomActionMsgAction

def feedback_callback(feedback):
    print(feedback)

rospy.init_node('kortex_action_client')
client = actionlib.SimpleActionClient('/action_custom_msg_as', CustomActionMsgAction)
client.wait_for_server()
print("connected to server")

goal = CustomActionMsgGoal()
goal.path = "/my_gen3/camera/color/image_raw"
goal.data = ""
goal.num_codes = 2

client.send_goal(goal, feedback_cb=feedback_callback)
#client.wait_for_result()

state_result = client.get_state()
rospy.loginfo("state_result: "+str(state_result))

#client.cancel_goal()

while state_result < 2:
    
    state_result = client.get_state()
    rospy.loginfo("state_result: "+str(state_result))
    
    
print('[Result] State: %d'%(client.get_state()))