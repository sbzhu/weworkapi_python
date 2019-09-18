#!/usr/bin/env python
# -*- coding:utf-8 -*-
##
 # Copyright (C) 2018 All rights reserved.
 #
 # @File CorpApi.py
 # @Brief
 # @Author abelzhu, abelzhu@tencent.com
 # @Version 1.0
 # @Date 2018-02-24
 #
 #

from AbstractApi import *

CORP_API_TYPE = {
        'GET_ACCESS_TOKEN' : ['/cgi-bin/gettoken', 'GET'],
        'USER_CREATE' 	   : ['/cgi-bin/user/create?access_token=ACCESS_TOKEN', 'POST'],
        'USER_GET' 	   : ['/cgi-bin/user/get?access_token=ACCESS_TOKEN', 'GET'],
        'USER_UPDATE'      : ['/cgi-bin/user/update?access_token=ACCESS_TOKEN', 'POST'],
        'USER_DELETE' 	   : ['/cgi-bin/user/delete?access_token=ACCESS_TOKEN', 'GET'],
        'USER_BATCH_DELETE': ['/cgi-bin/user/batchdelete?access_token=ACCESS_TOKEN', 'POST'],
        'USER_SIMPLE_LIST': ['/cgi-bin/user/simplelist?access_token=ACCESS_TOKEN', 'GET'],
        'USER_LIST' 	   : ['/cgi-bin/user/list?access_token=ACCESS_TOKEN', 'GET'],
        'USERID_TO_OPENID' : ['/cgi-bin/user/convert_to_openid?access_token=ACCESS_TOKEN', 'POST'],
        'OPENID_TO_USERID' : ['/cgi-bin/user/convert_to_userid?access_token=ACCESS_TOKEN', 'POST'],
        'USER_AUTH_SUCCESS': ['/cgi-bin/user/authsucc?access_token=ACCESS_TOKEN', 'GET'],

        'DEPARTMENT_CREATE': ['/cgi-bin/department/create?access_token=ACCESS_TOKEN', 'POST'],
        'DEPARTMENT_UPDATE': ['/cgi-bin/department/update?access_token=ACCESS_TOKEN', 'POST'],
        'DEPARTMENT_DELETE': ['/cgi-bin/department/delete?access_token=ACCESS_TOKEN', 'GET'],
        'DEPARTMENT_LIST'  : ['/cgi-bin/department/list?access_token=ACCESS_TOKEN', 'GET'],

        'TAG_CREATE' 	   : ['/cgi-bin/tag/create?access_token=ACCESS_TOKEN', 'POST'],
        'TAG_UPDATE' 	   : ['/cgi-bin/tag/update?access_token=ACCESS_TOKEN', 'POST'],
        'TAG_DELETE'  	   : ['/cgi-bin/tag/delete?access_token=ACCESS_TOKEN', 'GET'],
        'TAG_GET_USER' 	   : ['/cgi-bin/tag/get?access_token=ACCESS_TOKEN', 'GET'],
        'TAG_ADD_USER' 	   : ['/cgi-bin/tag/addtagusers?access_token=ACCESS_TOKEN', 'POST'],
        'TAG_DELETE_USER'  : ['/cgi-bin/tag/deltagusers?access_token=ACCESS_TOKEN', 'POST'],
        'TAG_GET_LIST' 	   : ['/cgi-bin/tag/list?access_token=ACCESS_TOKEN', 'GET'],

        'BATCH_JOB_GET_RESULT' : ['/cgi-bin/batch/getresult?access_token=ACCESS_TOKEN', 'GET'],

        'BATCH_INVITE'     : ['/cgi-bin/batch/invite?access_token=ACCESS_TOKEN', 'POST'],

        'AGENT_GET' 	   : ['/cgi-bin/agent/get?access_token=ACCESS_TOKEN', 'GET'],
        'AGENT_SET' 	   : ['/cgi-bin/agent/set?access_token=ACCESS_TOKEN', 'POST'],
        'AGENT_GET_LIST'   : ['/cgi-bin/agent/list?access_token=ACCESS_TOKEN', 'GET'],

        'MENU_CREATE' : ['/cgi-bin/menu/create?access_token=ACCESS_TOKEN', 'POST'], ## TODO
        'MENU_GET' 	   : ['/cgi-bin/menu/get?access_token=ACCESS_TOKEN', 'GET'],
        'MENU_DELETE' 	   : ['/cgi-bin/menu/delete?access_token=ACCESS_TOKEN', 'GET'],

        'MESSAGE_SEND' 	   : ['/cgi-bin/message/send?access_token=ACCESS_TOKEN', 'POST'],
        'MESSAGE_REVOKE'   : ['/cgi-bin/message/revoke?access_token=ACCESS_TOKEN', 'POST'],

        'MEDIA_GET' 	   : ['/cgi-bin/media/get?access_token=ACCESS_TOKEN', 'GET'],

        'GET_USER_INFO_BY_CODE' : ['/cgi-bin/user/getuserinfo?access_token=ACCESS_TOKEN', 'GET'],
        'GET_USER_DETAIL'  : ['/cgi-bin/user/getuserdetail?access_token=ACCESS_TOKEN', 'POST'],

        'GET_TICKET' 	   : ['/cgi-bin/ticket/get?access_token=ACCESS_TOKEN', 'GET'],
        'GET_JSAPI_TICKET' : ['/cgi-bin/get_jsapi_ticket?access_token=ACCESS_TOKEN', 'GET'],

        'GET_CHECKIN_OPTION' : ['/cgi-bin/checkin/getcheckinoption?access_token=ACCESS_TOKEN', 'POST'],
        'GET_CHECKIN_DATA' : ['/cgi-bin/checkin/getcheckindata?access_token=ACCESS_TOKEN', 'POST'],
        'GET_APPROVAL_DATA': ['/cgi-bin/corp/getapprovaldata?access_token=ACCESS_TOKEN', 'POST'],

        'GET_INVOICE_INFO' : ['/cgi-bin/card/invoice/reimburse/getinvoiceinfo?access_token=ACCESS_TOKEN', 'POST'],
        'UPDATE_INVOICE_STATUS' :
            ['/cgi-bin/card/invoice/reimburse/updateinvoicestatus?access_token=ACCESS_TOKEN', 'POST'],
        'BATCH_UPDATE_INVOICE_STATUS' :
            ['/cgi-bin/card/invoice/reimburse/updatestatusbatch?access_token=ACCESS_TOKEN', 'POST'],
        'BATCH_GET_INVOICE_INFO' :
            ['/cgi-bin/card/invoice/reimburse/getinvoiceinfobatch?access_token=ACCESS_TOKEN', 'POST'],

        'APP_CHAT_CREATE'  : ['/cgi-bin/appchat/create?access_token=ACCESS_TOKEN', 'POST'],
        'APP_CHAT_GET'     : ['/cgi-bin/appchat/get?access_token=ACCESS_TOKEN', 'GET'],
        'APP_CHAT_UPDATE'  : ['/cgi-bin/appchat/update?access_token=ACCESS_TOKEN', 'POST'],
        'APP_CHAT_SEND'    : ['/cgi-bin/appchat/send?access_token=ACCESS_TOKEN', 'POST'],

        'MINIPROGRAM_CODE_TO_SESSION_KEY' : ['/cgi-bin/miniprogram/jscode2session?access_token=ACCESS_TOKEN', 'GET'],
}

class CorpApi(AbstractApi) :
    def __init__(self, corpid, secret) :
        self.corpid = corpid
        self.secret = secret
        self.access_token = None

    def getAccessToken(self) :
        if self.access_token is None :
            self.refreshAccessToken()
        return self.access_token

    def refreshAccessToken(self) :
        response = self.httpCall(
                CORP_API_TYPE['GET_ACCESS_TOKEN'],
                {
                    'corpid'    :   self.corpid,
                    'corpsecret':   self.secret,
                })
        self.access_token = response.get('access_token')

