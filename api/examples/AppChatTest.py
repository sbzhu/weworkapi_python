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

chatid = "test210";
try :
##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_CREATE'],
            {
                'name' : 'appchat_test',
                'owner' : 'ZhuBiaoYi',
                'userlist' : ['LiShuang', 'ZhuShengBen', 'LinJianEn', 'ZhuBiaoYi', 'XuBin', 'yangpeiyi', 'HaLuoTeQu', 'lucky', 'raindong', 'simon', 'Wang', 'ZhaoDong', 'DengLinSheng', 'Li'],
                'chatid' : chatid,
            })
    print response 
    chatid = response['chatid']
except ApiException as e :
    print e.errCode, e.errMsg

try :
    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_UPDATE'],
            {
                'chatid' : chatid,
                'name' : 'appchat_test_new_name',
                'owner' : 'ZhuShengBen',
                'add_user_list' : ['huqiqi', 'Wang']
            })
    print response 

    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_UPDATE'],
            {
                'chatid' : chatid,
                'name' : '应用发消息测试',
                'owner' : 'ZhuBiaoYi',
                'del_user_list' : 'huqiqi',
            })
    print response 

    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_SEND'],
            {
                'chatid':chatid,
                'msgtype' : 'text',
                'text' : {'content':'我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党'},
                'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'safe' : 1,
            })
    print response 

    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_SEND'],
            {
                'chatid':chatid,
                'msgtype' : 'image',
                'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'image' : {
                    'media_id':'3A9Jo9CHit_5UTfOVE38_067dUJQlLs30mOa9FC0a4jEGeoQgpLCZgc7rEza6TbfB',
                },
                'safe' : 1,
            })
    print response 

    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_SEND'],
            {
                'chatid':chatid,
                'msgtype' : 'file',
                'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'file' : {
                    'media_id':'35L7MmcpGdyFfqjbGhbECCkGcaNsUajaPQifGLJq_H5E',
                },
                'safe' : 1,
            })
    print response 


    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_SEND'],
            {
                'chatid':chatid,
                'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'msgtype' : 'voice',
                'voice' : {
                    'media_id':'3x1yb34061fDXjyUXy2rWNd-a-hWe-l8eTw2VKyh3bDQ',
                },
                'safe' : 1,
            })
    print response 

    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_SEND'],
            {
                'chatid':chatid,
                'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'msgtype' : 'video',
                'video' : {
                    'media_id':'3neA1ypnC3k5QnAZqvyVvCesFYUrXietU5F-Ipnj6ZobiD-PuFlXngzPplWXibw9r',
                },
                'safe' : 1,
            })
    print response 

    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_SEND'],
            {
                'chatid':chatid,
                'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'msgtype' : 'news',
		"news" : {
		    "articles" : [
			{
			    "title" : "图文消息",
			    "description" : "今年中秋节公司有豪礼相送",
			    "url" : "URL",
			    "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png",
			    "btntxt":"更多",
			},
			{
			    "title" : "图文消息",
			    "description" : "今年中秋节公司有豪礼相送",
			    "url" : "URL",
			    "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png",
			    "btntxt":"更多",
			},
			{
			    "title" : "图文消息",
			    "description" : "今年中秋节公司有豪礼相送",
			    "url" : "URL",
			    "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png",
			    "btntxt":"更多",
			},
                    ]},
                    'safe' : 1, 
		}, 
            )
    print response 

    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_SEND'],
            {
                'chatid':chatid,
                'msgtype' : 'textcard',
                'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'textcard' : {
                    'title':'我是文本卡片消息',
                    'description' : 'aaaaaaa',
                    'url' : 'www.qq.com',
                    'btntxt' : '更多',
                },
                'safe' : 1,
            })
    print response 

    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_SEND'],
            {
                'chatid':chatid,
                "msgtype" : "mpnews",
                "mpnews": { 
                    "articles" : [
                        { 
                            "title" : "图文消息(mpnews)",
                            "thumb_media_id" : "3uFTZs4MRTr-OwUArqaoXPyqtuedcwCUW1x4sgKcOeQc",
                            "author" : "author",
                            "content" : "content",
                            "digest" : "我是图文"
                        },
                        { 
                            "title" : "图文消息(mpnews)",
                            "thumb_media_id" : "3uFTZs4MRTr-OwUArqaoXPyqtuedcwCUW1x4sgKcOeQc",
                            "author" : "author",
                            "content" : "content",
                            "digest" : "我是图文"
                        },
                        { 
                            "title" : "图文消息(mpnews)",
                            "thumb_media_id" : "3uFTZs4MRTr-OwUArqaoXPyqtuedcwCUW1x4sgKcOeQc",
                            "author" : "author",
                            "content" : "content",
                            "digest" : "我是图文"
                        },
                    ]
                },
                'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'safe' : 1,
            })
    print response 

except ApiException as e :
    print e.errCode, e.errMsg
