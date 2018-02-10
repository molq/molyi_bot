#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from My_beauty_housekeeper.utils.time_tools import ret_passtime
from My_beauty_housekeeper.weixinbot.myController import MyController

__author__ = 'molq'


def orderfilter(msg):
    isroot=False
    if("q"==msg['FromUserName']):isroot=True
    if(msg['Text']=='/聊天'):
        mymsg = {"order": 'tuling'}
        return mymsg


def normalfilter(msg):
    if(msg['FromUserName']=='土豆' or msg['FromUserName']=='杨徐峰'):
        # itchat.send("傻逼,蚊仔找你聊天,快出来 ")
        friend=MyController.myfriendslist[msg['FromUserName']]

        lasttime= ret_passtime(MyController.myfriendslist['last_com_time'])

        if(lasttime<WIATING_TIME and ):
            mymsg={"reply":'请稍等,也许他不在我已经去叫他了(回复聊天可以与我进行聊天)'}
            return mymsg
        else:pass
    if (msg['Text'] == '聊天'):
        mymsg={"order":'tuling'}
        return mymsg
    else:
        pass
    pass


def resolve_msg(replymsg,msg):
    if(replymsg==''):return ""
    if(replymsg["order"]=="tuling"):
        return tuling(msg['Text'])
    if(replymsg["reply"]!=None and replymsg["reply"]!=""):
        return replymsg["reply"]



def dofilter(msg):
    replymsg=""
    if("/".startswith(msg['Text'])):
        replymsg= orderfilter(msg)
    else:
        replymsg= normalfilter(msg)

    return  resolve_msg(replymsg,msg)
