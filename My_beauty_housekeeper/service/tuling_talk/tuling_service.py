#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

import requests

__author__ = 'molq'

# 调用图灵机器人的api，采用爬虫的原理，根据聊天消息返回回复内容
def tuling(info):
    appkey = "bc5576f485c54343b727c669dcdb20a5"
    url = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
    req = requests.get(url)
    content = req.text
    data = json.loads(content)
    answer = data['text']
    return answer

