# -*- coding: utf-8 -*-
"""
Created on Thu May 20 08:41:39 2021

@author: Juan Francisco Guarracino
"""

# This script is to control the daq NI usb-6343 plugged in the right 
# intracellular ephys setup
import nidaqmx


device_name= ['Dev1']
signal_channel= list(range(0,20,1))

def add_ai_channels(device_list,channel_list):
    """ This function is used to connect the daq to the computer.
    The first argument is a list of strings, the devices' names have to be
    checked in NI-MAX. The second argument is a list of strings of all the
    analog input channels you want to add"""
    for device in device_list:
        for channel in channel_list:
            with nidaqmx.Task() as task:
                task.ai_channels.add_ai_voltage_chan(device+'/ai'+
                                                     str(channel))
                print('channel '+channel+'from device '+device+' added')