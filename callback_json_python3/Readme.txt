注意事项
1.WXBizMsgCrypt.py文件封装了WXBizMsgCrypt接口类，提供了用户接入企业微信的三个接口，Sample.py文件提供了如何使用这三个接口的示例，ierror.py提供了错误码。
2.WXBizMsgCrypt封装了VerifyURL, DecryptMsg, EncryptMsg三个接口，分别用于开发者验证回调url，收到用户回复消息的解密以及开发者回复消息的加密过程。使用方法可以参考Sample.py文件。
3.加解密协议请参考企业微信官方文档。
4.本代码用到了pycrypto第三方库，请开发者自行安装此库再使用。