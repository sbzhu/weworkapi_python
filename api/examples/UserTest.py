#!/usr/bin/env python
# -*- coding:utf-8 -*-
##
 # Copyright (C) 2018 All rights reserved.
 #   
 # @File UserTest.py
 # @Brief 
 # @Author abelzhu, abelzhu@tencent.com
 # @Version 1.0
 # @Date 2018-02-24
 #
 #
 
import sys
sys.path.append("../src/")

from CorpApi import *
from TestConf import * 

## test
api = CorpApi(TestConf['CORP_ID'], TestConf['CONTACT_SYNC_SECRET'])

try :
    ##
    response = api.httpCall(
            CORP_API_TYPE['USER_CREATE'],
            {
                'userid' : 'zhangsan',
                'name' : 'zhangsanfeng',
                'mobile' : '131488888888',
                'email' : 'zhangsan@ipp.cas.cn',
                'department' : 1,
            })
    print response 

    ##
    response = api.httpCall(
            CORP_API_TYPE['USER_GET'],
            { 
                'userid' : 'zhangsan',
            })
    print response

    ##
    response = api.httpCall(
            CORP_API_TYPE['USER_DELETE'],
            { 
                'userid' : 'zhangsan',
            })
    print response

except ApiException as e :
    print e.errCode, e.errMsg

    ##
    response = api.httpCall(
            CORP_API_TYPE['USER_DELETE'],
            { 
                'userid' : 'zhangsan',
            })
    print response


