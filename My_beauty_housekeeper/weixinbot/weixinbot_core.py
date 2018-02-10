#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from My_beauty_housekeeper.weixinbot.myController import MyController

__author__ = 'molq'
from itchat.content import *
import requests
import json
import itchat

from myweixin_bot.msg_filter.myfilter import dofilter

itchat.auto_login(hotReload = True)




# 对于群聊信息，定义获取想要针对某个群进行机器人回复的群ID函数
def group_id(name):
    df = itchat.search_chatrooms(name=name)
    return df[0]['UserName']



@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

# 现在微信加了好多群，并不想对所有的群都进行设置微信机器人，只针对想要设置的群进行微信机器人，可进行如下设置
# @itchat.msg_register(TEXT, isGroupChat=True)
# def group_text_reply(msg):
#     # 当然如果只想针对@你的人才回复，可以设置if msg['isAt']:
#     item = group_id(u'想要设置的群的名称')  # 根据自己的需求设置
#     if msg['ToUserName'] == item:
#         itchat.send(u'%s' % tuling(msg['Text']), item)



