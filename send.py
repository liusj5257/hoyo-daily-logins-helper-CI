import os

from onepush import notify

PUSH_PLUS_TOKEN = os.environ['PUSH_PLUS_TOKEN']


with open('output.log', 'r', encoding='utf-8') as f:
    log_content = f.read()
notify('pushplus', token=PUSH_PLUS_TOKEN, title='星铁签到', content=log_content)
