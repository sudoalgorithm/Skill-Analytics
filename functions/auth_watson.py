import watson_developer_cloud as watson
import json, os

WORKSPACE = 'bd0975f8-a851-4020-b674-b304d5a41d5f'

def getConversationSevice():
    if 'VCAP_SERVICES' in os.environ:
        vcap = json.loads(os.getenv('VCAP_SERVICES'))
        if 'conversation' in vcap:
            creds = vcap['conversation'][0]['credentials']
            user = creds['username']
            password = creds['password']
            conversation = watson.ConversationV1(username=user, password=password, version='2017-04-21')
            return conversation
    elif os.path.isfile('credentials.json'):
        with open('credentials.json') as f:
            vcap = json.load(f)
            creds = vcap['services']['conversation'][0]['credentials']
            user = creds['username']
            password = creds['password']
            conversation = watson.ConversationV1(username=user, password=password, version='2017-04-21')
            return conversation
