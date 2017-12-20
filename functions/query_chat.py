from pprint import pprint
import json 

#Loading the filter.json data file
with open('filters.json') as data_file: 
	data = json.load(data_file)

query = {}

#Initializing an input (for serach)
def query_chat(input):



    for x in data.keys():
        query[x] = ""

    
    checkContext("market", input)
    checkContext("pIndustry", input)
    checkContext("pSkills", input)
    checkContext("sIndustry", input)
    checkContext("skills", input)
    checkContext("speciality", input)
    
    print query

    with open('data.json', 'w') as f:
        json.dump(query, f, ensure_ascii=False)

def checkContext(context, input):
        for x in data[context]:
            if(input in x):
                query[context] = x

i = "WHo is good at DB2 from MEP"

query_chat(i)