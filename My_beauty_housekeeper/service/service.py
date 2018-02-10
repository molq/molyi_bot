#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from My_beauty_housekeeper.utils.time_tools import ret_passtime

__author__ = 'molq'

def tempservice(friend,msg):
    status= friend['status']
    lasttime=friend['last_com_time']
    passtime=ret_passtime(lasttime)
    pass