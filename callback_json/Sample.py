#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: jonyqin
# Created Time: Thu 11 Sep 2014 03:55:41 PM CST
# File Name: Sample.py
# Description: WXBizJsonMsgCrypt 使用demo文件
#########################################################################
from WXBizJsonMsgCrypt import WXBizJsonMsgCrypt
import sys

if __name__ == "__main__":   
   # 企业在企业微信后台上设置的密钥相关配置在这里 TODO
   sToken = "xxxxxxx"
   sEncodingAESKey = "xxxxxxx"
   sCorpID = "ww1436e0e65a779aee"
   '''
	------------使用示例一：验证回调URL---------------
	*企业开启回调模式时，企业号会向验证url发送一个get请求 
	假设点击验证时，企业收到类似请求：
	* GET /cgi-bin/wxpush?msg_signature=5c45ff5e21c57e6ad56bac8758b79b1d9ac89fd3&timestamp=1409659589&nonce=263014780&echostr=P9nAzCzyDtyTWESHep1vC5X9xho%2FqYX3Zpb4yKa9SKld1DsH3Iyt3tP3zNdtp%2B4RPcs8TgAE7OaBO%2BFZXvnaqQ%3D%3D 
	* HTTP/1.1 Host: qy.weixin.qq.com

	接收到该请求时，企业应	1.解析出Get请求的参数，包括消息体签名(msg_signature)，时间戳(timestamp)，随机数字串(nonce)以及企业微信推送过来的随机加密字符串(echostr),
	这一步注意作URL解码。
	2.验证消息体签名的正确性 
	3. 解密出echostr原文，将原文当作Get请求的response，返回给企业微信
	第2，3步可以用企业微信提供的库函数VerifyURL来实现。
   '''
   wxcpt=WXBizJsonMsgCrypt(sToken,sEncodingAESKey,sCorpID)
   sVerifyMsgSig="012bc692d0a58dd4b10f8dfe5c4ac00ae211ebeb"
   sVerifyTimeStamp="1476416373"
   sVerifyNonce="47744683"
   sVerifyEchoStr="fsi1xnbH4yQh0+PJxcOdhhK6TDXkjMyhEPA7xB2TGz6b+g7xyAbEkRxN/3cNXW9qdqjnoVzEtpbhnFyq6SVHyA=="
   ret,sEchoStr=wxcpt.VerifyURL(sVerifyMsgSig, sVerifyTimeStamp,sVerifyNonce,sVerifyEchoStr)
   if(ret!=0):
      print "ERR: VerifyURL ret: " + str(ret)
      sys.exit(1)
   else:
      print "done VerifyURL"
      #验证URL成功，将sEchoStr返回给企业号

   print "=============================="
   '''
   ------------使用示例二：对用户回复的消息解密---------------
   用户回复消息或者点击事件响应时，企业会收到回调消息，此消息是经过企业微信加密之后的密文以post形式发送给企业，密文格式请参考官方文档
   假设企业收到企业微信的回调消息如下：
   POST /cgi-bin/wxpush? msg_signature=e3647471e395139e2308c1fa963f2d648a00b90e&timestamp=1409659813&nonce=1372623149 HTTP/1.1
   Host: qy.weixin.qq.com

   { 
    "tousername": "wx5823bf96d3bd56c7", 
    "encrypt": "cjhLUX7UU4yCSelv1vz7T0zT8huF51bAMVWriNvO1FMegHrQZNrtvRxbwf0fUPsFvwqR0U0fgiJNEA5Y30F2MoI2S7vv3EjVQ68C0cjw9frBoUE2Hj0BvFp9h3u6Vbsg4lc1C8AtHdaN8orKuNKkLRLuYEL52R1J3v8olJGZRLnRdVKIivixmX/eQpzgeExtp20jI1HxRP1AAZ6xZoILdqDPO549LO4WeG+685JRUTdiwcY5fjZlqeMxuT4PpMn1X9OWsS7NRj06Wa5E3Tvg4twjWp39KPfOdRte6P1T4JU=", 
    "agentid": 218 
   }

   企业收到post请求之后应该 1.解析出url上的参数，包括消息体签名(msg_signature)，时间戳(timestamp)以及随机数字串(nonce)
   2.验证消息体签名的正确性。 3.将post请求的数据进行json解析，并将"encrypt"标签的内容进行解密，解密出来的明文即是用户回复消息的明文，明文格式请参考官方文档
   第2，3步可以用企业微信提供的库函数DecryptMsg来实现。
   '''

   sReqNonce = "1372623149"
   sReqTimeStamp = "1409659813"

   sReqMsgSig = "e3647471e395139e2308c1fa963f2d648a00b90e"
   sReqData = '{ "tousername": "wx5823bf96d3bd56c7", "encrypt": "cjhLUX7UU4yCSelv1vz7T0zT8huF51bAMVWriNvO1FMegHrQZNrtvRxbwf0fUPsFvwqR0U0fgiJNEA5Y30F2MoI2S7vv3EjVQ68C0cjw9frBoUE2Hj0BvFp9h3u6Vbsg4lc1C8AtHdaN8orKuNKkLRLuYEL52R1J3v8olJGZRLnRdVKIivixmX/eQpzgeExtp20jI1HxRP1AAZ6xZoILdqDPO549LO4WeG+685JRUTdiwcY5fjZlqeMxuT4PpMn1X9OWsS7NRj06Wa5E3Tvg4twjWp39KPfOdRte6P1T4JU=", "agentid": 218 }';
   ret,sMsg=wxcpt.DecryptMsg( sReqData, sReqMsgSig, sReqTimeStamp, sReqNonce)
   if( ret!=0 ):
      print "ERR: DecryptMsg ret: " + str(ret)
      sys.exit(1)
   else:
      print sMsg
   # 解密成功，sMsg即为json格式的明文
   # TODO: 对明文的处理
   # ...
   # ...

   print "=============================="
   
   '''
   ------------使用示例三：企业回复用户消息的加密---------------
   企业被动回复用户的消息也需要进行加密，并且拼接成密文格式的json串。
   假设企业需要回复用户的明文如下：

    { 
            "ToUserName": "mycreate",
            "FromUserName":"wx5823bf96d3bd56c7",
            "CreateTime": 1348831860,
            "MsgType": "text",
            "Content": "this is a test",
            "MsgId": 1234567890123456,
            "AgentID": 128
    }

   为了将此段明文回复给用户，企业应： 1.自己生成时间时间戳(timestamp),随机数字串(nonce)以便生成消息体签名，也可以直接用从企业微信的post url上解析出的对应值。
   2.将明文加密得到密文。   3.用密文，步骤1生成的timestamp,nonce和企业在企业微信设定的token生成消息体签名。   4.将密文，消息体签名，时间戳，随机数字串拼接成json格式的字符串，发送给企业号。
   以上2，3，4步可以用企业微信提供的库函数EncryptMsg来实现。
   '''
   #sRespData = ' { "ToUserName": "mycreate", "FromUserName":"wx5823bf96d3bd56c7", "CreateTime": 1348831860, "MsgType": "text", "Content": "this is a test", "MsgId": 1234567890123456, "AgentID": 128 }';
   sRespData = '{ "ToUserName": "wx5823bf96d3bd56c7", "FromUserName": :mycreate", "CreateTime": 1409659813, "MsgType": "text", "Content": "hello", "MsgId": 4561255354251345929, "AgentID": 218}'
   ret,sEncryptMsg=wxcpt.EncryptMsg(sRespData, sReqNonce, sReqTimeStamp)
   if( ret!=0 ):
      print "ERR: EncryptMsg ret: " + str(ret)
      sys.exit(1)
   else:
      print sEncryptMsg
      #ret == 0 加密成功，企业需要将sEncryptMsg返回给企业号
   print "=============================="
