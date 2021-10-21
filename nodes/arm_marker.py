#!/usr/bin/env python3
# ArmMarker Node
# RKS

# Project imports

# Python imports

# 3rd-party imports
import rospy
import tf2_ros
from visualization_msgs.msg import Marker

class ArmMarker:
    """
    """
    def __init__(self):
        """
        Constructor of ROS Node ArmMarker class. Creates all ROS 
        interfaces(subscriber, publisher, etc) as well as internal variable
        for calculations.

        Public members
        float: period ~ number of second to complete trajectory
        """
        # Pull params
        rospy.init_node('arm_marker')
        self.period = rospy.get_param("homework2/twoarm/T")
        self._pub_rate = rospy.get_param('~pub_freq', default=5)
        # set up Publisher
        self._pub = rospy.Publisher('visualization_marker', Marker, queue_size=1)
        # set up Listener
        self._tfBuffer = tf2_ros.Buffer()
        self._listener = tf2_ros.TransformListener(self._tfBuffer)
        # set up init Marker
        self._marker_msg = Marker()
        self._marker_msg.ns = "ee"
        self._marker_msg.id = 0
        self._marker_msg.action = Marker.ADD
        self._marker_msg.lifetime = rospy.Duration(self.period/5)
        # set up Main loop
        self._time_delta = 1./self._pub_rate
        rospy.Timer(rospy.Duration(self._time_delta), self.main_loop)
        rospy.spin()

    
    def main_loop(self, event):
        """
        Main execution loop of arm marker node

        Args:
            event: A rospy.Timer event
        """
        try:
            trans = self._tfBuffer.lookup_transform("base_link", "end_effector", rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, 
            tf2_ros.ExtrapolationException):
            #End function early
            return None

        self._marker_msg.header.stamp = rospy.Time.now()
        if (trans.transform.translation.x > 0):
            self._marker_msg.type = Marker.SPHERE
            self._marker_msg.color = [0,.8,0,1]
        else:
            self._marker_msg.type = Marker.CUBE
            self._marker_msg.color = [.5,0,.5,1]

        self._marker_msg.pose.position.x = trans.transform.translation.x
        self._marker_msg.pose.position.y = trans.transform.translation.y

        self._pub.publish(self._marker_msg)


# Main execution loop
if __name__ == "__main__":
    try:
        arm_marker = ArmMarker()
    #If something kills this node, have it die
    except rospy.ROSInterruptException:
        pass
