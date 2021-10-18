#!/usr/bin/env python3
# File with TrajUtil for Figure 8 trajectory 

# Project imports

# Python imports

# 3rd-party imports
import numpy as np

class TrajUtil:
    """
    Collection of helper functions for getting the x,y component of position, 
        velocity, and acceleration for figure 8 trajectory. There is also a
        function for getting the linear and rotational velocity.
    """
    def __init__(self, width_m, height_m, period_s):
        """
        Constructor for utility class. 

        Args:
        float width_m:
            The width of the figure 8 in meters
        float height_m:
            The height of the figure 8 in meters
        float period_s:
            How fast a robot should complete the figure 8 in seconds

        Public members:
        float width_m:
            The width of the figure 8 in meters
        float height_m:
            The height of the figure 8 in meters
        float period_s:
            How fast a robot should complete the figure 8 in seconds
        """
        self.width_m = width_m
        self.height_m = height_m
        self.period_s = period_s

    def get_x(self, time_s):
        """
        Given a time, return the x position of figure 8-trajectory, where  

        x = (width/2)*sin((2*pi*time_s) / period)

        Args:
        float time_s:
            time since robot started doing figure 8 in seconds
        
        Rtn:
        float x_m:
            x position of the robot in meters
        """
        x = (self.width_m/2.) * np.sin( (2*np.pi * time_s) / self.period_s)
        return x

    def get_y(self, time_s):
        """
        Given a time, return the y position of figure 8-trajectory, where  

        y = (height/2)*sin((4*pi*time_s) / period)

        Args:
        float time_s:
            time since robot started doing figure 8 in seconds
        
        Rtn:
        float y_m:
            y position of the robot in meters
        """
        y = (self.height_m/2.) * np.sin( (4*np.pi * time_s) / self.period_s)
        return y

    def get_x_dot(self, time_s):
        """
        Given a time, return the x velocity of figure 8-trajectory, where  

        x_dot = (width*pi / period) * cos((2*pi*time_s) / period)

        Args:
        float time_s:
            time since robot started doing figure 8 in seconds
        
        Rtn:
        float x_ms:
            x velocity of the robot in meters per second
        """
        x_dot = ( (np.pi*self.width_m) / self.period_s) * np.cos( (2*np.pi * time_s) / self.period_s)
        return x_dot

    def get_y_dot(self, time_s):
        """
        Given a time, return the y velocity of figure 8-trajectory, where  

        y_dot = (2pi*height / period) * cos((4*pi*time_s) / period)

        Args:
        float time_s:
            time since robot started doing figure 8 in seconds
        
        Rtn:
        float y_ms:
            y velocity of the robot in meters per second
        """
        y_dot = ( (2*np.pi*self.height_m) / self.period_s) * np.cos( (4*np.pi * time_s) / self.period_s)
        return y_dot

    def get_x_ddot(self, time_s):
        """
        Given a time, return the x acceleration of figure 8-trajectory, where  

        x_ddot = A * sin((2*pi*time_s) / period)
        A = (-2 * np.pi^2 * width) / period^2

        Args:
        float time_s:
            time since robot started doing figure 8 in seconds
        
        Rtn:
        float x_mss:
            x acceleration of the robot in meters per second squared
        """
        A = (-2 * np.pi**2 * self.width_m) / self.period_s**2
        x_ddot = A * sin( (2*np.pi*time_s) / self.period )
        return x_ddot

    def get_y_ddot(self, time_s):
        """
        Given a time, return the y acceleration of figure 8-trajectory, where  

        y_ddot = A * sin((4*pi*time_s) / period)
        A = (-8 * np.pi^2 * height) / period^2

        Args:
        float time_s:
            time since robot started doing figure 8 in seconds
        
        Rtn:
        float y_mss:
            y acceleration of the robot in meters per second squared
        """
        A = (-8 * np.pi**2 * self.height_m) / self.period_s**2
        y_ddot = A * np.sin( (4*np.pi*time_s) / self.period_s )
        return y_ddot

    def get_linear_vel(self, time_s):
        """
        Given a time, return the linear velocity command where

        v = sqrt(x_dot**2 + y_dot**2)
        
        Args:
        float time_s:
            time since robot started doing figure 8 in seconds
        
        Rtn:
        float v:
            linear velocity command of the robot in meters per second
        """
        x_dot = self.get_x_dot(time_s)
        y_dot = self.get_y_dot(time_s)
        v = np.sqrt(x_dot**2 + y_dot**2)
        return v

    def get_rotational_vel(self, time_s):
        """
        Given a time, return the rotational velocity command where

        w = ((-x_ddot * y_dot) + (y_ddot * x_dot))/B
        B = x_dot**2 + y_dot**2
        
        Args:
        float time_s:
            time since robot started doing figure 8 in seconds
        
        Rtn:
        float w:
            rotational velocity command of the robot in rads per second
        """
        # Get velocities and rotations
        x_ddot = self.get_x_ddot(time_s)
        y_ddot = self.get_y_ddot(time_s)
        x_dot = self.get_x_dot(time_s)
        y_dot = self.get_y_dot(time_s)
        
        bottom = x_dot**2 + y_dot**2
        top = ((-1*x_ddot) * y_dot) + (y_ddot * x_dot)
        w = top/bottom
        return w

