import requests
import json
"""
Setting you corp account (XXXXXXXX) and application info (YYYYYYYY & 00000000) below.
"""
# Relative WeiXIn Setting
corp_id = 'XXXXXXXX'
corp_secret = 'YYYYYYYY'
agent_id = 00000000
# Setting access_token log file
file_path = '/tmp/access_token.log'


def get_access_token_from_file():
    try:
        f = open(file_path, 'r+')
        this_access_token = f.read()
        print('get success %s' % this_access_token)
        f.close()
        return this_access_token
    except Exception as e:
        print(e)


# Access token, use it when the saved token became invalid.
def get_access_token():
    get_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (corp_id, corp_secret)
    print(get_token_url)
    r = requests.get(get_token_url)
    request_json = r.json()
    this_access_token = request_json['access_token']
    print(this_access_token)
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


# snedMessage until success
flag = True
while (flag):
    # Access token from file
    access_token = get_access_token_from_file()
    try:
        to_user = '@all'
        message = "FIRE FIRE"
        send_message_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % access_token
        print(send_message_url)
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
        access_token = get_access_token()