#!/usr/bin/env python
# -*- coding:utf-8 -*-
##
 # Copyright (C) 2018 All rights reserved.
 #   
 # @File ServiceProviderApi.py
 # @Brief 
 # @Author abelzhu, abelzhu@tencent.com
 # @Version 1.0
 # @Date 2018-02-26
 #
 #
 
from AbstractApi import *

SERVICE_PROVIDER_API_TYPE = { 
        'GET_PROVIDER_TOKEN': ['/cgi-bin/service/get_provider_token', 'POST'],
        'GET_LOGIN_INFO'    : ['/cgi-bin/service/get_login_info?access_token=PROVIDER_ACCESS_TOKEN', 'POST'],
        'GET_REGISTER_CODE' : ['/cgi-bin/service/get_register_code?provider_access_token=PROVIDER_ACCESS_TOKEN', 'POST'],
        'GET_REGISTER_INFO' : ['/cgi-bin/service/get_register_info?provider_access_token=PROVIDER_ACCESS_TOKEN', 'POST'],
        'SET_AGENT_SCOPE'   : ['/cgi-bin/agent/set_scope', 'POST'], ### TODO 
        'SET_CONTACT_SYNC_SUCCESS' : ['/cgi-bin/sync/contact_sync_success', 'GET'],
}

class ServiceProviderApi(AbstractApi) :
    def __init__(self, corpid, provider_secret) :
        self.corpid = corpid
        self.provider_secret = provider_secret 

        self.provider_access_token = None

    def getProviderAccessToken(self) :
        if self.provider_access_token is None :
            self.refreshProviderAccessToken()
        return self.provider_access_token

    def refreshProviderAccessToken(self) :
        response = self.httpCall(
                SERVICE_PROVIDER_API_TYPE['GET_PROVIDER_TOKEN'],
                {
                    'corpid'         :   self.corpid, 
                    'provider_secret':   self.provider_secret, 
                })
        self.provider_access_token = response.get('provider_access_token') 

