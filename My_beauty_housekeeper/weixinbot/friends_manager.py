#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

import asyncio
import itchat

from My_beauty_housekeeper.utils.constant import STATUS_NORMAL
from My_beauty_housekeeper.utils.dict_change import class_to_dict
from My_beauty_housekeeper.weixinbot.Friend import Friend

__author__ = 'molq'

# class Friend_manager(object):
def intFriends():
    friendList = itchat.get_friends(update=True)[:]
    myfriendsList={}
    for friend in friendList:
        f=Friend()
        f.nickname= friend['NickName']
        f.remakename=friend['RemarkName']
        f.username=friend['UserName']
        f.status=STATUS_NORMAL
        myfriendsList[friend['NickName']]=class_to_dict(f)
        # await asyncio.sleep(1)
    return myfriendsList




