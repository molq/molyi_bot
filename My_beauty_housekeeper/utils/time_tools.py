#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

import asyncio

from My_beauty_housekeeper.config.log import logger
from My_beauty_housekeeper.utils.constant import WIATING_TIME

__author__ = 'molq'



def ret_passtime(befor_date):
    time.sleep(1)
    if(befor_date== None or befor_date==''):
        return WIATING_TIME*2

    else:
        now = time.time()
        logger.info(str(now - befor_date) + "秒")
        return now-befor_date



ret_passtime(time.time())
