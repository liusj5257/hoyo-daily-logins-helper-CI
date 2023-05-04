import os

print(os.environ)

from onepush import get_notifier

PUSH_PLUS_TOKEN = os.environ['PUSH_PLUS_TOKEN']
AGENTID = os.environ['AGENTID']
CORPID = os.environ['CORPID']
CORPSECRET = os.environ['CORPSECRET']
PROVIDER = os.environ['PROVIDER']
WEBHOOK = os.environ['WEBHOOK']
CHANNEL = os.environ['CHANNEL']
with open('output.log', 'r', encoding='utf-8') as f:
    log_content = f.read()


if "Message: OK" not in log_content:
    n = get_notifier(PROVIDER)
    print(n.params)   
    if PROVIDER == 'pushplus':
        response = n.notify(token=PUSH_PLUS_TOKEN,title='星铁签到',content=log_content,webhook=WEBHOOK,channel = CHANNEL)
        print(response.text)    




    # n = get_notifier(PROVIDER)
    # print(n.params)    
    # response = n.notify(corpid=CORPID,corpsecret=CORPSECRET,agentid=AGENTID,title='星铁签到',content=log_content)
    # print(response.text)
