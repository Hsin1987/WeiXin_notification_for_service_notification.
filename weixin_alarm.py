import requests
import json
"""
Setting you corp account (XXXXXXXX) and application info (YYYYYYYY & 00000000) below.

Note:
Now, it's for text message notification. But it could do more.
"""
# Setting you corp account (XXXXXXXX) and application info (YYYYYYYY & 00000000) below.
# WeiXin Service Setting
corp_id = 'XXXXXXXX'
corp_secret = 'YYYYYYYY'
agent_id = 00000000
# Setting access_token log file
file_path = '/tmp/access_token.log'


# Access token, use it when the saved token became invalid.
def get_access_token():
    get_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (corp_id, corp_secret)
    print(get_token_url)
    r = requests.get(get_token_url)
    request_json = r.json()
    this_access_token = request_json['access_token']
    r.close()
    # Write the token into file
    try:
        f = open(file_path, 'w+')
        f.write(this_access_token)
        f.close()
    except Exception as e:
        print(e)

    # Return the access_token
    return this_access_token


class WXAlarm:
    def __init__(self):
        self.access_token = get_access_token()

    def get_access_token_from_file(self):
        try:
            f = open(file_path, 'r+')
            this_access_token = f.read()
            f.close()
            return this_access_token
        except Exception as e:
            print(e)

    def sent(self, message,  to_user='@all'):
        flag = True
        while (flag):
            try:
                #to_user = '@all'
                #message = "FIRE FIRE"
                send_message_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % self.access_token
                message_params = {
                    "touser": to_user,
                    "msgtype": "text",
                    "agentid": agent_id,
                    "text": {
                        "content": message
                    },
                    "safe": 0
                }
                r = requests.post(send_message_url, data=json.dumps(message_params))
                print('post success %s ' % r.text)

                # Determine whether sending is successful or not. If not, execute exception function.
                request_json = r.json()
                errmsg = request_json['errmsg']
                if errmsg != 'ok': raise
                # If it's successful , change the flag.
                flag = False
            except Exception as e:
                print(e)
                self.access_token = get_access_token()



