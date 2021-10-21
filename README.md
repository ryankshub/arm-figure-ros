# Homework 2 Package: Figure Skating Turtle and Rviz Arm

Author and Maintainer: **Ryan King-Shepard**

## **Description**
A package that shows 2 main functionalities: the turtle bot executing a 
figure 8 trajectory and providing a 2-DOF arm visualization in rviz

This package contains:

- nodes:
    1. `arm_marker` ~ Publishes a marker to represent the end-effector of 2-DOF arm
    2. `arm_traj` ~ Publishes joint angles that cause a 2-DOF arm to follow a trajectory 
    3. `simodom` ~ Performs a coordinate transform so turtle traversal of figure eight can 
        be simulated in turtlesim and rviz
    4. `trajectory` ~ Publishes velocity commands that allow turtle to perform figure 8 trajectory
- config:
    * `arm.yaml` ~ Contains parameters for 2-DOF visualization in rviz such link length, 
        arm thickness, and trajectory period. Loaded in namespace */homework2/twoarm/..* 
    * `trajectory.yaml` ~ Contains parameters for figure-8 turtle trajectory in rviz such as 
        width and height of figure 8, and trajectory period. Loaded in 
        namespace */homework2/fig8/..* 
- docs:
    * `TrajectoryDerivation.pdf` ~ Derivativation of the math behind the homework2 python package's
        math
- launch 
    * `arm_basics.launch` ~ Sets up visualization of 2-DOF arm in rviz
    * `arm_mark.launch` ~ Executes either gui-control or trajectory-control of 2-DOF arm. 
        *includes arm_basics.launch*
    * `figure_eight.launch` ~ Executes figure 8 turtle trajectory
- `package.xml`
    * Package configuration
- `CMakeLists.tx`
    * Build configuration
- rviz
    * `turtle_view.rviz` ~ Rviz configuration for figure 8 turtle trajectory
    * `twoarm.rviz` ~ Rviz configuration for the 2-DOF arm 
- `setup.py`
    * Setup for python packages
- src
    * `homework2` ~ Math package used to calculate figure 8 trajectory and velocity commands
- test
    * Test directory
- urdf
    * `twoarm.urdf.xacro` ~ URDF for links and joints of 2 DOF arm
- `README.md`
    * We meet again


## **Dependencies and Installation**

### *ROS Dependencies*
This package was developed and tested in ros-noetic. Homework2 is designed and should be built using catkin. This package also requires the turtlesim package to run. This should usually come with your ros installation, but to check this run: 
```bash
source /opt/ros/{ros-version}/setup.bash
rosrun turtlesim turtlesim_node
```
This should result a little screen with a turtle in the center. If the window doesn't pop up, refer to [ROS wiki](http://wiki.ros.org) to install turtlesim on your machine.

The full list of ros package dependencies can be found in `package.xml`.

### *Python Dependencies*
All code for this package was developed and test in Python 3 (specfically 3-8-10).  
This package requires `numpy` in order to run. The version used was 1-17.4, however there is no 
strong attachment to this version; other versions should work fine as long as they compatitble with
the python version. Refer to [Numpy docs](NUMPY SITE) for installation information. 

## **Execution**

### Figure 8 turtle trajectory
The `figure_eight.launch` controls the figure eight turtle trajectory.  
```bash
roslaunch homework2 figure_eight.launch [mode:=(sim or real)] [pub_freq:=freq]
```
The `mode` determines if a simulation using rviz and turtlesim should run or if velocity commands
are being sent to a real turtlebot. Set `mode` to `sim` for simulation or `real` for turtlebot interfacing. Examples of results are below:

Running `sim`:

https://user-images.githubusercontent.com/90436131/138294896-0b74be56-29c7-45f7-8263-720d015b4a9e.mp4

Running `real`:

https://user-images.githubusercontent.com/90436131/138296408-b520e8d8-0aaa-4497-bd3c-2331cf5ee285.mp4


Note: `mode` must be either `sim` or `real`; any other value will cause an error. If `mode` is
not provided, it's defaults to `sim`. 

The `pub_freq` determines the publishing rate of the velocity commands to the turtle. It's default 
value is 30Hz. The shape of the figure 8 and the speed at which it's completes can be controlled by 
adjusting the parameters in `trajectory.yaml`

Once the roslaunch is run, use the `resume` service to have the turtle start moving. To stop the turtle's movements, use the `pause` service. You can resume motion again by using the `resume` service. Note: calling the `resume` service while the turtle is moving will not do anything. The same 
goes for calling `pause` if the turtle is already stationary

Example of `resume` call. You can call `pause` the same way. 
```bash
rosservice call \resume '{}'
```



### 2-DOF arm visualization
To run the 2-DOF arm visualization, run the `arm_mark.launch` launchfile. 
```bash
roslaunch homework2 arm_mark.launch use_jsp:=(true or false) [mark_pub_freq:=freq] [arm_pub_freq:=freq]
```

The `use_jsp` argument determines if the visualization will running with gui control or with trajectory control. In gui control, you can directly control the joint angles of the robot.

https://user-images.githubusercontent.com/90436131/138295009-5fa19e68-b48e-42a5-bae0-e964633cbe94.mp4

In trajecory control, joint angles are sent to the robot and cause this animation

https://user-images.githubusercontent.com/90436131/138295193-2fbd0781-56c8-412c-b69b-f46c82e99ade.mp4


where the changing shape represents the end-effector crossing the y-axis. 

Set `use_jsp` to true to activate gui control and to false to activate trajectory control. Note: Unlike the other parameters, `use_jsp` must be set. Failure to do so will result in an error. 

The last two parameters are optional: `mark_pub_freq` controls the publishing rate of the end-effector
marker, defaulted at 10Hz, and `arm_pub_freq` controls the publishing rate of the joint angles in 
trajectory control, defaulted at 20Hz. 

You can change parameters of the visualization, such as length and thickness of the arm's links, in
the `arm.yaml`




