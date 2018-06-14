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

import random

from CorpApi import *
from TestConf import * 

## test
api = CorpApi(TestConf['CORP_ID'], TestConf['APP_SECRET'])

try :
##
    response = api.httpCall(
            CORP_API_TYPE['MINIPROGRAM_CODE_TO_SESSION_KEY'],
            {
                "js_code" : "sVqtL3itg0L30LTGJtZ_isKC0efG5FqGw470fVp8Dpw",
                "grant_type" : "authorization_code"
            })
    print response 

except ApiException as e :
    print e.errCode, e.errMsg

