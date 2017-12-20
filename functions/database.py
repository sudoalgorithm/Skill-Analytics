#
# functions to get the filter keywords
#

from cloudant.client import Cloudant
from cloudant.result import Result
from functions.get_client import getClient
import pandas as pd
import json


SKILLS = 'skills'
MARKET = 'market'
P_IND = 'pIndustry'
S_IND = 'sIndustry'
P_SKILL = 'pSkill'
SPECIALITY = 'speciality'

def getFilters():
    
    client = getClient()
    filter_db = client['filters']
    lists = []
    for doc in filter_db:
        lists.append({doc['name']: doc["list"]})
    return lists

def getAllUsers():

    client = getClient()
    db = client['people']
    data = db.all_docs(include_docs = True)

    rows = []
    for d in data['rows']:
        rows.append(d['doc'])

    df = pd.DataFrame(rows)
    del df['_rev'], df['_id']
    return df
    

