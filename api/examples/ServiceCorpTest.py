#!/usr/bin/env python
# -*- coding:utf-8 -*-
##
 # Copyright (C) 2018 All rights reserved.
 #   
 # @File ServiceCorpTest.py
 # @Brief 
 # @Author abelzhu, abelzhu@tencent.com
 # @Version 1.0
 # @Date 2018-02-24
 #
 #
 
import sys
sys.path.append("../src/")

from ServiceCorpApi import *
from TestConf import * 


## 第三方服务商接口的使用方法
api = ServiceCorpApi(
        "SUITE_ID", 
        "SUITE_SECRET",
        "SUITE_TICKET" 
);

try :
    pre_auth_code = api.httpCall(SERVICE_CORP_API_TYPE['GET_PRE_AUTH_CODE']).get('pre_auth_code')
    print pre_auth_code
except ApiException as e :
    print e.errCode, e.errMsg


## 第三方服务商使用永久授权码调用企业接口的方法
api = ServiceCorpApi(
        "SUITE_ID", 
        "SUITE_SECRET",
        "SUITE_TICKET",
        'AUTH_CORPID',
        'PERMANENT_CODE'
); 
try :
    response = api.httpCall(
            CORP_API_TYPE['USER_GET'],
            { 
                'userid' : 'zhangsan',
            })
    print response
except ApiException as e :
    print e.errCode, e.errMsg
