import os

print(os.environ)

from onepush import notify

PUSH_PLUS_TOKEN = os.environ['PUSH_PLUS_TOKEN']
AGENTID = os.environ['AGENTID']
CORPID = os.environ['CORPID']
CORPSECRET = os.environ['CORPSECRET']
PROVIDER = os.environ['PROVIDER']


with open('output.log', 'r', encoding='utf-8') as f:
    log_content = f.read()


if "Message: OK" not in log_content:
    # if PROVIDER == 'pushplus':
    #     notify('pushplus', token=PUSH_PLUS_TOKEN, title='星铁签到_Warning', content=log_content)
    # elif PROVIDER == '1':
    n = get_notifier('wechatworkapp')
    print(n.params)    
    response = n.notify(corpid=CORPID,corpsecret=CORPSECRET,agentid=AGENTID,title='星铁签到',content=log_content)
    print(response.text)    

