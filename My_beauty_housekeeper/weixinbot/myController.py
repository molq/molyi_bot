#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itchat
from itchat.content import *

from My_beauty_housekeeper.utils.dict_change import class_to_dict
from My_beauty_housekeeper.weixinbot.friends_manager import intFriends

__author__ = 'molq'

class MyController(object):
    myfriendslist={}
    #初始化暂定
    def __init__(self,):
        itchat.auto_login(hotReload=True)
        self.myfriendslist=intFriends()
        pass

    #根据配置对联系人列表更新(主要是权限什么的)
    def reloadfirends(self,myfriendslist):
        self.myfriendslist=myfriendslist
        pass

    #监听聊天
    def chat_listen(self):
        pass

    #停止所有服务
    def stop(self):
        pass

    # 注册文本消息，绑定到text_reply处理函数
    # text_reply msg_files可以处理好友之间的聊天回复
    @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
    def text_reply(self,msg):
        text = dofilter(msg,)
        if (text != ""):
            itchat.send('%s' % text, msg['FromUserName'])


if __name__ == '__main__':
    itchat.run()
    m= MyController()
    print(m.myfriendslist)
