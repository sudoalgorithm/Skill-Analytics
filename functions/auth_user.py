#
# functions to auth login
#

from functions.get_client import getClient
from cloudant.client import Cloudant
import json, os

def auth(username, password):

    client = getClient()
    users_db = client['users']
    
    for u in users_db:
        if password == u['password'] and username == u['name']:
            client.disconnect()
            return True, u['id']
    
    client.disconnect()
    return False, None

def checkID(id):

    client = getClient()
    users_db = client['users']
    
    for u in users_db:
        if u['id']==id:
            client.disconnect()
            return ({"name":u['name'], "password":u['password'], "id":u['id']})
