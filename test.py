from weixin_alarm import WXAlarm
import time, datetime

ts = time.time()
alarm = WXAlarm()
count = 0

while count < 5:
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    alarm.sent(st + ": Hello, World", '@all')
    count +=1
