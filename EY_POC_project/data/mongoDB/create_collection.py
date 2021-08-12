import pymongo

uri = "mongodb://usndtaxeyccdb01:Vxw7l67DhObOkVBwRS7uo0grpG33nw7e92zo8Pf6tqbUonw6jjXelvF9Fa4Axl4vx9ealHUSqU0G6itrHY4gjg==@usndtaxeyccdb01.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@usndtaxeyccdb01@"
client = pymongo.MongoClient(uri)


binaryDB = client["IntentBinaryTree"]

expert_rule_set_col = binaryDB["ExpertRuleSet"]

dummy_dict = {"intent": "intent_id",
              "type": "pass",
              "input": [],
              "link": False,
              "left": "sim_1",
              "right": "sim_2",
              "parent": None
            }

# x = expert_rule_set_col.insert_one(dummy_dict)

x = expert_rule_set_col.find_one()

print(x)