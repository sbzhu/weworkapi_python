#!/usr/bin/env python
# -*- coding:utf-8 -*-
##
 # Copyright (C) 2018 All rights reserved.
 #   
 # @File ServiceCorp.py
 # @Brief 
 # @Author abelzhu, abelzhu@tencent.com
 # @Version 1.0
 # @Date 2018-02-24
 #
 #
 
from CorpApi import *

SERVICE_CORP_API_TYPE = { 
        'GET_CORP_TOKEN'    : ['/cgi-bin/service/get_corp_token?suite_access_token=SUITE_ACCESS_TOKEN', 'POST'],
        'GET_SUITE_TOKEN'   : ['/cgi-bin/service/get_suite_token', 'POST'], 
        'GET_PRE_AUTH_CODE' : ['/cgi-bin/service/get_pre_auth_code?suite_access_token=SUITE_ACCESS_TOKEN', 'GET'],
        'SET_SESSION_INFO'  : ['/cgi-bin/service/set_session_info?suite_access_token=SUITE_ACCESS_TOKEN', 'POST'], 
        'GET_PERMANENT_CODE': ['/cgi-bin/service/get_permanent_code?suite_access_token=SUITE_ACCESS_TOKEN', 'POST'], 
        'GET_AUTH_INFO'     : ['/cgi-bin/service/get_auth_info?suite_access_token=SUITE_ACCESS_TOKEN', 'POST'], 
        'GET_ADMIN_LIST'    : ['/cgi-bin/service/get_admin_list?suite_access_token=SUITE_ACCESS_TOKEN', 'POST'],
        'GET_USER_INFO_BY_3RD' : ['/cgi-bin/service/getuserinfo3rd?suite_access_token=SUITE_ACCESS_TOKEN', 'GET'],
        'GET_USER_DETAIL_BY_3RD' : ['/cgi-bin/service/getuserdetail3rd?suite_access_token=SUITE_ACCESS_TOKEN', 'POST'],
}

class ServiceCorpApi(CorpApi) :
    def __init__(self, suite_id, suite_secret, suite_ticket, auth_corpid=None, permanent_code=None) :
        self.suite_id = suite_id 
        self.suite_secret = suite_secret
        self.suite_ticket = suite_ticket

        # 调用 CorpAPI 的function， 需要设置这两个参数
        self.auth_corpid = auth_corpid 
        self.permanent_code = permanent_code 

        self.access_token = None
        self.suite_access_token = None

    ## override CorpApi 的 refreshAccessToken， 使用第三方服务商的方法
    def getAccessToken(self) :
        if self.access_token is None :
            self.refreshAccessToken()
        return self.access_token
    def refreshAccessToken(self) :
        response = self.httpCall(
                SERVICE_CORP_API_TYPE['GET_CORP_TOKEN'],
                {
                    "auth_corpid"   : self.auth_corpid, 
                    "permanent_code": self.permanent_code,
                })
        self.access_token = response.get('access_token') 

    ##
    def getSuiteAccessToken(self) :
        if self.suite_access_token is None :
            self.refreshSuiteAccessToken()
        return self.suite_access_token

    def refreshSuiteAccessToken(self) :
        response = self.httpCall(
                SERVICE_CORP_API_TYPE['GET_SUITE_TOKEN'],
                {
                    "suite_id"      : self.suite_id,
                    "suite_secret"  : self.suite_secret,
                    "suite_ticket"  : self.suite_ticket,
                })
        self.suite_access_token= response.get('suite_access_token') 

