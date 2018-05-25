# Use WeChat(Corp.) for Alarm Notification.
Here's  the module for WeiXin(Corp.) messsange notification.
1. "notification_weixin_example.py" is an example.
2. Or, you can import the weixin_alarm as an object in your code.
The file, test.py is for refernce.

## Preparation
step 1. Register a WeiXin Corporation Account.

 ※ Free and easily to setup for small biz <less than 200 people.>

step 2. Access the corporation and application info from the WeiXin Corporation Web Page.：
* corpid
* corpsecret
* Agentid

step 3. Check Library
```
sudo apt-get install libssl-dev
sudo pip install -U configparser requests simplejson
```
Step.4 Try the Example: notification_weixin_example.py

## References:
* [Zabbix使用微信发送告警（附Python代码）](http://www.ttlsa.com/zabbix/use-wechat-send-zabbix-msg/)
* [Github-zabbix-alertscripts](https://github.com/vincihu/zabbix-alertscripts/tree/master/AlertWeixin)