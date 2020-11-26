
# About
weworkapi_python 是为了简化开发者对企业微信API接口的使用而设计的，API调用库系列之python版本      
本库仅做示范用，并不保证完全无bug；  
作者会不定期更新本库，但不保证与官方API接口文档同步，因此一切以[官方文档](https://work.weixin.qq.com/api/doc)为准。

更多来自个人开发者的其它语言的库推荐：  
python : https://github.com/sbzhu/weworkapi_python  abelzhu@tencent.com(企业微信团队)  
ruby ： https://github.com/mycolorway/wework  MyColorway(个人开发者)  
php : https://github.com/sbzhu/weworkapi_php  abelzhu@tencent.com(企业微信团队)  
golang : https://github.com/sbzhu/weworkapi_golang  ryanjelin@tencent.com(企业微信团队)   
golang : https://github.com/doubliekill/EnterpriseWechatSDK  1006401052yh@gmail.com(个人开发者)  

# Director 

├── api // API 接口  
│   ├── examples // API接口的测试用例  
│   ├── README.md  
│   └── src // API接口的关键逻辑  
├── conf.py  
├── README.md  

# Usage
将本项目下载到你的目录，既可直接引用相关文件  
详细使用方法参考examples路径下的测试用例

# 关于token的缓存
token是需要缓存的，不能每次调用都去获取token，[否则会中频率限制](https://work.weixin.qq.com/api/doc#10013/%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%BC%93%E5%AD%98%E5%92%8C%E5%88%B7%E6%96%B0access_token)  
在本库的设计里，token是以类里的一个变量缓存的  
比如api/src/CorpApi.py 里的access_token变量  
在类的生命周期里，这个accessToken都是存在的， 当且仅当发现token过期，CorpAPI类会自动刷新token   
刷新机制在 api/src/AbstractApi.py  
所以，使用时，只需要全局实例化一个CorpAPI类，不要析构它，就可一直用它调函数，不用关心 token  
```
api = CorpAPI(corpid, corpsecret);
api.dosomething()
api.dosomething()
api.dosomething()
....
```
当然，如果要更严格的做的话，建议自行修改，全局缓存token，比如存redis、存文件等，失效周期设置为2小时。

# Contact us
abelzhu@tencent.com  

# 
